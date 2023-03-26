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


def ask(message: str) -> str:
    """Adds the message to the conversation and gets a response from the AI.

    :param message: String, the message from the user
    :return: String, the response from OpenAI
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[initial_prompt, user_info_prompt, {"role": "user", "content": message}],
    )
    # TODO - add additional context to AI requests.

    return response["choices"][0]["message"]["content"]
