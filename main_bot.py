import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix="!",case_insensitive=True, intents=discord.Intents.all())
bot.remove_command('help')

cat_fact = ["Cats are believed to be the only mammals who don't taste sweetness.",
            "Cats are supposed to have 18 toes (five toes on each front paw; four toes on each back paw).",
            "Cats can jump up to six times their length.",
            "Cats have 230 bones, while humans only have 206.",
            "Cats have nearly twice the amount of neurons in their cerebral cortex as dogs.",
            "Cats walk like camels and giraffes : They move both of their right feet first, then move both of their left feet. No other animals walk this way.",
            "According to The Huffington Post, cats typically sleep for 12 to 16 hours a day.",
            "Despite popular belief, many cats are actually lactose intolerant.",
            "A cat with a question-mark-shaped tail is asking, “Want to play ?”.",
            "Cats find it threatening when you make direct eye contact with them.",
            "Cats mark you as their territory when they rub their faces and bodies against you, as they have scent glands in those areas.",
            "Meowing is a behavior that cats developed exclusively to communicate with people."]

dog_fact = ["A third of ALL households around the world have a dog.",
            "Dogs were the first animal domesticated (tamed) by humans, over 20,000 years ago.",
            "Dogs are thought to be as smart as two-year-old children, so many owners teach them commands and tricks.",
            "Dog noses are at least 40x more sensitive than ours.",
            "Many dogs are trained to work as guide dogs, helping blind people get around safely.",
            "From their ears to their eyebrows, shoulders, and tail, dogs often use signals and smells, rather than sound, to communicate.",
            "A dog's nose print is unique, much like a person's fingerprint.",
            "Dogs' noses can sense heat/thermal radiation, which explains why blind or deaf dogs can still hunt.",
            "A recent study shows that dogs are among a small group of animals who show voluntary unselfish kindness towards others without any reward.",
            "Some dogs are taller or heavier, but according to the Guinness World Records, a Mastiff named Zorba is the world's overall largest dog ever. Zorba weighed 343 pounds and measured over eight feet from his nose to his tail.",
            "All puppies are born deaf."]

parrot_fact = ["There are believed to be 18,000–20,000 or more bird species in the world! There are over a dozen families of birds that are kept as pets, and there are up to a few dozen species in each family.",
            "Birds are direct descendants of dinosaurs! Approximately 65 million years ago, all but one group of dinosaurs went extinct. The remaining group of dinosaurs became the birds we know and love today.",
            "The oldest known bird according to Guinness World Records was a Cockatoo named Cookie who lived to 82 years and 89 days. Cookie lived until August 27, 2016.",
            "Keep an eye on your bird’s eyes. Large, dilated pupils can indicate your bird is relaxed or content. However, small, pinprick pupils can indicate your bird is agitated and is likely to bite.",
            "Crested birds, like Cockatoos, will raise the crest on top of their head to show you they’re happy to see you.",
            "Birds are typically highly intelligent animals. They are also sensitive and experience a broad range of emotions, exhibiting the same mental, emotional, and problem-solving capacity of a human child around the age of 4 - 6 years."]

rabbit_fact = ["To express happiness, bunnies will sometimes jump around and flick their heads and feet.",
            "Like deer, a female rabbit is called a “doe” and a male rabbit is called a “buck”.",
            "Some, rabbits might seem like quiet pets, but they’re actually capable of making a lot of sounds, including growling, screeching, chattering their teeth, and even honking softly !",
            "Bunnies can be very affectionate and bond closely with their owners. Some will even come when called.",
            "Bunnies have an average lifespan of 5 to 10 years, but the oldest living rabbit broke the Guinness World Record at the ripe old age of 17.",
            "Rabbits are social creatures and most want other rabbits around for companionship so consider adopting a bonded pair! If you already have a rabbit but want to add another to your brood, talk to your vet or the shelter about the best way to introduce bunnies to each other.",
            "Because their eyes are positioned on the sides of their heads, bunnies can see an almost perfect 360 degrees."]

