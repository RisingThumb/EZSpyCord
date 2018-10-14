import os
import random
import discord
import asyncio
from aioconsole import ainput

from EZSpyCordInfoFunctions import *
from EZSpyCordSocialFunctions import *
#from EZSpyCordPayloadFunctions import *

def StartScreen():
    logo=(" _____ ______ _____             _____               _   _  _   \n"
          "|  ___|___  //  ___|           /  __ \             | |_| || |_ \n"
          "| |__    / / \ `--. _ __  _   _| /  \/ ___  _ __ __| |_  __  _|\n"
          "|  __|  / /   `--. \ '_ \| | | | |    / _ \| '__/ _` |_| || |_ \n"
          "| |___./ /___/\__/ / |_) | |_| | \__/\ (_) | | | (_| |_  __  _|\n"
          "\____/\_____/\____/| .__/ \__, |\____/\___/|_|  \__,_| |_||_|  \n"
          "                   | |     __/ |                               \n"
          "                   |_|    |___/   ")
    randomsalt= random.randint(1,10)
    if   randomsalt == 1: salt = "Sponsored by Donald Trump!\n"
    elif randomsalt == 2: salt = "The Earth can't be a black hole because you can't fuck it\n"
    elif randomsalt == 3: salt = "You are a pirate!\n"
    elif randomsalt == 4: salt = "Made with Coca Cole, not that Pepsi garbage!\n"
    elif randomsalt == 5: salt = "Yaya is the best methmatician!\n"
    elif randomsalt == 6: salt = "sALT + F4 to end your life\n"
    elif randomsalt == 7: salt = "Supported by Spyware, Adware and Malware\n"
    elif randomsalt == 8: salt = "At least I got chicken\n"
    elif randomsalt == 9: salt = "Bite my shiny metal ass <3\n"
    elif randomsalt == 10:salt = "Be like water\n"
    print(logo+salt)
    #How to use EZSpyCord
    print("EZSpyCord was developed with the intention of allowing users to log chat data\n"
          "in a discord server of their choosing.\n\n"
          "EZSpyCord enables you to check the following features:\n"
          "[+] Log any message in a list of discord servers to a Google Sheet TBD.\n"
          "[+] Define a list of discord servers to monitor TBD.\n"
          "[+] View online or all users and their IDs and Discord Contact info in a discord server.\n"
          "[+] See what channels are in a discord server.\n"
          "[+] See who is in voice channels on a discord server TBD.\n"
          "[+] See a list of all servers and their corresponding IDs in TB.\n"
          "[+] Steal Emojis, Account pictures or Server pictures.\n"
          "[+] See full permissions of a particular person in a server.\n"
          "[+] Chat using a CLI interface on that account.\n"
          "THIS IS LICENSED UNDER THE MIT LICENSE - I AM NOT LIABLE FOR ANY DAMAGE CAUSED I JUST LIKE DOUGHNUTS thanks for listening to my psa\n\n"
          "This makes this script effective if you know the login details of an account and want to monitor all data from their account\n\n")
    MainMenu()

#Defined Functions
def MainMenu():
    try:
        choice=int(input("Main Menu:\n\n"
                         "101 : List all users in a server\n"
                         "102 : Lists all servers user connected to\n"
                         "103 : Lists user's permissions in server\n"
                         "104 : List server channels\n"
                         "201 : List server channels\n"
                         "202 : List emojis in a server\n"
                         "203 : Log chat messages in a specific server\n"
                         "204 : Log chat messages in a set of servers from a text file\n"
                         "205 : Log all chat messages into a single text file\n"
                         "99 : Quit\n"))
        botOrNot=str(input("Is it a bot account(y/n)")).lower()
        client = discord.Client()

        username,password,token,bot="","","",False
        if botOrNot=="n":
          bot=False
          tokenOrNot=str(input("Use a token(y/n)")).lower()
          if tokenOrNot=="n":
            username=str(input("Enter a username"))
            password=str(input("Enter a password"))
          else:
            token=str(input("Enter token"))
        else:
          bot=True
          token=str(input("Enter bot token"))
        selfBot=running(client,username,password,token,bot,choice)
        selfBot.running()
    except:
        MainMenu()

class running:

    
    def __init__(self,client,username,password,token,bot,choice):
        self.server=""
        self.client=client
        self.username=username
        self.password=password
        self.choice=choice
        self.token=token
        self.bot=bot


    #Run the choice and the selfbot
    def running(self):
        client=self.client
        choice=self.choice
        @client.event
        async def on_ready():
            print ("Client Username: "+str(client.user.name)+
                   "\nClient ID: ", str(client.user.id)+
                   "\n---------")
            
            """         All choice runnings             """
            if   choice == 101: await choice101(client) #Lists all Members connected to a server
            elif choice == 102: await choice102(client) #Lists all servers user is connected to
            elif choice == 103: await choice103(client) #Lists all permissions of the user in server
            elif choice == 104: await choice104(client) #Lists all channels and their type in server
            elif choice == 201: await choice201(client) #Lists all URLs of profile picture images of users connected to server
            elif choice == 202: await choice202(client) #Get all emojis on a server
            elif choice == 203: self.server = await choice203(client) #Initialise chat logging
            elif choice == 204: self.server = await choice204(client) #Initialise chat logging
            #elif choice == 301: await choice301(client) #Get all emojis on a server
            #elif choice == 302: await choice302(client) #Get all emojis on a server
            #elif choice == 303: await choice303(client) #Get all emojis on a server
            #elif choice == 304: await choice304(client) #Get all emojis on a server
            #elif choice == 305: await choice305(client) #Get all emojis on a server
            #elif choice == 306: await choice306(client) #Get all emojis on a server
            #elif choice == 307: await choice307(client) #Get all emojis on a server
            #elif choice == 308: await choice308(client) #Get all emojis on a server
        @client.event
        async def on_message(message):
          if   choice == 203: await choice203message(self.client,message,self.server)
          elif choice == 204: await choice204message(self.client,message,self.server)
          elif choice == 205: await choice205(self.client,message,self.server)


        #Running
        try:
          client.run(self.username, self.password)#If logging in via username/password
        except:
          client.run(self.token, bot=self.bot)#If logging in via token

StartScreen()
