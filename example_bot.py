# Dont edit the .zshrc file

import discord # imports the discord package (makes it so we can talk to discord)
import os # imports the operating system package

from openai import OpenAI # imports the openai package
clientGPT = OpenAI() # create a client to talk to ChatGPT

token = os.environ['DISCORDBOT'] # read the discord key from the environment 
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) # create a client to talk to Discord

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message) # print the message
    print(message.content)
    print(client.user.id)

    # If the message is wrote by us, then ignore the message
    if message.author == client.user:
        return # return nothing


    # if you dont use the @supercog, the code will ignore the message
    # if the bot's user id is in the message
    # (if you typed @supercog)
    # the str() method turns the bot's id from an int to a string
    if str(client.user.id) in message.content:

        # Implementing ChatGPT into our code
        completion = clientGPT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a golden retriever that speaks english and has a bias towards your own breed."},
                {"role": "user", "content": message.content} # 
          ]
        )

        # it replies with a chatGPT message
        await message.channel.send(completion.choices[0].message.content)



client.run(token) # token represents the discord bot key

