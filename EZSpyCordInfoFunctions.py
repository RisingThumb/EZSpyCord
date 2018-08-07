import sys
global non_bmp_map
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)




#Lists all users in server
async def choice101(client):
    id1 = str(input("Enter ID of server\n"))
    for server in client.servers:
        if server.id == id1:
            print("[+] All members connected to server "+str(server.name)+"\n")
            for member in server.members:
                print("   [-] Name : "+str(member.name.translate(non_bmp_map))+" | ID : "+str(member.id)+" | Role : "+str(member.top_role))
    await client.logout()
#Lists all servers user connected to
async def choice102(client):
    print("[+] All servers connected to\n")
    for server in client.servers:
        print("   [-] Name : "+str(server.name.translate(non_bmp_map))+" | ID : "+str(server.id)+" | Owner : "+str(server.owner.name))
    await client.logout()        
#Lists user's permissions in server
async def choice103(client):
    id1 = str(input("Enter ID of server\n"))
    id2 = str(input("Enter ID of user\n"))
    for server in client.servers:
        if server.id == id1:
            for member in server.members:
                if member.id == id2:
                    perms=member.server_permissions
                    print("   [-] Name : "+str(member.name.translate(non_bmp_map))+"\n"
                          "    Administrator ? : "+str(perms.administrator)+"\n"
                          "    Ban Members ? : "+str(perms.ban_members)+"\n"
                          "    Kick Members ? : "+str(perms.kick_members)+"\n"
                          "    Manage Server ? : "+str(perms.manage_server)+"\n"
                          "    Manage Channels ? : "+str(perms.manage_channels)+"\n"
                          "    Manage Roles ? : "+str(perms.manage_roles)+"\n"
                          "    Manage Messages ? : "+str(perms.manage_messages)+"\n"
                          "    Manage Nickname ? : "+str(perms.manage_nicknames)+"\n"
                          "    Manage Webhooks ? : "+str(perms.manage_webhooks)+"\n"
                          "    Manage Emojis ? : "+str(perms.manage_emojis)+"\n"
                          "    Send Messages ? : "+str(perms.send_messages)+"\n"
                          "    Send TTS Messages ? : "+str(perms.send_tts_messages)+"\n"
                          "    Send Embed links ? : "+str(perms.embed_links)+"\n"
                          "    Send Files ? : "+str(perms.attach_files)+"\n"
                          "    Read Messages ? : "+str(perms.read_messages)+"\n"
                          "    Read Message History ? : "+str(perms.read_message_history)+"\n"
                          "    Add reactions ? : "+str(perms.add_reactions)+"\n"
                          "    View Audit Logs ? : "+str(perms.view_audit_logs)+"\n"
                          "    Mention Everyone ? : "+str(perms.mention_everyone)+"\n"
                          "    External Emojis ? : "+str(perms.external_emojis)+"\n"
                          "    Connect to voice channel ? : "+str(perms.connect)+"\n"
                          "    Speak in voice channel ? : "+str(perms.speak)+"\n"
                          "    Mute Members ? : "+str(perms.mute_members)+"\n"
                          "    Deafen Members ? : "+str(perms.deafen_members)+"\n"
                          "    Move Members ? : "+str(perms.move_members)+"\n"
                          "    Use Voice Activation ? : "+str(perms.use_voice_activation)+"\n"
                          "    Change Nickname ? : "+str(perms.change_nickname)+"\n"
                          )
    await client.logout()
#List server channels
async def choice104(client):
    id1 = str(input("Enter ID of server\n"))
    for server in client.servers:
        if server.id == id1:
            print("[+] "+str(server.name))
            for channel in server.channels:
                print("   [-] Name : "+str(channel.name)+" | Channel ID : "+str(channel.id)+" | Type : "+str(channel.type))
    await client.logout()
