import discord
from bot111 import token
import random
import discord.ext.tasks
import discord.ext.commands
# Create a bot instance with intents
intents = discord.Intents.all()
intents.messages = True
bot = discord.Client(intents=intents)

bot_greetings = [
    "Hello!","Hi there!",
    "Hey!","Greetings!","Good day!","Hi!",
    "Hello there!","Hey there!","Hi!",
    "Hello!","Hi there!","Hey!","Greetings!",
    "Hello!","Hi!","Hey there!","Hello!","Hi there!",
    "Hey!","Greetings!","Hello!",
    "Hi!","Hey there!","Hello!","Hi there!",
    "Hey!","Greetings!","Hello!","Hi!","Hey there!",
    "Hello!","Hi there!","Hey!","Greetings!",
    "Hello!","Hi!","Hey there!"
]
usr_greetings = [
    "hello!","hi there!","hey!","good morning!",
    "good afternoon!","good evening!","yo!",
    "greetings!","howdy!","hey, what's up?","hiya!",
    "hello, how are you?","hi!","hello world!","hey, hi!","morning!",
    "afternoon!","evening!","hiya there!",
    "hi","hey there!","good day!","hi, how are you?",
    "hey, how's it going?","yo there!","hey, what's new?",
    "hey buddy!","hi mate!","good to see you!",
    "howdy there!","hey, nice to meet you!","hi friend!",
    "hey you!","hello friend!","hi everyone!","hey folks!",
    "hi team!","hey all!","hello folks!","hi folks!","hey team!",
    "hi friends!","hello everyone!",
    "hey there friend!","hiya friend!","hey there buddy!",
    "hello there!","hi buddy!","hello mate!","hey pal!",
    "hi pal!","hello pal!","hey dude!","hi dude!","hello dude!","hello"
]

@bot.event
async def on_ready():
    print('Bot ready!')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() in (usr_greetings):
        await message.channel.send(random.choice(bot_greetings))


bot.run(token)



