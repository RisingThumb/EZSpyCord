import os
import random


#Defined Functions
def MainMenu(login):
    try:
        global choice
        choice=int(input("Main Menu:\n\n"
                         "1 : Information Gathering tools\n"
                         "2 : Social Engineering chat tools\n"
                         "3 : Payload tools\n"
                         "4 : User modifications\n"
                         "99 : Quit\n"))
        if choice == 1:
            InfoMenu(login)
        if choice == 2:
            SocialMenu(login)
        if choice == 3:
            PayloadMenu(login)
        if choice == 4:
            NullMenu(login)
        if choice == 99:
            quit()
    except:
        MainMenu(login)


def InfoMenu(login):
    try:
        global choice
        choice=int(input("Information Gathering Menu:\n\n"
                         "1 : List all members from a server(REQ:Server ID)\n"
                         "2 : List all server names and IDs\n"
                         "3 : List all pictures in server(REQ:Server ID)\n"
                         "4 : List all roles and permissions of a user in server(REQ:Server & User ID)\n"
                         "5 : List all channels and their type in a server(REQ:Server ID)\n"
                         "6 : Get all Emoji URLs(REQ:Server ID)\n"
                         "89 : Back\n"
                         "99 : Quit\n"))
        choice += 100
        if choice == int(199):
            quit()
        if choice == int(189):
            MainMenu(login)
        else:
            try:
                login(choice)
            except:
                quit()
    except:
        quit()

#For doing Social Engineering

def SocialMenu(login):
    try:
        global choice
        choice = int(input("Options Menu:\n\n"
                         "1 : List all pictures in server(REQ:Server ID)\n"
                         "2 : Get all Emoji URLs(REQ:Server ID)\n"
                         "3 : Private Message a person(REQ:User ID)\n"
                         "4 : Channel Chat(REQ:Server ID)\n"
                         "89 : Back\n"
                         "99 : Quit\n"))
        choice+=200
        if choice == int(299):
            quit()
        if choice == int(289):
            MainMenu(login)
        else:
            try:
                login(choice)
            except:
                quit()
    except:
        quit()
        
#For running any payloads
        
def PayloadMenu(login):
    try:
        global choice
        choice = int(input("Options Menu:\n\n"
                         "89 : Back\n"
                         "99 : Quit\n"))
        choice += 300
        if choice == 389:
            MainMenu(login)
        if choice == 399:
            MainMenu(login)
        else:
            quit()
    except:
        quit()
        
#For user modifications/User payloads
        
def NullMenu(login):
    try:
        global choice
        choice=int(input("Options Menu:\n\n"
                         "89 : Back\n"
                         "99 : Quit\n"))
        choice += 400
        if choice == 489:
            MainMenu(login)
        if choice == 499:
            quit()
        else:
            quit()
    except:
        quit()

def StartScreen(login):
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
    MainMenu(login)
