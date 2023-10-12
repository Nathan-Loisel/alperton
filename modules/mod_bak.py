import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_bak:
    def __init__(self):
        self.name = "Backup files"
        self.output = output(OUTPUT_TYPE.alert)

    def run(self):
        COMMON_BAK_OLD_FILES = []

        # .bak
        bak = subprocess.Popen(["find", "/", "-name", "*.bak", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = bak.communicate()
        bak = out.decode("utf-8").split("\n")
        bak = list(filter(None, bak))
        for i in bak:
            if i in COMMON_BAK_OLD_FILES:
                bak.remove(i)
        if len(bak) > 0:
            out = ""
            for i in bak:
                out += "\n" + i
            self.output.addEntry([".bak files found", out])

        # .old
        old = subprocess.Popen(["find", "/", "-name", "*.old", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = old.communicate()
        old = out.decode("utf-8").split("\n")
        old = list(filter(None, old))
        for i in old:
            if i in COMMON_BAK_OLD_FILES:
                old.remove(i)
        if len(old) > 0:
            out = ""
            for i in old:
                out += "\n" + i
            self.output.addEntry([".old files found", out])

        return self.output
