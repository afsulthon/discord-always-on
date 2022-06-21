import os
import discord
from keep_alive import keep_running

keep_running()

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('Ready!')

client.run(os.getenv('DISCORD_TOKEN'), bot=False)
