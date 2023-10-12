import os
import subprocess
from utils import COLOR, STATUS, OUTPUT


class mod_history:
    def __init__(self):
        self.name = "History"
        self.output_type = OUTPUT.multiple_binary
        self.alert = [False, False]
        self.alert_title = ["", ""]
        self.output = ["", ""]

    def run(self):
        # .bash_history
        bash_history = subprocess.Popen(["find", "/", "-name", ".bash_history", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = bash_history.communicate()
        bash_history = out.decode("utf-8").split("\n")
        bash_history = list(filter(None, bash_history))
        if len(bash_history) > 0:
            self.alert[0] = True
            self.alert_title[0] = ".bash_history found"
            for i in bash_history:
                self.output[0] += "\n" + i

        # .zsh_history
        zsh_history = subprocess.Popen(["find", "/", "-name", ".zsh_history", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = zsh_history.communicate()
        zsh_history = out.decode("utf-8").split("\n")
        zsh_history = list(filter(None, zsh_history))
        if len(zsh_history) > 0:
            self.alert[1] = True
            self.alert_title[1] = ".zsh_history found"
            for i in zsh_history:
                self.output[1] += "\n" + i

        return self.output_type, self.alert, self.alert_title, self.output