from . import parser
from .plugin_modules import plugin_datetime, plugin_weather


plugins = [plugin_datetime, plugin_weather]


def get_plugin_specs():
    """Gets a list of all the plugin spec dicts."""
    plugin_specs = []
    for plugin in plugins:
        plugin_specs.append(plugin.spec)


def process_request(request: str) -> str:
    """Processes a request for the plugin API.

    :param request: The string output from the AI to parse.
    :return: string, the output from the appropriate plugin.
    :raises: parser.PluginParserError if the request is invalid.
    """
    # Parse the request.
    # Will raise parser.PluginParserError if the request is invalid.
    request = parser.parse

    plugin_name = request["plugin"]
    for plugin in plugins:
        if plugin.spec["plugin"] == plugin_name:
            return plugin.run(**request["args"])
