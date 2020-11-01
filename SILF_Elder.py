# importing discord package
import discord
from discord import message

# client (this bot)
client = discord.Client()

#doing stuff
@client.event
async def on_ready():
    testBotChannel = client.get_channel(772103423721472040)
    await testBotChannel.send('Jedu bomby, můžeš mě používat')

@client.event
async def on_message(message):
    if message.content == 'heh':
        testBotChannel = client.get_channel(772103423721472040)
        await testBotChannel.send('nehehuj hajzle')

# run the client on the server
client.run('NzU4OTU5MTgwMTA2MTcwMzg5.X22h0Q.B1TNzWVc0zi0-Ps62ifXVZWlc-4')