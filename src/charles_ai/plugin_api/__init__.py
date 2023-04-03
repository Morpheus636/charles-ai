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
    :return: dict, the parsed, machine-readable request.
    :rasies: InvalidRequestError - Raised if the request is invalid.
    """
    # Attempt to parse the request.
    # If the request is not a plugin JSON, return it as-is.
    try:
        request = parser.parse(request)
    except parser.PluginParserError:
        return request

    plugin_name = request["plugin"]
    for plugin in plugins:
        if plugin.spec["plugin"] == plugin_name:
            plugin.run(**request["args"])  # TODO - Plugin args
