# Script that runs on linux to check for privilege escalations
# Style:
# (blue) [-] for infos
# (green) [+] for good news
# (red) [!] for bad news

# Styles
class COLOR:
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m'

class STATUS:
    info = COLOR.blue + "[-]" + COLOR.reset
    good = COLOR.green + "[+]" + COLOR.reset
    bad = COLOR.red + "[!]" + COLOR.reset

import os 
import subprocess

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

# Module: check if path has a "." entry
import modules.mod_path
path_check = modules.mod_path.mod_path()
path_check.run()

# Module: check for sudo rights
print(STATUS.info + " Checking sudo rights")
sudo = subprocess.Popen(["sudo", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = sudo.communicate()
if "not allowed to run sudo" in err.decode("utf-8"):
    print(STATUS.info + " No sudo rights")
else:
    print(STATUS.good + " Sudo rights:")
    print(out.decode("utf-8"))
print("")

# Module: check for suid binaries
COMMON_SUID_BINARIES = ["/bin/mount", \
                        "/bin/umount", \
                        "/bin/ping", \
                        "/bin/ping6", \
                        "/bin/su", \
                        "/usr/bin/sudo", \
                        "/usr/bin/passwd", \
                        "/usr/bin/newgrp", \
                        "/usr/bin/chsh", \
                        "/usr/bin/chfn"]
print(STATUS.info + " Checking suid binaries")
suid = subprocess.Popen(["find", "/", "-perm", "-4000", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = suid.communicate()
suid = out.decode("utf-8").split("\n")
suid = list(filter(None, suid))
for i in suid:
    if i in COMMON_SUID_BINARIES:
        suid.remove(i)
print(STATUS.good + " Uncommon suid binaries:")
for i in suid:
    print(i)

# Module: find all .bak or .old files
COMMON_BAK_OLD_FILES = []
print(STATUS.info + " Checking for .bak and .old files")
bak = subprocess.Popen(["find", "/", "-name", "*.bak", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = bak.communicate()
bak = out.decode("utf-8").split("\n")
bak = list(filter(None, bak))
for i in bak:
    if i in COMMON_BAK_OLD_FILES:
        bak.remove(i)
if len(bak) > 0:
    print(STATUS.good + " .bak files:")
    for i in bak:
        print(i)
old = subprocess.Popen(["find", "/", "-name", "*.old", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = old.communicate()
old = out.decode("utf-8").split("\n")
old = list(filter(None, old))
for i in old:
    if i in COMMON_BAK_OLD_FILES:
        old.remove(i)
if len(old) > 0:
    print(STATUS.good + " .old files:")
    for i in old:
        print(i)
print("")

# Module: check home directories
print(STATUS.info + " Checking home directories")
home = subprocess.Popen(["ls", "-ahlR", "/home"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = home.communicate()
print(out.decode("utf-8"))
print("")
root = subprocess.Popen(["ls", "-ahlR", "/root"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = root.communicate()
print(out.decode("utf-8"))
print("")

# Module: check for hidden files
print(STATUS.info + " Checking for hidden files")
hidden = subprocess.Popen(["find", "/", "-name", ".*", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = hidden.communicate()
hidden = out.decode("utf-8").split("\n")
hidden = list(filter(None, hidden))
if len(hidden) > 0:
    print(STATUS.good + " Hidden files:")
    for i in hidden:
        print(i)
print("")

# Module: get all manually installed packages 
print(STATUS.info + " Checking manually installed packages")
packages = subprocess.Popen(["apt-mark", "showmanual"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = packages.communicate()
packages = out.decode("utf-8").split("\n")
packages = list(filter(None, packages))
if len(packages) > 0:
    print(STATUS.good + " Manually installed packages:")
    for i in packages:
        print(i)
print("")