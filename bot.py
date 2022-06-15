from datetime import timedelta
import discord
from discord.ext import commands
from logger import *
from pytimeparse import parse
from time import sleep
from env import get_env

ENV_FPATH = "./.env"
COMMAND = "remindme"

def get_prefix(fpath):
    return get_env(fpath)

def has_prefix(string, prefix):
    try:
        for i in range(len(prefix)): 
            if string[i] != prefix[i]:
                return False
    except IndexError as e:
        logging.error(e)
        return False
    return True

def sleep_t(t_delta):
    num_secs = t_delta.days * 86400 + t_delta.seconds + t_delta.microseconds / 1000000.0
    num_secs = int(num_secs // 1)  # Set up num_secs so it is accepted by range()
    num_secs_elapsed = 0
    for i in range(num_secs):
        logging.info(f"{num_secs_elapsed}/{num_secs} seconds elapsed.")
        sleep(1)
        num_secs_elapsed += 1

config = get_env(ENV_FPATH)
_input = "1.2 minutes"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
            
@client.event
async def on_message(message):
    if message.channel.id != 986466659093053510:
        return
    if message.author == client.user: # Ignore messages from the bot itself
        return
    if message.content.startswith(config["PREFIX"] + COMMAND):
        args = message.content.split()
        sleep_amt = timedelta(seconds=parse(args[1]))
        msg_txt = " ".join(args[2:])
        await message.reply(f"Reminding {message.author} in {sleep_amt}", mention_author=False)
        sleep_t(sleep_amt)
        await message.reply(f"<@{message.author.id}>: {msg_txt}", mention_author=False)

client.run(config["TOKEN"])

client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"prefix: {config['PREFIX']}"))
        