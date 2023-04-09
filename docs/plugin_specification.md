# Charles AI Plugin Standard
The purpose of this document is to define the standard for plugins used by the Charles-AI assistant chatbot.

## Plugin Composition
Each plugin is made up of a single python module located at `src/charles_ai/plugin_api/plugin_modules`.

The following must be defined within that module's global namespace:
- `dict` `spec`: Dictionary containing the following keys:
  - `plugin`: String, the name of the plugin
  - `description`: String, a description of what the plugin does.
  - `args`: Dictionary, where keys are the name of each paramenter and values are a description of the parameter.
- `func` `run()`: The function to run when a request is made for the plugin.
  - Must accept `**kwargs` as defined in the `spec.args` dictionary.
  - Must return a string, which will be returned to the AI model as a system message.

## Enabling Plugins
Plugins are enabled by importing them and appending their namespace to `plugin_api.plugins` `within plugin_api/__init__.py`

## Utilities Available to Plugins
### Config
Config should be handled via environment variables. To access them, use this code:
```py
import os

os.getenv("YOUR_ENV_VAR_NAME")
```

The following commonly used config values are accessible via the config module:
```py
from ... import config

config.units
```


### Logging
Python's logging module should be used for logging within plugins. Use the following code to get a logger near the top of the plugin's module:

```py
import logging

logger = logging.getLogger(__name__)
```

Then, use `logger.debug("")`, `logger.info("")`, `logger.warning("")`, `logger.error("")`, or `logger.critical("")` to log information.