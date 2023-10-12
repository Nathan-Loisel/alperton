import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_hidden:
    def __init__(self):
        self.name = "Hidden files"
        self.output = output(OUTPUT_TYPE.alert)

    def run(self):
        hidden = subprocess.Popen(["find", "/", "-name", ".*", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = hidden.communicate()
        hidden = out.decode("utf-8").split("\n")
        hidden = list(filter(None, hidden))
        if len(hidden) > 0:
            out = ""
            for i in hidden:
                out += "\n" + i
            self.output.addEntry(["Hidden files found", out])
        
        if(len(self.output[len(self.output) - 1][1].split("\n")) > 20):
            self.output[len(self.output) - 1][0] = "Hidden files found (truncated)"
            self.output[len(self.output) - 1][1] = "\n".join(self.output[len(self.output) - 1][1].split("\n")[0:20]) + "\n[...]"

        return self.output
