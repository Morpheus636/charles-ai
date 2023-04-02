import json


class PluginParserError(Exception):
    pass


def parse(request: str) -> dict:
    """Parses a string as outputted by the AI into a dict.

    :param request: The string output from the AI to parse.
    :return: dict, the parsed, machine-readable request.
    :rasies: PluginParserError - Raised if the request is invalid.
    """
    # Remove formatting.
    request = request.removeprefix("```").removesuffix("```")

    # Attempt to load the string with formatting removed as a JSON.
    try:
        request = json.loads(request)
    except json.JSONDecodeError:
        raise PluginParserError("The request could not be parsed because it is not a valid JSON.")

    # Validate the request
    try:
        assert request.get("plugin")
        assert isinstance(request.get("args"), dict)
    except AssertionError:
        raise PluginParserError("The request is malformed.")
