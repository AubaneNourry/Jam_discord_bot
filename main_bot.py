import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Le bot est prêt")

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    mgs = []
    async for each in ctx.channel.history(limit=number_of_messages + 1):
        mgs.append(each)
    for message in mgs:
        await message.delete()

bot.run("MTA1NDc0NzQ4NzgzNzEwNjMyNw.GShHfE.nOPrBiL4Opw42mITtSSvioinh-RLfqlCOjwHoY")