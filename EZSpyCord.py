import discord
import asyncio
from aioconsole import ainput
#Functions choice101-199
from EZSpyCordMenu import *
from EZSpyCordInfoFunctions import *
#Functions choice201-299
from EZSpyCordSocialFunctions import *
import getpass
#Logs in
def login(choiceselected):
    try:
        username = str(input("Enter email for your account:\n"))
        password = str(getpass.getpass("Enter password(Invisible as you type):\n"))
        global choice
        choice = choiceselected
        try:
            client = discord.Client()
            running(client,username, password)
        except:
            pass
    except:
        print("Unable to login to account... Try again...")

#To be put in the EZSpyCordSocialFunctions module, handles Channel communications
async def choice204(client):
    global id2
    id1 = await ainput("Enter ID of server\n")
    chans = ("[+] Channels\n")
    for server in client.servers:
        if server.id == str(id1):
            for channel in server.channels:
                if str(channel.type) == "text":chans+=( "  [-]"+channel.name+" - "+channel.id+"\n")
    print(chans)
    id2 = await ainput("Enter ID of Channel")
    for server in client.servers:
        if server.id == str(id1):
            for channel in server.channels:
                if channel.id == str(id2):
                    user = channel
                    break
    while True:
        message = await ainput("\nEZSpyCord > ")
        if str(message) == "help":print("type 'cd' to go back")
        elif str(message) == "refresh":print("Refreshing messages")
        elif str(message) == "cd":
            await client.close()
        else: await client.send_message(user,str(message))
        
#To be put in the EZSpyCordSocialFunctions module, handles Person Communications
async def choice203(client):
    global id3
    id3 = await ainput("Enter ID of user\n")
    for server in client.servers:
        for member in server.members:
            if member.id == str(id3):
                print("Found User...")
                user=member
                break
        break
    while True:
        message = await ainput("\nEZSpyCord > ")
        if str(message) == "help": print("type 'cd' to go back")
        elif str(message) == "cd":await client.close()
        else:await client.send_message(user,str(message))





def running(client,username, password):
    @client.event
    async def on_ready():
        print ("Client Username: "+str(client.user.name)+
               "\nClient ID: ", str(client.user.id)+
               "\n---------")
        global choice
        global id2
        id2=0#Defined to prevent errors on recieving messages

        
        """         ALL INFO GATHERING HERE             """
        if choice == 101: await choice101(client) #Lists all Members connected to a server
        if choice == 102: await choice102(client) #Lists all servers user is connected to
        if choice == 103: await choice103(client) #Lists all permissions of the user in server
        if choice == 104: await choice104(client) #Lists all channels and their type in server

        """         ALL SOCIAL ENGINEERING HERE         """
        if choice == 201: await choice201(client) #Lists all URLs of profile picture images of users connected to server
        if choice == 202: await choice202(client) #Get all emojis on a server
        if choice == 203: await choice203(client) #Chat with a person
        if choice == 204: await choice204(client) #Chat with people in a server's channel

        """         ALL PAYLOADS HERE                   """
        #if choice == 301: await choice301(client)...

        """         ALL USER'S TOOLS HERE               """
        #if choice == 401: await choice301(client)...

    @client.event
    async def on_message(message):
        global id3
        #Put this in social functions module+refactor it
        if choice == 203:
            try:
                if message.author.id == str(id3):
                    attachments = message.attachments
                    links = "N/A"
                    for item in attachments:
                        links = item['url']
                    print("[+]"+str(message.author)+"\n  [-] "+str(message.content)+"\n  [-] "+str(links)+"\n")
            except:
                print(message.content)
        global id2
        #Put this in social functions module+refactor it
        if choice == 204:
            if message.channel.id == str(id2):
                attachments = message.attachments
                links="N/A"
                for item in attachments:
                    links = item['url']
                print("[+]"+str(message.author.name)+"\n  [-] "+str(message.content)+"\n  [-] "+str(links)+"\n")

    client.run(username, password)

global choice
choice = 0
StartScreen(login)
print("/###/ SCRIPT END /###/")
