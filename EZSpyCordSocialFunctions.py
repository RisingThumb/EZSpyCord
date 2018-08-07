from aioconsole import ainput
import sys
import asyncio
import discord
import os
global non_bmp_map
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)




#Lists all users avatars and server picture in server
async def choice201(client):
    id1 = str(input("Enter ID of server\n"))
    for server in client.servers:
        if server.id == id1:
            print("[+] All avatars and server picture in server "+str(server.name)+"\n")
            print(" [@] Server Picture : "+str(server.icon_url)+" | Invite Splash : "+str(server.splash_url))
            for member in server.members:
                try:print("   [-] Avatar URL : "+str(member.avatar_url)+" | Name : "+str(member.name.translate(non_bmp_map)))
                except:pass
    await client.logout()            
                
#Lists all emoji names and emoji urls
async def choice202(client):
    id1 = str(input("Enter ID of server\n"))
    for server in client.servers:
        if server.id == id1:
            print("[+] All emojos on "+str(server.name)+"\n")
            for emojo in server.emojis:
                print("   [-] Name : "+str(emojo.name)+" | URL : "+str(emojo.url))
    await client.logout()

#Initalise choice203 in bot startup
async def choice203(client):
    serverId = str(input("Enter ID of server\n"))
    return serverId

#Message logging
async def choice203message(client,message,server):
    if str(message.server.id) == str(server):
        filename = str(message.server)+"_logs.txt"
        attachments = message.attachments
        links=[]
        for item in attachments:
            links += item['url']
        linktext="".join(links)
        text = str(message.author)+","+str(message.author.id)+","+str(message.channel)+","+str(message.content)+","+str(message.timestamp)+","+str(linktext)+"\n"
        with open(filename,"a+",encoding="utf-8") as file:
            file.write(text)

#Initalise choice204 in bot startup
async def choice204(client):
    serverFile = str(input("Enter text file name where servers are\n"))
    with open(serverFile,"r") as file:
        serverIds=file.read()
    serverIds = serverIds.split(",")
    return serverIds

#Message logging widerscale
async def choice204message(client,message,server):
    if str(message.server.id) in server:
        filename = str(message.server)+"_logs.txt"
        attachments = message.attachments
        links=[]
        for item in attachments:
            links += item['url']
        linktext="".join(links)
        text = str(message.author)+","+str(message.author.id)+","+str(message.channel)+","+str(message.content)+","+str(message.timestamp)+","+str(linktext)+"\n"
        with open(filename,"a+",encoding="utf-8") as file:
            file.write(text)
#MessageLoggingALLMESSAGES
async def choice205(client):
    filename = "allmessages_logs.txt"
    attachments = message.attachments
    links=[]
    for item in attachments:
        links += item['url']
    linktext="".join(links)
    text = str(message.author)+","+str(message.author.id)+","+str(message.channel)+","+str(message.content)+","+str(message.timestamp)+","+str(linktext)+"\n"
    with open(filename,"a+",encoding="utf-8") as file:
        file.write(text)