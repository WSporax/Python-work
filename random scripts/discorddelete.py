import discord

client = discord.Client()

@client.event
async_def on_message(message):
    if message.channel == "general":
        await message.channel.purge(limit = 1)

