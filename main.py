import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Le bot est prêt")

@client.event
async def on_message(message):
    if (message.content.lower() == "quoi"):
        await message.channel.send("feur", delete_after = 5)
    if (message.content.lower()== "méchant"):
        await message.delete()
    if (message.content.lower()== "axel"):
        await message.channel.send("ratio", delete_after = 5)
    if (message.content.startswith("!del")):
        mgs = []
        number = int(message.content.split()[1])
        async for each in message.channel.history(limit=number + 1):
            mgs.append(each)
        for message in mgs:
            await message.delete()

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(1054748398550528053)
    await general_channel.send(content=f"Bienvenue sur le serveur {member} !")

client.run("MTA1NDc0NzQ4NzgzNzEwNjMyNw.GShHfE.nOPrBiL4Opw42mITtSSvioinh-RLfqlCOjwHoY")