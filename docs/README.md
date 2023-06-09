# Charles AI
An AI assistant Discord bot powered by OpenAI's GPT-3.5 model.

## Technologies
- Python
- OpenAI's Chat API

## Usage
1. Deploy an instance of the bot (see [Deployment](#Deployment) below for instructions)
2. Send the bot a DM. The bot will remember up to 10 messages of context (5 back-and-forth interactions).
3. When a conversation is finished, you can manually reset the message context backlog by reacting to the bot with a thumbs up.
This is highly recommended, because more messages in the context backlog means more tokens are sent in each request.

## Deployment
> **Note**
> Charles AI is still in development. The deployment documentation will improve as development progresses.

The Charles AI [Docker container](https://hub.docker.com/repository/docker/morpheus636/charles-ai/general) is the recommended and supported deployment method.

Deploy the container with the following environment variables:

#### Mandatory Environment Variables
```
OPENAI_API_KEY='your_openai_api_key_here'
DISCORD_BOT_TOKEN='your_discord_bot_secret_here'
ALLOWED_USER_ID='your_discord_user_id_here'
AI_USER_INFO'A system prompt for the AI explaining who you are. Keep this short as it counts towards your tokens on every single message.'
```
#### Optional Environment Variables
```
AI_NAME='your_ai_name_here'
UNITS='metric (default) or imperial'
```

## Contact
To submit a bug report or feature request, please open a GitHub Issue in this repository. 

To ask a question or get support, you can join my [Discord Server](https://discord.morpheus636.com) or create a Discussions thread within this repository.

This project is maintained my Morpheus636. Contribution guidelines for all of my projects can be found at https://docs.morpheus636.com/contributing

## Credits
- OpenAI

## Copyright Notice
© Copyright 2022 Josh Levin ([Morpheus636](https://github.com/morpheus636))

This repository (and everything in it) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This repository is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this repository.  If not, see <https://www.gnu.org/licenses/>.
