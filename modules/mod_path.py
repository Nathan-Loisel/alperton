import os
import subprocess
from utils import COLOR, STATUS, OUTPUT
from output import output

class mod_path:
    def __init__(self):
        self.name = "Path"
        self.output = output(OUTPUT_TYPE.alert)

    def run(self):
        path = os.environ["PATH"]
        path_split = path.split(":")
        for i in path_split:
            if i == ".":
                self.output.addEntry(["Path contains current directory", path])
                break
        return self.output