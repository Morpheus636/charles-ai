import json
import os

import openai

from . import plugin_api


# Data state for prompts.
system_instruction = {
    "role": "system",
    "content": "",
}

user_info_prompt = {"role": "system", "content": ""}

conversation = []


def setup():
    """Sets up the AI, including API key and user info prompt. This function must be called before any other AI engine function."""
    global system_instruction
    global user_info_prompt

    openai.api_key = os.getenv("OPENAI_API_KEY")
    user_info_prompt["content"] = os.getenv("AI_USER_INFO")

    # Load system instruction
    with open("src/charles_ai/system_instruction.txt", "r") as file:
        system_instruction["content"] = (
            file.read()
            + "\n```\n"
            + json.dumps({"plugins": plugin_api.get_plugin_specs()})
            + "\n```"
        )


def ask(new_message: str) -> str:
    """Adds the message to the conversation and gets a response from the AI.

    :param message: String, the message from the user
    :return: String, the response from OpenAI
    """
    global conversation
    # Message history algorithm.
    # Note that the user can also manually reset the history by adding a thumbs up reaction.
    messages = [system_instruction, user_info_prompt]
    # Grab the most recent 10 items from the conversation history, if they exist.
    for i in range(0, 9):
        index = len(conversation) - 1 - i
        if index >= 0:
            message = conversation[index]
            if message:
                messages.append(message)
    messages.append({"role": "user", "content": new_message})

    # OpenAI API request.
    api_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    # Save conversation history.
    # TODO - garbage-collect/remove old conversation history.
    response = api_response["choices"][0]["message"]["content"]
    conversation.append({"role": "user", "content": new_message})
    conversation.append({"role": "assistant", "content": response})

    # Attempt to process the response as a plugin request, then recursively
    # call ask() until the response is not a request for a plugin
    # and return the final response. PluginParserError is raised if the request
    # is not for the plugin API.
    try:
        return ask(plugin_api.process_request(response))
    except plugin_api.parser.PluginParserError:
        return response
