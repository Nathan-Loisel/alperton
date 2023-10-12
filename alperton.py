import os 
import subprocess
from utils import COLOR, STATUS, OUTPUT

from modules.mod_path import mod_path

modules = [mod_path()]

# auto run
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