import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output


class mod_users:
    def __init__(self):
        self.name = "Users"
        self.output = output(OUTPUT_TYPE.info)

    def run(self):
        users = subprocess.Popen(["tail", "-n", "10", "/etc/passwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_users, err = users.communicate()
        out = out_users.decode("utf-8")
        if len(out) > 0:
            self.output.addEntry(["Users", out])

        no_login = subprocess.Popen(["grep", "-vE", "nologin", "/etc/passwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_no_login, err = no_login.communicate()
        out = out_no_login.decode("utf-8")
        if len(out) > 0:
            self.output.addEntry(["Users with login", out])

        groups = subprocess.Popen(["tail", "-n", "10", "/etc/group"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_groups, err = groups.communicate()
        out = out_groups.decode("utf-8")
        if len(out) > 0:
            self.output.addEntry(["Groups", out])

        return self.output