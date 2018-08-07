#Remove all channels from a specific server
async def choice301(client):
    try:
        id1 = str(input("Enter ID of server\n"))
        for server in client.servers:
            if server.id == id1:
            	channels=server.channels
                for channel in channels:
                    print("[+] Deleting channel : "+str(channel.name))
                    await client.delete_channel(channel)
    except discord.Forbidden: print("Insufficient permissions")
    except: print("An error occured...")
    await client.logout()

#Deletes a specific server
async def choice302(client):
    try:
        id1 = str(input("Enter ID of server\n"))
        for server in client.servers:
            if server.id == id1:
                print("[+] Deleting server : "+str(server.name))
                await client.delete_server(server)
    except discord.Forbidden:
        print("Insufficient permissions")
    except:
        print("An error occured...")
    await client.logout()

#Deletes all servers the user can
async def choice303(client):
	servers=client.servers
    for server in servers:
        try:
            print("[+] Deleting server : "+str(server.name))
            await client.delete_server(server)
        except discord.Forbidden:
            print("Insufficient permissions")
        except:
            print("An error occured...")
        await client.logout()

#Deletes all channels the user can
async def choice304(client):
    for server in client.servers:
    	channels=server.channels
        for channel in channels:
            try:
                print("[+] Deleting channel : "+str(channel.name))
                await client.delete_channel(channel)
            except discord.Forbidden:
                print("Insufficient permissions")
            except:
                print("An error occured...")
    await client.logout()

#Bans all members from a specified server
async def choice305(client):
    try:
        id1 = str(input("Enter ID of server\n"))
        for server in client.servers:
            if server.id == id1:
            	members=server.members
                for member in members:
                    print("[+] Banning : "+str(member.name))
                    try:
                        await client.ban(member)
                    except:
                        print("   [-] Couldn't ban user")
    except discord.Forbidden: print("Insufficient permissions")
    except: print("An error occured...")
    await client.logout()

#Kicks all members from a specified server
async def choice306(client):
    try:
        id1 = str(input("Enter ID of server\n"))
        for server in client.servers:
            if server.id == id1:
            	members=server.members
                for member in members:
                    print("[+] Kicking : "+str(member.name))
                    try:
                        await client.kick(member)
                    except:
                        print("   [-] Couldn't ban user")
    except discord.Forbidden: print("Insufficient permissions")
    except: print("An error occured...")
    await client.logout()  

#Bans all users the user can
async def choice307(client):
    for server in client.servers:
    	members=server.members
        for member in members:
            try:
                print("[+] Banning user : "+str(member.name))
                await client.ban(member)
            except discord.Forbidden:
                print("Insufficient permissions")
            except:
                print("An error occured...")
    await client.logout()

#Kicks all users the user can
async def choice308(client):
    for server in client.servers:
    	members=server.members
        for member in members:
            try:
                print("[+] Kicking user : "+str(member.name))
                await client.kick(member)
            except discord.Forbidden:
                print("Insufficient permissions")
            except:
                print("An error occured...")
    await client.logout()
