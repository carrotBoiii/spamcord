import discord
from decouple import config

client = discord.Client()

bot_token = config('TOKEN')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


prefix = ';'

check = False


@client.event
async def on_message(message):
    if message.context.startswith(prefix + 'stop'):
        global check
        check = True


try:
    @client.event
    async def on_message(message):

        send = ""

        todo = (message.content.split(prefix, 1)[1] + ' ;end').split(' ' + prefix)

        if message.author == client.user:
            return

        if message.content.startswith(prefix + 'help'):
            await message.channel.send(">>> ***Hey! " + message.author.name + ''',*** you can *spam* messages into any text channel just by typing 
             `;spam ;[your text] ;[number of times to send]`
              _Example_ : `;spam ;I am Spamcord ;10`
              
              **ENJOY TROLLING  YOUR FRIENDS XD** :joy:''')
        if message.content.startswith(prefix + 'hello') or message.content.startswith(prefix + 'hi'):
            await message.channel.send('Hello! ' + message.author.name)

        if message.content.startswith(prefix + 'spam'):
            try:
                for i in range(int(todo[2])):
                    global check
                    await message.channel.send(todo[1])
                    if check:
                        check = False
                        break
            finally:
                print(IndexError)
finally:
    print(Exception)
client.run(bot_token)
