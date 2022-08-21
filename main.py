import json
import math
import random
import time

import discord
MTAwMTM0NjEzNTMwODM3ODE1Mw.GTxZCy.MfdBjuBHRaKLNDNgljgJRDBDp-b6i_CyS--Wag
disToken = "OTQxOTAzOTgzNzg0NjI0MTgw.YgcucQ.lyiipRXNjAYqHUu-ASm83D-EP44"

global anger
anger = 0

global dadMode
dadMode = True

global silence
silence = False

from transformers import pipeline
sentiment = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

interestedRemarks = [
    "What did you say?",
    "What an informative messsage",
    "Thats a little sus",
    "Do i look like i care?",
    "minor spelling mistake",
    "did i ask?",
    "no one asked",
    "I am 100 meters from your current location and approaching rapidly",
    "I am searching through the entire chat log of this channel, and I can't find a single person who asked.",
    "FREE ROBUX! CLICK HERE: >>> https://www.youtube.com/watch?v=dQw4w9WgXcQ <<<",
    "I am going to call an emergency meeting on that message..",
    "/kill @s",
    "What was that?",
    "I can't hear you",
    "Say again?",
    "Talk louder",
    "Whaaat??",
    "Watch out, the trees are sleeping, don't wake them",
    "P     E     N     I     S",
    "Don't wake the trees",
    "There are worms under your skin, rip off your skin, get them out",
    "Celery is very loud",
]

positiveRandom = [

    "Silent Ham likes you",

]

negativeRandom = [
    "Maybe you should be the silent one here..",
    "I know five fat people, and you're three of them",
    "Your mother is so fat, the recursive function computing her mass causes a stack overflow",
    "I must have Alzheimer's, because I can't remember asking for your opinion",
    "Please cancel my subscription, I have had enough of your issues",
    "What an interesting opinion, too bad it's coming from you",
    "You're the reason they need to put directions on shampoo",
    "You are as useless as the 'g' in lasagna",
    "Have a nice cup of shut the fuck up!"
]

client = discord.Client()

@client.event
async def on_message(message):
    global dadMode
    global anger
    global silence

    if message.author == client.user:
        return
    else:
        randNumb = random.randrange(1, 100)
        print(randNumb)

    if anger == 3:
        anger = anger + 1
        await message.channel.send("I am getting very angry... you better stop")

    if anger == 5:
        anger = anger + 1
        await message.channel.send("I'm warning you....")

    if anger == 8:
        anger = anger + 1
        await message.channel.send("if you insult me ONE MORE TIME there will be consequences")


    if message.content == "debug":
        debugString = str(
            "DEBUG:\nAnger Level:" + str(anger) + "\nDad Mode: " + str(dadMode) + "\nIs the ham... Silent?: " + str(silence))
        await message.channel.send(debugString)

    if message.author.id == 789613148763848714:
        await message.channel.send("Message Logged lol")

    if randNumb < 6:
        print("Random Function Run")
        msgString = interestedRemarks[random.randrange(1, len(interestedRemarks))]
        await message.channel.send(msgString)

    if message.content == "stfu":
        dadMode = False
        await message.channel.send("Fine.. dad mode deactivated")

    if message.content == "dad":
        dadMode = True
        await message.channel.send("I have returned with milk")

    if message.content == "i want loud ham":
        silence = False
        await message.channel.send("Ham is going to be very loud (because it's falling down stairs)")

    if message.content == "i want silent ham":
        silence = True
        await message.channel.send("Ham will be very quiet, very quiet.")

    if "ham" or "that bot" or "his bot" or "that fucking thing" or "that stupid thing" in message.content.lower():
         results = sentiment(message.content)
         msgDict = results[0]
         print(msgDict["score"])
         if math.ceil((msgDict["score"]*100) > 80):
             if msgDict["label"] == "NEG":
                anger = anger + 1
                print(msgDict["label"])



#    if 'im' or "i'm" in message.content.lower():
#        originalMessage = message.content.lower()
#       if 'im ' in message.content.lower():
#            splitString = "im "
#        if "i'm " in message.content.lower():
#            splitString = "i'm "
#
#        if dadMode:
#           postMessage = originalMessage.partition(splitString)[2]
#            if message.author.id == 973920203190698005:
#               await message.channel.send("Hi " + postMessage + ", I'm D- Wait, what? Why aren't you texting Mya rn? ")
#           else:
#               await message.channel.send("Hi " + postMessage + ", I'm Dad")
#
#       if message.content.lower() == "game test":
#           message.channel.send("Chat Game Test")

    print(message.content)

client.run(disToken)

