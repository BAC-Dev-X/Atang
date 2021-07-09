import discord
import random

TOKEN = 'ODYyOTg2NDg0MzE4NDcwMTY0.YOgUyw.e6YBq16ZP7gMvmWAuMf4k-D881k'

client = discord.client()

#logs the bot on
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#client message responses to the specified server
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str (message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == '':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello{username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == "!random":
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await user_message.channel.send('This can be used anywhere!')
        return 


client.run(TOKEN)
