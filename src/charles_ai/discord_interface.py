import os

import discord

from . import ai_engine


# Setup discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Event handler for bot coming online. DMs the allowed user that it is ready."""
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

    if isinstance(message.channel, discord.DMChannel):
        # Non-command: AI conversation
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
    if not user.id == int(os.getenv("ALLOWED_USER_ID")):
        return
 
    if isinstance(reaction.message.channel, discord.DMChannel):
        if reaction.message.author != client.user:
            # Clear the conversation history if the user reacts with :thumbsup:
            if reaction.emoji.name == "👍":
                ai_engine.conversation = []


def start():
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
