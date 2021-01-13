import discord, os, keep_alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(

  command_prefix='&',

  self_bot=True

)

@client.event

async def on_connect():

  await client.change_presence(activity = discord.Streaming(name = "Ton text ici", url = "https://www.twitch.tv/X"))// Exemple de text : CryptoUser1337 -r00t

keep_alive.keep_alive()

client.run(os.getenv("Ton token discord"), bot=False)
