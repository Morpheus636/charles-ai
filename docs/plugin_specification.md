# Charles AI Plugin Standard
The purpose of this document is to define the standard for plugins used by the Charles-AI assistant chatbot.

## Plugin Composition
Each plugin is made up of a single python module located at `src/charles_ai/plugin_api/plugin_modules`.

The following must be defined within that module's global namespace:
- `dict` `spec`: Dictionary containing the following keys:
  - `plugin`: String, the name of the plugin
  - `description`: String, a description of what the plugin does.
  - `args`: Dictionary, where keys are the name of each paramenter and values are a description of the parameter.
- `func` `run()`: The function to run when a request is made for the plugin. Must accept `**kwargs` as defined in the `spec.args` dictionary.