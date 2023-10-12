import os
import subprocess
from utils import COLOR, STATUS, OUTPUT

class mod_sudo:
    def __init__(self):
        self.name = "Sudo rights"
        self.output_type = OUTPUT.binary
        self.alert = False
        self.alert_title = ""
        self.output = ""

    def run(self):
        sudo = subprocess.Popen(["sudo", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sudo.communicate()
        if not "not allowed to run sudo" in err.decode("utf-8"):
            self.alert = True
            self.alert_title = "User has sudo rights"
            self.output = out.decode("utf-8")
        return self.output_type, self.alert, self.alert_title, self.output