import os
import subprocess
from utils import COLOR, STATUS, OUTPUT

class mod_bak:
    def __init__(self):
        self.name = "Backup files"
        self.output_type = OUTPUT.multiple_binary
        self.alert = [False, False]
        self.alert_title = ["", ""]
        self.output = ["", ""]

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
            self.alert[0] = True
            self.alert_title[0] = ".bak files found"
            for i in bak:
                self.output[0] += "\n" + i

        # .old
        old = subprocess.Popen(["find", "/", "-name", "*.old", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = old.communicate()
        old = out.decode("utf-8").split("\n")
        old = list(filter(None, old))
        for i in old:
            if i in COMMON_BAK_OLD_FILES:
                old.remove(i)
        if len(old) > 0:
            self.alert[1] = True
            self.alert_title[1] = ".old files found"
            for i in old:
                self.output[1] += "\n" + i

        return self.output_type, self.alert, self.alert_title, self.output
