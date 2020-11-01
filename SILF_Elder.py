# importing discord package
import discord
from discord import message
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context

# client (this bot)
client = commands.Bot(command_prefix='-', help_command=None)

#doing stuff

@client.command(name='help')
async def help(context):

    myEmbed = discord.Embed(title="Commands", description='Default prefix is -', color=0x424242)
    myEmbed.add_field(name="help", value="shows commands", inline=False)
    myEmbed.set_footer(text= "Commands in embed :)")
    myEmbed.set_author(name="S!LF Elder")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    testBotChannel = client.get_channel(772103423721472040)
    await testBotChannel.send('Jedu bomby, můžeš mě používat')

@client.event
async def on_message(message):
    if message.content == 'old':
        testBotChannel = client.get_channel(772103423721472040)

        myEmbed = discord.Embed(title="Title", description="description", color=0x424242)
        myEmbed.add_field(name="name", value="value", inline=False)
        myEmbed.set_footer(text= "text in footer")
        myEmbed.set_author(name="name -author")

        await testBotChannel.send(embed=myEmbed)
    await client.process_commands(message)



# run the client on the server
client.run('NzU4OTU5MTgwMTA2MTcwMzg5.X22h0Q.B1TNzWVc0zi0-Ps62ifXVZWlc-4')