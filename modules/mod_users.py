import os
import subprocess
from utils import COLOR, STATUS, OUTPUT


class mod_users:
    def __init__(self):
        self.name = "Users"
        self.output_type = OUTPUT.multiple_binary
        self.alert_title = ["", "", ""]
        self.output = ["", "", ""]

    def run(self):
        users = subprocess.Popen(["tail", "-n", "10", "/etc/passwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_users, err = users.communicate()
        out = out_users.decode("utf-8")
        if len(out) > 0:
            self.alert_title[0] = "Users"
            self.output[0] = out

        no_login = subprocess.Popen(["grep", "-vE", "nologin", "/etc/passwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_no_login, err = no_login.communicate()
        out = out_no_login.decode("utf-8")
        if len(out) > 0:
            self.alert_title[2] = "Users with no login"
            self.output[2] = out

        groups = subprocess.Popen(["tail", "-n", "10", "/etc/group"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_groups, err = groups.communicate()
        out = out_groups.decode("utf-8")
        if len(out) > 0:
            self.alert_title[1] = "Groups"
            self.output[1] = out

        return self.output_type, self.alert, self.alert_title, self.output