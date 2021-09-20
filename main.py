import discord
from discord.ext import commands
import random
import json
from time import time
from datetime import datetime

TOKEN = 'ODg1ODMzNTM2MTEwNzIzMTMz.YTsyxQ.ywXJKp7Cl4u4eZsACC58FxaifgE'

quotes = ["“Part of the journey is the end.”~ Tony Stark, Avengers: Endgame",
"“Tony, trying to get you to stop has been one of the few failures of my entire life.” \
~ Pepper Potts, Avengers: Endgame",
"“No amount of money ever bought a second of time.” ~ Tony Stark, Avengers: Endgame",
"“You know, I keep telling everybody they should move on and grow. Some do. But not us.” \
~ Steve Rogers, Avengers: Endgame",
"“It's not about how much we lost. It's about how much we have left.” \
~ Tony Stark, Avengers: Endgame",
"“No mistakes. No do-overs. Look out for each other. This is the fight of our lives.” \
~ Steve Rogers, Avengers: Endgame",
"“The hardest choices require the strongest wills.” \
~ Thanos, Avengers: Infinity War",
"“Today we don’t fight for one life, we fight for all of them.” \
~ Black Panther, Avengers: Infinity War",
"“It’s not enough to be against something. You have to be for something better.” \
~ Tony Stark, Captain America: Civil War",
"“I would rather be a good man than a great king.” \
~ Thor, Thor: The Dark World",
"“I choose to run towards my problems, and not away from them. \
Because that–because that's what heroes do.” \
~ Thor, Thor: Ragnarok",
"“But a thing isn’t beautiful because it lasts. It’s a privilege to be among them.” \
~ Vision, Avengers: Age of Ultron",
"“The world has changed and none of us can go back. \
All we can do is our best, and sometimes the best that we can do is to start over.” \
~ Peggy Carter, Captain America: The First Avenger",
"“Teach Me.” ~Stephen Strange, Doctor Strange",
"“Faith is my sword. Truth is my shield. Knowledge my armor.” \
~Stephen Strange, Doctor Strange",
"“I had my eyes opened. I came to realize that \
I had more to offer this world than just making things that blow up.” \
~ Tony Stark, Iron Man",
"“No man can win every battle, but no man should fall without a struggle.” \
~ Peter Parker, Spider-Man: Homecoming",
"“I am Iron Man.” ~ Tony Stark, Iron Man, Avengers: Endgame",
"“Hulk smash!” ~ Bruce Banner, The Incredible Hulk",
"“I don't know what you've got inside you already. The mix could be… an abomination.” \
~ Samuel Sterns, The Incredible Hulk",
"“Look, it’s me, I’m here, deal with it. Let’s move on.” \
~ James Rhodes, Iron Man 2",
"“How ironic, Tony. Trying to rid of the world of weapons, \
you gave it its best one ever! And now, I'm going to kill you with it!” \
~ Obadiah Stane, Iron Man 2",
"“If it were any smarter, it'd write a book – \
a book that would make Ulysses look like it was written in crayon.” \
~ Justin Hammer, Iron Man 2",
"“I don’t want to kill anyone. I don’t like bullies. I don’t care where they’re from.” \
~ Steve Rogers, Captain America: The First Avenger",
"“He will be the first in a new breed of super-soldiers. \
And they will personally escort Adolf Hitler to the gates of Hell.” \
~ Colonel Phillips, Captain America: The First Avenger",
"“I can do this all day.” ~ Steve Rogers, Captain America: The First Avenger",
"“That’s my secret, Captain. I’m always angry.” ~ Bruce Banner, Avengers",
"“We have a Hulk.” ~ Tony Stark, Avengers",
"“There’s no throne, there is no version of this, \
where you come out on top. Maybe your army comes and maybe \
it’s too much for us, but it’s all on you. Because if we \
can’t protect the Earth, you can be damned well sure we’ll avenge it.” \
~ Tony Stark, Avengers",
"“This is so unlike you, brother. So clandestine. \
Are you sure you wouldn’t rather just punch your way out?” \
~Loki, Thor: The Dark World"
"“You get hurt, hurt 'em back. You get killed… walk it off.” \
~ Captain America, Avengers: Age of Ultron"
"“You never know. You hope for the best and make do with what you get.” \
~ Nick Fury, Avengers: Age of Ultron"
"“He just kicked your ass, full-size. You really want to find out what it's \
like when you can't see him coming?” ~Howard Stark, Ant-Man"]
    
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('We have successfully logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = "Jarvis"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, newprefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = newprefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    await ctx.send(f"The prefix has been successfully changed to {newprefix}.")


@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=10):

    if amount <= 0:
        await ctx.send(f"I'm sorry, Sir, but it is not possible to delete {amount} messages.")
        return

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"**{amount}** messages were deleted by **{ctx.author}**.")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if "jarvis" in user_message.lower(): 
        if "what is your prefix" in user_message.lower() or "prefix?" in user_message.lower(): 
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
            
            current = prefixes[str(message.guild.id)]
            await message.channel.send(f"My prefix for this server is {current}, Sir.") 
    
        elif "what is the time" in user_message.lower() \
        or "time?" in user_message.lower() or "what time" in user_message.lower():
            nt = datetime.now()
            await message.channel.send(f"It's {nt.hour:02d}:{nt.minute:02d}, Sir.")

        elif "what is the date" in user_message.lower() \
        or "date?" in user_message.lower() or "what date" in user_message.lower():
            nd = datetime.now()
            await message.channel.send(f"Today is {nd.day}.{nd.month}.{nd.year}, Sir.")


    if message.channel.name == 'bot-spielplatz':
        if user_message.lower() == 'hello' or user_message.lower() == 'good day' \
        or user_message.lower() == 'good morning' or user_message.lower() == 'good afternoon' \
        or user_message.lower() == 'good day' or user_message.lower() == 'good evening':
            await message.channel.send(f'{user_message.capitalize()}, Sir.')
        
    await client.process_commands(message)


@client.command(aliases = ['Prefix'])
async def prefix(context):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
            
    current = prefixes[str(context.message.guild.id)]
    await context.send(f"My prefix for this server is {current}, Sir.") 

@client.command(aliases = ['Time'])
async def time(context):
    nt = datetime.now()
    await context.send(f"It's {nt.hour:02d}:{nt.minute:02d}, Sir.")

@client.command(aliases = ['Date'])
async def date(context):
    nd = datetime.now()
    await context.send(f"Today is {nd.day}.{nd.month}.{nd.year}, Sir.")

@client.command(aliases = ['Ping', 'Ping!', 'Ping?', 'ping!', 'ping?'])
async def ping(context):
    start = time()
    msg = await context.send(f"Pong! My latency is {round(client.latency * 1000)} ms, Sir.")
    end = time()
    await msg.edit(content = f"Pong! My latency is {round(client.latency * 1000)} ms, Sir." 
    f" My response time is {(end-start) * 1000:,.0f} ms.")

@client.command(aliases = ['random','Random', 'random?', 'Random?'])
async def _random(context, range = 100):
    await context.send(f"Here is your random number, Sir: {random.randrange(range)}")

@client.command()
async def quote(context, *args):
    sub = ' '.join(args)
    quotes1 = [i for i in quotes if sub in i]
    if not quotes1:
        await context.send("I couldn't find the quote you requested, Sir.")
    else:
        await context.send(random.choice(quotes1))

@client.command()
@commands.is_owner()
async def shutdown(context):
    await context.send("Shutting down.")
    await client.close()
    

client.run(TOKEN)