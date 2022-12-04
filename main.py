import os
import discord
from discord.ext import commands
from art import *

client = commands.Bot(command_prefix="$", case_insensitive=True,intents=discord.Intents(messages=True, members=True, message_content=True, guilds=True))

@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))
  print(text2art("ready", "small"))

@client.command()
async def ping(ctx):
  await ctx.reply(f"{round({client.latency}*1000, 2)}")

@client.command()
async def askui(ctx):
  m = discord.Embed(title="RULES AND REGULATIONS", color=discord.Color.purple(), description=f"Please note that these rules are subject to change")
  
  m.add_field(name="1 - Be respectful to other members of the server.", value="Every members are equal here - be RESPECTFUL. Any attacks\, racism\, sexism\, homophobic remarks\, political extremism or bigotry\, and etc. towards other members will not be tolerated.\n_ _", inline=False) 
  
  m.add_field(name="2 - Not Safe For Work (NSFW) Content is Forbidden.", value="No pornographic/highly suggestive material, graphic violence, illegal activity, and/or other NSFW content via a link, image, text, or emote in all channel.\n_ _", inline=False) 
  
  m.add_field(name="3 - Please try to text/speak in ENGLISH only.", value="Please try to speak/type in English in all chats. We understand that most members are multilingual, but we want to make sure everyone can join conversations.\n_ _", inline=False)
  
  m.add_field(name="4 - No spamming.", value="Spamming is not allowed.\n_ _", inline=False)

  m.add_field(name="5 - For your own protection and privacy we respectfully ask that you do not share any personal pictures or videos of yourself or other private individuals within the askui server.", value="_ _", inline=False)
  m.add_field(name="6 - If you see something against the rules or something that makes you feel unsafe, let the admins know. We want this server to be a welcoming and safe space!", value="_ _", inline=False)
  m.set_footer(text="If you at any point feel like you have been sanctioned unfairly, you may contact the moderation/management team via direct message for help", icon_url=None)
  
  await ctx.reply(embed=m)
  
client.run(os.environ["TOKEN"])