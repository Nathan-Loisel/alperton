import os
import subprocess
from utils import COLOR, STATUS, OUTPUT

class mod_homes:
    def __init__(self):
        self.name = "Home directory"
        self.output_type = OUTPUT.binary
        self.alert = False
        self.alert_title = ""
        self.output = ""

    def run(self):
        home = subprocess.Popen(["ls", "-ahlR", "/home"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_home, err = home.communicate()
        out = out_home.decode("utf-8")
        root = subprocess.Popen(["ls", "-ahlR", "/root"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_root, err = root.communicate()
        out += out_root.decode("utf-8")

        if len(out) > 0:
            self.alert = True
            self.alert_title = "Home directories"
            self.output = out

        if len(self.output.split("\n")) > 20:
            self.output = "\n".join(self.output.split("\n")[:20]) + "\n..."

        return self.output_type, self.alert, self.alert_title, self.output
        
