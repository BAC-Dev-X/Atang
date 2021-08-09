import  discord
import random
from  discord.ext import commands

TOKEN = ''
Client = commands.Bot(command_prefix= '.')
#Client = discord.Client()

@Client.event
async def on_ready():
    print('Bot is ready as {0.user}'.format(Client))

@Client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@Client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@Client.command()
async def ping(ctx):
    await ctx.send(f'Reply!   {round(Client.latency * 1000)}ms')

@Client.command(aliases=['8ball', 'test'])
async  def _8ball(cxt, *, question):
   responses =['It is certain',
               'Without doubt',
               'Most likely',
               'yes',
               'Ask again later',
               'Cannot predict now',
               'My reply is no']
   await cxt.send(f'Question:{question}\nAnswer: {random.choice(responses)}')


Client.run(TOKEN)