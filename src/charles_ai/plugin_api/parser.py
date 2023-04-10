import json
import logging


logger = logging.getLogger(__name__)


class PluginParserError(Exception):
    pass


def parse(request: str) -> dict:
    """Parses a string as outputted by the AI into a dict.

    :param request: The string output from the AI to parse.
    :return: dict, the parsed, machine-readable request.
    :rasies: PluginParserError - Raised if the request is invalid.
    """
    logger.debug("Attempting to parse request")
    # Look for a plugin request in the message.
    if "```" in request:
        request = request.split("```")
        logger.debug(request)
        request = request[1]

    # Attempt to load the string with formatting removed as a JSON.
    try:
        request = json.loads(request)
        logger.debug("Successfully loaded JSON.")
    except json.JSONDecodeError:
        logger.debug("Failed to parse request: Invalid JSON.")
        raise PluginParserError("The request could not be parsed because it is not a valid JSON.")

    # Validate the request
    try:
        assert request.get("plugin")
        logger.debug("Plugin key exists in request.")
        assert isinstance(request.get("args"), dict)
        logger.debug("Args key exists in request.")
    except AssertionError:
        logger.debug("Failed to parse request: Malformed.")
        raise PluginParserError("The request is malformed.")

    logger.debug("Successfully parsed request.")
    return request
