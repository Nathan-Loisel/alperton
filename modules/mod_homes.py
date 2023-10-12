import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_homes:
    def __init__(self):
        self.name = "Home directory"
        self.output = output(OUTPUT_TYPE.info)

    def run(self):
        home = subprocess.Popen(["ls", "-ahlR", "/home"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_home, err = home.communicate()
        out = out_home.decode("utf-8")
        root = subprocess.Popen(["ls", "-ahlR", "/root"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_root, err = root.communicate()
        out += out_root.decode("utf-8")

        if len(out) > 0:
            self.output.addEntry(["Home directory listing", out])

        if len(self.output[len(self.output) - 1][1].split("\n")) > 20:
            self.output[len(self.output) - 1][0] = "Home directory listing (truncated)"
            self.output[len(self.output) - 1][1] = "\n".join(self.output[len(self.output) - 1][1].split("\n")[0:20]) + "\n[...]"

        return self.output
        
