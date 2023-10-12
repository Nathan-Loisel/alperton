import os
import subprocess
from utils import COLOR, STATUS, OUTPUT

class mod_hidden:
    def __init__(self):
        self.name = "Hidden files"
        self.output_type = OUTPUT.binary
        self.alert = False
        self.alert_title = ""
        self.output = ""

    def run(self):
        hidden = subprocess.Popen(["find", "/", "-name", ".*", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = hidden.communicate()
        hidden = out.decode("utf-8").split("\n")
        hidden = list(filter(None, hidden))
        if len(hidden) > 0:
            self.alert = True
            self.alert_title = "Hidden files found"
            for i in hidden:
                self.output += "\n" + i
        
        if len(self.output.split("\n")) > 20:
            self.output = "\n".join(self.output.split("\n")[:20]) + "\n..."

        return self.output_type, self.alert, self.alert_title, self.output