hamster_fact = ["“Hamster,” from the German word “hamstern,” means “hoard,” which is a favorite pastime of our hamster friends.",
            "Hamsters can be easily startled. Always approach your hamster from the side, use your voice and call their name to alert them that you are approaching.",
            "Hamsters naturally like to hide. Provide them with plenty of substrate for burrowing under in their habitat and a hollow hideaway where they can relax.",
            "Most hamsters are very fast runners, and the shape and size of their hind feet allows them to run backward as well.",
            "Hamsters are born blind, and even as adults can only see a few inches in front of their nose."]

turtle_fact = ["A tortoise is a turtle, but a turtle isn't a tortoise.",
            "A group of tortoises is called a creep, but you won't see a creep very often. Tortoises are solitary roamers.",
            "Tortoises have an exoskeleton AND an endoskeleton. The shell has three main parts: the top carapace, the bottom plastron, and the bridge that fuses these pieces together.",
            "The scales on the carapace are called scutes."]

goldfish_fact = ["Goldfish don’t have stomachs and should therefore be fed easily digestible food in lots of small feeding sessions, rather than lots of food at once.",
            "Goldfish can tell different faces apart and are able to distinguish between different shapes, colors and sounds.",
            "Many people say that goldfish have a memory of just a few seconds, but this is a myth! Goldfish have a memory span of at least three months!",
            "Goldfish have no eyelids, so they have to sleep with their eyes open!",
            "Keeping pet goldfish dates all the way back to ancient China (over 2000 years ago).",
            "Goldfish don’t like to be kept in the dark and, unlike humans, they are able to see ultra-violet and infra-red light."]

horse_fact = ["Horses have a nearly 360-degree field of vision, this is due to the positioning of their eyes on the sides of their head.",
            "Horses have a “stay-apparatus” which is a system of tendons and ligaments that allows the horse to lock their legs in position so they can relax without falling over.",
            "As a prey animal, horses need to react quickly should a flight-or-fight situation arise. When they need to fight, horses can go from standing still to delivering a powerful kick in just 0.3 seconds, whereas human reaction time is 1.6 seconds.",
            "Horses are highly intelligent animals",
            "They can be taught many different tasks through positive reinforcement and clicker training, just as dogs can.",
            "Horses find safety in a herd and form strong social relationships with each other. They use their senses to recognize familiar horses and spend time with those they have formed friendships with."]

guinea_pig_fact = ["They don’t come from Guinea. In fact, guinea pigs originate from the Andes region of South America. The ‘guinea’ in their name is a bit of a mystery.",
            "They don’t get on with rabbits. It’s a popular myth that you can happily keep guinea pigs and rabbits together. Not only will rabbits bully guinea pigs, they have very different needs.",
            "They like to chat to each other. While they enjoy human affection, guinea pigs need to be with others of their own kind and should always be kept in pairs or small groups.",
            "They only sleep for short periods. Although crepuscular creatures, who are most active during dusk and dawn, guinea pigs are awake for up to 20 hours of the day.",
            "They can break dance. Well, not quite, but when they are excited, guinea pigs can jump straight up and down, often turning 90° in mid-air, performing a slick little move known as ‘pop corning’.",
            "They have an odd number of toes. Guinea pigs have four toes on their front feet, but only three on their back ones."]

def isflaot(nb):
    try:
        float(nb)
        False
    except:
        return True


@bot.event
async def on_ready():
    print("InfoPet Bot is ready")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(content="The command you are trying to use does not exist at the moment.\nIf you think that this command should be implemented in our bot then make a suggestion using the !suggestion.\nTo see the commands usable by our bot do : !help.", delete_after=30.00)
        return
    f = open("./error.txt", "a")
    f.write(str(ctx.author))
    f.write(" : ")
    f.write(str(error))
    f.write("\n")
    await ctx.send(content="It seems that an unknown error has occurred. It has just been reported to the developers. You can also use the command: !suggestion to tell us in which case you have encountered this error so that it can be resolved as soon as possible.\nWe thank you for your patience and hope that this will not impact your use of our bot.\nSincerely the N-Queen Team.", delete_after=30.00)
    return


