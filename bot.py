
# coding: utf-8

# In[2]:


import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NDgzNjU5OTcxNjIwNTAzNTU2.DrlS6Q.DWYZTZF8Gw_T5CgVElzKy8l1GME')

