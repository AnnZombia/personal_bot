import time
import os
import discord
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

andrew = None

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    for guild in client.guilds:
       for member in guild.members:
          name = member.name
          if name == 'XXX':
             status = member.raw_status
             print(status)
             await client.close() 
client.run(token)
