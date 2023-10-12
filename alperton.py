import os 
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

from modules.mod_path import mod_path
from modules.mod_suid import mod_suid
from modules.mod_sudo import mod_sudo
from modules.mod_bak import mod_bak
from modules.mod_hidden import mod_hidden
from modules.mod_homes import mod_homes
from modules.mod_users import mod_users
from modules.mod_history import mod_history

modules = [mod_path(), mod_suid(), mod_sudo(), mod_bak(), mod_hidden(), mod_homes(), mod_users(), mod_history()]

def __main__():
    print(COLOR.red + " ▄▄▄       ██▓     ██▓███  ▓█████  ██▀███  ▄▄▄█████▓ ▒█████   ███▄    █ ")
    print("▒████▄    ▓██▒    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █ ")
    print("▒██  ▀█▄  ▒██░    ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒")
    print("░██▄▄▄▄██ ▒██░    ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒")
    print(" ▓█   ▓██▒░██████▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░")
    print(" ▒▒   ▓▒█░░ ▒░▓  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ")
    print("  ▒   ▒▒ ░░ ░ ▒  ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░    ░      ░ ▒ ▒░ ░ ░░   ░ ▒░")
    print("  ░   ▒     ░ ░   ░░          ░     ░░   ░   ░      ░ ░ ░ ▒     ░   ░ ░ ")
    print("      ░  ░    ░  ░            ░  ░   ░                  ░ ░           ░ " + COLOR.reset)
    print("")

    for module in modules:
        print(STATUS.info + " Running module: " + module.name)
        output = module.run()

        for i in range(len(output.content)):
            if(output.type == OUTPUT_TYPE.info):
                print(STATUS.info + " " + output.content[i][0])
            elif(output.type == OUTPUT_TYPE.alert):
                print(STATUS.binary + " " + output.content[i][0])
            print(output.content[i][1])
            print("")

        print("")

if(__name__ == "__main__"):
    __main__()