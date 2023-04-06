import logging

from . import parser
from .plugin_modules import plugin_datetime, plugin_weather


plugins = [plugin_datetime, plugin_weather]


logger = logging.getLogger(__name__)


def get_plugin_specs():
    """Gets a list of all the plugin spec dicts."""
    logging.debug("Getting all plugin specs")
    plugin_specs = []
    for plugin in plugins:
        logger.debug(f"Found spec: {plugin.spec} in module {plugin.__name__}")
        plugin_specs.append(plugin.spec)
    return plugin_specs


def process_request(request: str) -> str:
    """Processes a request for the plugin API.

    :param request: The string output from the AI to parse.
    :return: string, the output from the appropriate plugin.
    :raises: parser.PluginParserError if the request is invalid.
    """
    logger.debug(f"Attempting to process request: {request}")
    # Parse the request.
    # Will raise parser.PluginParserError if the request is invalid.
    parsed_request = parser.parse(request)

    plugin_name = parsed_request["plugin"]
    logger.debug(f"Request for plugin: {plugin_name}")
    for plugin in plugins:
        if plugin.spec["plugin"] == plugin_name:
            logger.debug(f"Found spec for plugin: {plugin_name}. Running.")
            return plugin.run(**request["args"])