@bot.command('suggestion')
async def help(ctx, *, message = "None"):
    '''Make a suggestion'''
    if message == "None":
        embed = discord.Embed(title="**SUGGESTION**", description="The suggestion function allows you to communicate with us and send us an idea, a comment on what we should review/add to our bot.\n \n**How to use our suggestion feature :**", color=0x149431)
        embed.set_thumbnail(url=os.getenv("IMG_SUGGESTION"))
        embed.add_field(name="COMMAND", value="!suggestion", inline=True)
        embed.add_field(name="MESSAGE", value="Write the suggestion you want to make.", inline=True)
        embed.set_footer(text="Thank you for participating in the development of our bot.")
        await ctx.send(embed=embed)
        return
    f = open("./suggestion.txt", "a")
    f.write(str(ctx.author))
    f.write(" : ")
    f.write(message)
    f.write("\n")
    await ctx.send(content="**Your suggestion has been sent. From InfoPet bot and its developers, we thank you.**")



@bot.command('help')
async def help(ctx, *, message = "None"):
    '''Envoie la liste des commandes et leurs fonctions'''
    if message == "None":
        embed = discord.Embed(title="**LIST OF COMMANDS :**", colour=discord.Colour.blue())
        embed.set_thumbnail(url=os.getenv("IMG_HELP"))
        embed.add_field(name="**!help**", value="Gives you more information about the robot's features.", inline=False)
        embed.add_field(name="**!info**", value="Displays information sheets on pets.", inline=False)
        embed.add_field(name="**!food**", value="To calculate the amount of food needed for your pet.", inline=False)
        embed.add_field(name="**!suggestion**", value="To Send us your suggestion.", inline=False)
        embed.set_footer(text="If you want more information about a particular order please use:\n !help (command name)")
        await ctx.send(embed=embed)
        return
    if message.lower() == "food":
        embed = discord.Embed(title="**FOOD CALCULATOR**", description="The food calculator function will calculate the amount of kibble/ration to be given to your pet according to the pet concerned and its weight.\n \n**How to use our food calculator :**", color=0x149431)
        embed.set_thumbnail(url=os.getenv("IMG_CALCULATOR"))
        embed.add_field(name="COMMAND", value="!food", inline=True)
        embed.add_field(name="PET NAME", value="Name of the pet", inline=True)
        embed.add_field(name="WEIGHT", value="Weight of the pet in kilograms", inline=True)
        embed.set_footer(text="PET SUPPORTED : Cat, Dog, Parrot, Hamster.\nMore pets will be added in the future.")
        await ctx.send(embed=embed)
        return
    if message.lower() == "info":
        embed = discord.Embed(title="**INFORMATION SHEET**", description="The info function will display the information sheet of the selected pet.\n \n**How to use our info feature :**", color=0x149431)
        embed.set_thumbnail(url=os.getenv("IMG_INFO"))
        embed.add_field(name="COMMAND", value="!info", inline=True)
        embed.add_field(name="PET NAME", value="Name of the pet (If the name of the pet is not specified then, the bot will send a selection menu)", inline=True)
        embed.set_footer(text="PET SUPPORTED : Cat, Dog, Parrot, Rabbit, Hamster, Turtle, Glodfish, Horse, Guinea Pig.\nMore pets will be added in the future.")
        await ctx.send(embed=embed)
        return
    if message.lower() == "suggestion":
        embed = discord.Embed(title="**SUGGESTION**", description="The suggestion function allows you to communicate with us and send us an idea, a comment on what we should review/add to our bot.\n \n**How to use our suggestion feature :**", color=0x149431)
        embed.set_thumbnail(url=os.getenv("IMG_SUGGESTION"))
        embed.add_field(name="COMMAND", value="!suggestion", inline=True)
        embed.add_field(name="MESSAGE", value="Write the suggestion you want to make.", inline=True)
        embed.set_footer(text="Thank you for participating in the development of our bot.")
        await ctx.send(embed=embed)
        return
    await ctx.send(content=f"The **{message}** command does not exist at the moment.\nIf you think that this command should be implemented in our bot then make a suggestion using the !suggestion.\nTo see the commands usable by our bot do : !help.", delete_after=30.00)


