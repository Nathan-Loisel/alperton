import os
import subprocess
from utils import COLOR, STATUS, OUTPUT

class mod_path:
    def __init__(self):
        self.name = "Path"
        self.output_type = OUTPUT.binary
        self.alert = False
        self.alert_title = ""
        self.output = ""

    def run(self):
        path = os.environ["PATH"]
        path_split = path.split(":")
        for i in path_split:
            if i == ".":
                self.alert = True
                self.alert_title = "Path has a '.' entry"
                self.output = path
                break
        return self.output_type, self.alert, self.alert_title, self.output