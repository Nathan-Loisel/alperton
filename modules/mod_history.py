import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_history:
    def __init__(self):
        self.name = "History"
        self.output = output(OUTPUT_TYPE.info)

    def run(self):
        # .bash_history
        bash_history = subprocess.Popen(["find", "/", "-name", ".bash_history", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = bash_history.communicate()
        bash_history = out.decode("utf-8").split("\n")
        bash_history = list(filter(None, bash_history))
        if len(bash_history) > 0:
            out = ""
            for i in bash_history:
                out += "\n" + i
            self.output.addEntry([".bash_history found", out])

        # .zsh_history
        zsh_history = subprocess.Popen(["find", "/", "-name", ".zsh_history", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = zsh_history.communicate()
        zsh_history = out.decode("utf-8").split("\n")
        zsh_history = list(filter(None, zsh_history))
        if len(zsh_history) > 0:
            out = ""
            for i in zsh_history:
                out += "\n" + i
            self.output.addEntry([".zsh_history found", out])

        return self.output