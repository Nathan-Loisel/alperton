import os 
import subprocess
from utils import COLOR, STATUS, OUTPUT

from modules.mod_path import mod_path
from modules.mod_suid import mod_suid
from modules.mod_sudo import mod_sudo
from modules.mod_bak import mod_bak
from modules.mod_hidden import mod_hidden
from modules.mod_homes import mod_homes

modules = [mod_path(), mod_suid(), mod_sudo(), mod_bak(), mod_hidden(), mod_homes()]

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
        output_type, alert, alert_title, output = module.run()
        if output_type == OUTPUT.binary:
            if alert:
                print(STATUS.bad + " " + alert_title)
                print(output)

        elif output_type == OUTPUT.multiple_binary:
            for i in range(len(alert)):
                if alert[i]:
                    print(STATUS.bad + " " + alert_title[i])
                    print(output[i])
                    print("")

        print("")

if(__name__ == "__main__"):
    __main__()