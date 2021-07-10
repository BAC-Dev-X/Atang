import discord
import random

TOKEN = ''

Client = discord.Client()

#logs the bot on
@Client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Client))

#client message responses to the specified server
@Client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str (message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == Client.user:
        return
    if message.channel.name == 'atangs-bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
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


Client.run(TOKEN)