@bot.command(name='food')
async def delete(ctx, *, infos = "None"):
    '''Food Calculator'''
    if (infos == "None" or infos == "help"):
        embed = discord.Embed(title="**FOOD CALCULATOR**", description="The food calculator function will calculate the amount of kibble/ration to be given to your pet according to the pet concerned and its weight.\n \n**How to use our food calculator :**", color=0x149431)
        embed.set_thumbnail(url=os.getenv("IMG_CALCULATOR"))
        embed.add_field(name="COMMAND", value="!food", inline=True)
        embed.add_field(name="PET NAME", value="Name of the pet", inline=True)
        embed.add_field(name="WEIGHT", value="Weight of the pet in kilograms", inline=True)
        embed.set_footer(text="PET SUPPORTED : Cat, Dog, Parrot, Hamster.\nMore pets will be added in the future.")
        await ctx.send(embed=embed)
        return
    infos = infos.split()
    if (len(infos) == 1 or len(infos) > 3):
        await ctx.send(content="Wrong number of arguments, please consult the **!food help** command.", delete_after=30.00)
        return
    if (len(infos) == 2):
        if infos[0].lower() == "cat":
            if isflaot(infos[1]):
                await ctx.send(content="Invalid weight, please consult the **!food help** command.", delete_after=30.00)
                return
            weight = float(infos[1])
            if weight < 2.00:
                await ctx.send(content="```The weight indicated is too low. It may be that it corresponds to that of a kitten. However, our food calculator does not yet calculate the food needed for a non-adult cat. This feature will be added in the future.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if weight > 11.00:
                await ctx.send(content="```The weight indicated is too high. Your cat may be overweight. In this case, we advise you to visit your veterinarian to find a suitable feeding solution for your pet.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if (weight >= 2.00 and weight <= 11.00):
                amount = [str(round(weight * 12)), str(round(weight * 14.5))]
                await ctx.send(content=f"**According to our calculations, a {infos[0]} of {infos[1]} kilograms would need about {amount[0]} to {amount[1]} grams of food per day.**\n*The perfect amount of food for your cat cannot be found only with the help of our calculator, we advise you to judge yourself or with the help of a professional the amount of food to give to your cat according to: its race, its physical activity, its age, etc...*")
            return
        if infos[0].lower() == "dog":
            if isflaot(infos[1]):
                await ctx.send(content="Invalid weight, please consult the **!food help** command.", delete_after=30.00)
                return
            weight = float(infos[1])
            if weight < 2.00:
                await ctx.send(content="```The weight indicated is too low. It may be that it corresponds to that of a puppy. However, our food calculator does not yet calculate the food needed for a non-adult dog. This feature will be added in the future.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if weight > 100.00:
                await ctx.send(content="```The weight indicated is too high. Your dog may be overweight. In this case, we advise you to visit your veterinarian to find a suitable feeding solution for your pet.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if (weight >= 2.00 and weight <= 100.00):
                amount = [str(round(weight * 13.5)), str(round(weight * 16.5))]
                await ctx.send(content=f"**According to our calculations, a {infos[0]} of {infos[1]} kilograms would need about {amount[0]} to {amount[1]} grams of food per day.**\n*The perfect amount of food for your dog cannot be found only with the help of our calculator, we advise you to judge yourself or with the help of a professional the amount of food to give to your pet according to: its race, its physical activity, its age, etc...*")
            return
        if infos[0].lower() == "parrot":
            if isflaot(infos[1]):
                await ctx.send(content="Invalid weight, please consult the **!food help** command.", delete_after=30.00)
                return
            weight = float(infos[1])
            if weight < 0.10:
                await ctx.send(content="```The weight indicated is too low. It may be that it corresponds to that of a baby parrot. However, our food calculator does not yet calculate the food needed for a non-adult parrot. This feature will be added in the future.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if weight > 4.00:
                await ctx.send(content="```The weight indicated is too high. Your parrot may be overweight. In this case, we advise you to visit your veterinarian to find a suitable feeding solution for your pet.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            if (weight >= 0.10 and weight <= 4.00):
                amount = [str(round(weight * 100)), str(round(weight * 200))]
                await ctx.send(content=f"**According to our calculations, a {infos[0]} of {infos[1]} kilograms would need about {amount[0]} to {amount[1]} grams of food per day.**\n*The perfect amount of food for your dog cannot be found only with the help of our calculator, we advise you to judge yourself or with the help of a professional the amount of food to give to your pet according to: its race, its physical activity, its age, etc...*")
            return
        if infos[0].lower() == "hamster":
            if isflaot(infos[1]):
                await ctx.send(content="Invalid weight, please consult the **!food help** command.", delete_after=30.00)
                return
            weight = float(infos[1])
            if (weight > 0.025 and weight < 0.500):
                await ctx.send(content=f"**According to our calculations, a {infos[0]} of {infos[1]} kilograms would need about 10 to 15 grams of food per day.**\n*The perfect amount of food for your hamster cannot be found only with the help of our calculator, we advise you to judge yourself or with the help of a professional the amount of food to give to your pet according to: its race, its physical activity, its age, etc...*")
                return
            await ctx.send(content="```The weight seems incorrect.\nIf you have any problems, please let us know by using the !suggestion.\nThanks to you```")
            return
    await ctx.send(content=f"```It seems that the pet {infos[0]} is not supported by our food calculator. To know the list of supported pets please refer to the !help food command.\nIf you want {infos[0]} to be added to our calculator, don't hesitate to make a suggestion with the !suggestion command.\nThanks to you```")
    return



async def info_cat(ctx):
    embed = discord.Embed(title="**CAT** (*Felis catus*) :", url=os.getenv("LINK_CAT"), color=0xffc107)
    embed.set_thumbnail(url=os.getenv("IMG_CAT"))
    embed.set_footer(text=random.choice(cat_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_CAT"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD2_CAT"), inline=False)
    embed.add_field(name="HANDLING :", value=os.getenv("FIELD3_CAT"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD4_CAT"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD5_CAT"), inline=False)
    embed.add_field(name="SCRATCHING :", value=os.getenv("FIELD6_CAT"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD7_CAT"), inline=False)
    await ctx.send(embed=embed)

async def info_dog(ctx):
    embed = discord.Embed(title="**DOG** (*Canis familiaris*) :", url=os.getenv("LINK_DOG"), color=0x752a25)
    embed.set_thumbnail(url=os.getenv("IMG_DOG"))
    embed.set_footer(text=random.choice(dog_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_DOG"), inline=False)
    embed.add_field(name="EXERCISE :", value=os.getenv("FIELD2_DOG"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD3_DOG"), inline=False)
    embed.add_field(name="HANDLING :", value=os.getenv("FIELD4_DOG"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD5_DOG"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD6_DOG"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD7_DOG"), inline=False)
    await ctx.send(embed=embed)

async def info_parrot(ctx):
    embed = discord.Embed(title="**PARROT** (*Psittacines*) :", url=os.getenv("LINK_PARROT"), color=0xb098ff)
    embed.set_thumbnail(url=os.getenv("IMG_PARROT"))
    embed.set_footer(text=random.choice(parrot_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_PARROT"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD2_PARROT"), inline=False)
    embed.add_field(name="EXERCISE AND PLAY :", value=os.getenv("FIELD3_PARROT"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD4_PARROT"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD5_PARROT"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD6_PARROT"), inline=False)
    await ctx.send(embed=embed)

async def info_rabbit(ctx):
    embed = discord.Embed(title="**RABBIT** (*Leporidae*) :", url=os.getenv("LINK_RABBIT"), color=0xb82f04)
    embed.set_thumbnail(url=os.getenv("IMG_RABBIT"))
    embed.set_footer(text=random.choice(rabbit_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_RABBIT"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD2_RABBIT"), inline=False)
    embed.add_field(name="HANDLING :", value=os.getenv("FIELD3_RABBIT"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD4_RABBIT"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD5_RABBIT"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD6_RABBIT"), inline=False)
    await ctx.send(embed=embed)

async def info_hamster(ctx):
    embed = discord.Embed(title="**HAMSTER** (*Cricetinae*) :", url=os.getenv("LINK_HAMSTER"), color=0xb4a131)
    embed.set_thumbnail(url=os.getenv("IMG_HAMSTER"))
    embed.set_footer(text=random.choice(hamster_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_HAMSTER"), inline=False)
    embed.add_field(name="HANDLING :", value=os.getenv("FIELD2_HAMSTER"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD3_HAMSTER"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD4_HAMSTER"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD5_HAMSTER"), inline=False)
    await ctx.send(embed=embed)

async def info_turtle(ctx):
    embed = discord.Embed(title="**TURTLE** (*Testudines*) :", url=os.getenv("LINK_TURTLE"), color=0xb601c4)
    embed.set_thumbnail(url=os.getenv("IMG_TURTLE"))
    embed.set_footer(text=random.choice(turtle_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_TURTLE"), inline=False)
    embed.add_field(name="TEMPERATURE :", value=os.getenv("FIELD2_TURTLE"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD3_TURTLE"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD4_TURTLE"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD5_TURTLE"), inline=False)
    await ctx.send(embed=embed)

async def info_goldfish(ctx):
    embed = discord.Embed(title="**GOLDFISH** (*Carassius auratus*) :", url=os.getenv("LINK_GOLDFISH"), color=0x5356bb)
    embed.set_thumbnail(url=os.getenv("IMG_GOLDFISH"))
    embed.set_footer(text=random.choice(goldfish_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_GOLDFISH"), inline=False)
    embed.add_field(name="TANK TEMPERATURE :", value=os.getenv("FIELD2_GOLDFISH"), inline=False)
    embed.add_field(name="WATER :", value=os.getenv("FIELD3_GOLDFISH"), inline=False)
    embed.add_field(name="TANK SIZE :", value=os.getenv("FIELD4_GOLDFISH"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD5_GOLDFISH"), inline=False)
    await ctx.send(embed=embed)

async def info_horse(ctx):
    embed = discord.Embed(title="**Horse** (*Equus ferus caballus*) :", url=os.getenv("LINK_HORSE"), color=0x704640)
    embed.set_thumbnail(url=os.getenv("IMG_HORSE"))
    embed.set_footer(text=random.choice(horse_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_HORSE"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD2_HORSE"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD3_HORSE"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD4_HORSE"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD5_HORSE"), inline=False)
    await ctx.send(embed=embed)

async def info_guinea_pig(ctx):
    embed = discord.Embed(title="**GUINEA PIG** (*Cavia porcellus*) :", url=os.getenv("LINK_GUINEA_PIG"), color=0x8b7964)
    embed.set_thumbnail(url=os.getenv("IMG_GUINEA_PIG"))
    embed.set_footer(text=random.choice(guinea_pig_fact))
    embed.add_field(name="FOOD :", value=os.getenv("FIELD1_GUINEA_PIG"), inline=False)
    embed.add_field(name="GROOMING :", value=os.getenv("FIELD2_GUINEA_PIG"), inline=False)
    embed.add_field(name="HOUSING :", value=os.getenv("FIELD3_GUINEA_PIG"), inline=False)
    embed.add_field(name="HEALTH :", value=os.getenv("FIELD4_GUINEA_PIG"), inline=False)
    embed.add_field(name="AVERAGE LIFESPAN :", value=os.getenv("FIELD5_GUINEA_PIG"), inline=False)
    await ctx.send(embed=embed)


## Select Menu for info command ##

class SelectMenu(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label="Cat", description="View the cat's information sheet.", emoji="🐱"),
                discord.SelectOption(label="Dog", description="View the dog's information sheet.", emoji="🐶"),
                discord.SelectOption(label="Parrot", description="View the parrot's information sheet.", emoji="🦜"),
                discord.SelectOption(label="Rabbit", description="View the rabbit's information sheet.", emoji="🐰"),
                discord.SelectOption(label="Hamster", description="View the hamster's information sheet.", emoji="🐹"),
                discord.SelectOption(label="Turtle", description="View the turtle's information sheet.", emoji="🐢"),
                discord.SelectOption(label="Goldfish", description="View the goldfish's information sheet.", emoji="🐟"),
                discord.SelectOption(label="Horse", description="View the horse's information sheet.", emoji="🐴"),
                discord.SelectOption(label="Guinea pig", description="View the guinea pig's information sheet.", emoji="🐹"),
                discord.SelectOption(label="Quit", description="Quit the selection", emoji="❌")]
        super().__init__(placeholder="Of which pet do you want the information sheet ?", options=options)

    async def callback(self, interaction: discord.Interaction):
        mgs = []
        async for each in interaction.channel.history(limit=1):
            mgs.append(each)
        for message in mgs:
            await message.delete()
        if (self.values[0] == "Cat"):
            await info_cat(interaction.channel)
        if (self.values[0] == "Dog"):
            await info_dog(interaction.channel)
        if (self.values[0] == "Parrot"):
            await info_parrot(interaction.channel)
        if (self.values[0] == "Rabbit"):
            await info_rabbit(interaction.channel)
        if (self.values[0] == "Hamster"):
            await info_hamster(interaction.channel)
        if (self.values[0] == "Turtle"):
            await info_turtle(interaction.channel)
        if (self.values[0] == "Goldfish"):
            await info_goldfish(interaction.channel)
        if (self.values[0] == "Horse"):
            await info_horse(interaction.channel)
        if (self.values[0] == "Guinea pig"):
            await info_guinea_pig(interaction.channel)
        if (self.values[0] == "Quit"):
            await interaction.channel.send(content="You have successfully exited the info menu.")
        Select.stop

class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())

@bot.command(name='info')
async def info(ctx, *, name = "None"):
    if name == "None":
        await ctx.send(content="Select the pet :", view=Select(), delete_after=25.00)
        return
    name = name.lower()
    if name == "cat":
        await info_cat(ctx)
        return
    if name == "dog":
        await info_dog(ctx)
        return
    if name == "parrot":
        await info_parrot(ctx)
        return
    if name == "rabbit":
        await info_rabbit(ctx)
        return
    if name == "hamster":
        await info_hamster(ctx)
        return
    if name == "turtle":
        await info_turtle(ctx)
        return
    if name == "goldfish":
        await info_goldfish(ctx)
        return
    if name == "horse":
        await info_horse(ctx)
        return
    if name == "guinea pig":
        await info_guinea_pig(ctx)
        return
    await ctx.send(content=f"```It seems that the pet : {name} does not have an information sheet. To know the list of supported pets please refer to the !help info command.\nIf you want {name} to be added to the list of information sheets, don't hesitate to make a suggestion using the !suggestion command.\nThanks to you```")
    





bot.run(os.getenv("TOKEN"))