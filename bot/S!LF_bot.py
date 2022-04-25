# importing discord package
from asyncio.tasks import wait
import urllib.request, json 
import datetime
import asyncio
import random
import json
import discord
import music
from reddit import get_posts
from discord.flags import Intents
from discord import message
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands import converter
from discord.ext.commands.core import command

cogs = [music]

# client (this client)
client = commands.Bot(command_prefix='-', Intents = discord.Intents.all(), help_command=None)

for i in range(len(cogs)):
    cogs[i].setup(client)



# defining time for giveaways
def convert(time):
    pos = ["s", "m", "h", "d"]
    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2
    
    return val * time_dict[unit]

# Actual commands 

@client.command()
async def ping(ctx) :
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ')

@client.command(name='help')
async def help(context):

    myHelpEmbed = discord.Embed(title="Příkazy", description='Defaultní prefix je: -', color=0x424242)
    myHelpEmbed.add_field(name="help", value="Zobrazí příkazy", inline=False)
    myHelpEmbed.add_field(name="ping", value="Zobrazí tvoji odezvu", inline=False)
    myHelpEmbed.add_field(name="cat", value="Najde náhodný obrázek kočky", inline=False)
    myHelpEmbed.add_field(name="cute", value="Najde náhodný roztomilý obrázek", inline=False)
    myHelpEmbed.add_field(name="meme", value="Najde náhodný meme", inline=False)
    myHelpEmbed.add_field(name="teplota", value="Zobrazí teplotu a vlhkost v Kubově pokoji :)", inline=False)
    myHelpEmbed.add_field(name="ga", value="Začne vytváření giveawaye", inline=False)
    myHelpEmbed.add_field(name="join", value="Připojí se hlasového kanálu, kde právě jsi", inline=False)
    myHelpEmbed.add_field(name="play [url]", value="Začne pouštět hudbu z YT", inline=False)
    myHelpEmbed.add_field(name="pause", value="Pozastaví hranou hudbu", inline=False)
    myHelpEmbed.add_field(name="resume", value="Bude pokračovat v přehrávání hudby", inline=False)
    myHelpEmbed.add_field(name="leave", value="Odejte z hlasového kanálu", inline=False)
    myHelpEmbed.set_footer(text= "Commands in embed :)")

    await context.message.channel.send(embed=myHelpEmbed)

@client.command()
async def cat(ctx) :
    await ctx.send(get_posts('cats'))

@client.command()
async def meme(ctx) :
    await ctx.send(get_posts('memes'))

@client.command()
async def cute(ctx) :
    await ctx.send(get_posts('cute'))


@client.command(name='teplota')
async def teplota(context):

    url = '109.183.224.100:2222/api'
    try:
        req = urllib.request.Request("http://" + url)
        req = urllib.request.urlopen(req, timeout=3)
        with urllib.request.urlopen("http://109.183.224.100:2222/api") as url:      #Deklarace URL adresy
            data = json.loads(url.read().decode())                                    #Dekodovani JSONu
            tmp = data['temperature']
            humi = int(round(data['humidity'], 0))
            await context.message.channel.send("V Jakubovo pokoji je právě {} °C a {} % vlhkosti.".format(tmp, humi))

    except:
        await context.message.channel.send("Nastala nějaká chyba, server je nejspíš nedostupný :pensive:")

    
# Giveaway function 
@client.command()
@commands.has_any_role("Admin", "Moderator")
async def ga(ctx):
    await ctx.send("Jdeme sestavit tenhle rigged giveaway :)")
    
    questions = ["Teď napiš třeba #giveaways nebo jakýkoliv kanál s '#'",
                "Jak dlouho to má trvat? Napiš to jako číslo + s / m / h / d",
                "Co bude výhrou?"]
    
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Jsi nesthil odepsat :/")
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"Jsi to špatně napsal")
        return
    
    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"ERROR: Špatně jsi napsal jednotku. Piš hned za číslo: s / m / h / d")
        return
    elif time == -2:
        await ctx.send(f"ERROR: Musí to být číslo 😡")
        return
    prize = answers[2]

    await ctx.send(f"Giveaway bude v kanále {channel.mention} a bude trvat {answers[1]}")

    embed = discord.Embed(title= "Giveaway!", description= f"Hlasuj pomocí 🎉 o: {prize}", color= 0x9e200d)
    embed.add_field(name= "Vytvořil/a:", value= ctx.author.mention)
    embed.set_footer(text= f"Končí za {answers[1]}")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction('🎉')

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Hezky pěkně! {winner.mention} vyhrál: {prize}!")
    





# run the client on the server
client.run('NzU4OTU5MTgwMTA2MTcwMzg5.X22h0Q.B1TNzWVc0zi0-Ps62ifXVZWlc-4')