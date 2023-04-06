import logging
import os

import discord

from . import ai_engine


logger = logging.getLogger(__name__)


# Setup discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Event handler for bot coming online. DMs the allowed user that it is ready."""
    logger.info("Discord Interface Ready")
    user = await client.fetch_user(os.getenv("ALLOWED_USER_ID"))
    await user.send("Systems are now fully operational.")


@client.event
async def on_message(message):
    """Event handler for DMs to the bot."""
    # Don't have the bot reply to itself.
    if message.author == client.user:
        return

    # Ensure the bot only replies to authorized users.
    if not message.author.id == int(os.getenv("ALLOWED_USER_ID")):
        await message.reply(
            "I am unable to assist you. If this is a mistake, you need to add your user ID in the `ALLOWED_USER_ID` environment variable on my server."
        )
        return

    # Only reply to DMs
    if isinstance(message.channel, discord.DMChannel):
        logger.debug(
            f"Received message: {message.content} from user: {message.author.id} in channel {message.channel.id}"
        )

        # No prefix means it's not a command.
        if not message.content.startswith("?"):
            await message.reply(ai_engine.ask(message.content))

        # Clear command
        elif message.content.startswith("?clear"):
            args = message.content.split(" ")
            if len(args) == 1:
                limit = 200
            else:
                limit = int(args[1])
            async for msg in message.channel.history(limit=limit):
                if msg.author == client.user:
                    await msg.delete()


@client.event
async def on_reaction_add(reaction, user):
    """Event handler for reactions to the bot."""
    # Ensure only authorized users can clear history.
    if not user.id == int(os.getenv("ALLOWED_USER_ID")):
        return

    # Clear conversation log if the user reacts to a DM from the bot with :thumbsup:
    if (
        isinstance(reaction.message.channel, discord.DMChannel)
        and reaction.message.author != client.user
    ):
        if reaction.emoji.name == "👍":
            logger.debug("Received thumbsup reaction. Clearing queue.")
            ai_engine.conversation = []


def start():
    """Blocking: Start the bot's async event loop."""
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
