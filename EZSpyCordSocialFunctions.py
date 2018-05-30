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
