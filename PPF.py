import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncioa

Client = discord.Client()
client = commands.Bot(command_prefix = "?")
@client.event
async def on_message(message):
    if message.content.upper().startswith('?FEEDBACK'):
        server = client.get_server("363386694868664320")
        args = message.content.split(" ")
        await client.send_message(server.get_channel("444915979512971264"), "%s" % (" ".join(args[1:])))
        await client.send_message(message.author, "Thank you for your feedback! It's really appreciated.")

client.run("NDQ0OTE1NDQ3MzQzNzQyOTg2.Ddi5ew.gbnbMv1MPmva4bfVIajJoIWo2uQ")
