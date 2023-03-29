import os

import openai

from . import config


# Data state for prompts.
initial_prompt = {
    "role": "system",
    "content": f"You are {config.ai_name}, a helpful AI assistant developed by Morpheus636 and powered by OpenAI. Answer as concisely as possible.",
}

user_info_prompt = {"role": "system", "content": ""}

conversation = []


def setup():
    """Sets up the AI, including API key and user info prompt. This function must be called before any other AI engine function."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    user_info_prompt["content"] = os.getenv("AI_USER_INFO")


def ask(new_message: str) -> str:
    """Adds the message to the conversation and gets a response from the AI.

    :param message: String, the message from the user
    :return: String, the response from OpenAI
    """
    # Message history algorithm.
    # Note that the user can also manually reset the history by adding a thumbs up reaction.
    messages = [initial_prompt, user_info_prompt]
    # Grab the most recent 10 items from the conversation history, if they exist.
    for i in range(0, 10):
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

    # Save conversation history and return.
    response = api_response["choices"][0]["message"]["content"]
    conversation.append({"role": "user", "content": new_message})
    conversation.append({"role": "assistant", "content": response})
    return response
