import discord
from termcolor import colored, cprint
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    message_time = str(message.created_at)
    print(f'{username}: {user_message}')
    cprint('| ' + channel, 'blue')
    cprint('⏱️ ' + message_time, 'magenta')

    #Check for inf. loop
    if message.author == client.user:
        return
    
    #Check message contents
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')

    if user_message.lower() == ';server':
        guild = client.get_guild(1031720878733533285)
        await message.channel.send(f'Server ID is: "{guild.id}"\nThe Server name is: "{str(guild)}"')

client.run('MTA0MjU2MjA2MTg4MTgzOTc3Ng.GzNrhv.o2fHKqgV6nxcTdihqLu-B4r8bZtLD1LvziwZeo')