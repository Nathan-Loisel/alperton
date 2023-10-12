import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_sudo:
    def __init__(self):
        self.name = "Sudo rights"
        self.output = output(OUTPUT_TYPE.alert)

    def run(self):
        sudo = subprocess.Popen(["sudo", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sudo.communicate()
        if not "not allowed to run sudo" in err.decode("utf-8"):
            self.output.addEntry(["Sudo rights detected", out.decode("utf-8")])
        return self.output