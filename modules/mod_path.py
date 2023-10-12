#from alperton import COLORS, STATUS

class mod_path:
    def __init__(self):
        self.name = "path"
        self.description = "Check if $PATH has a '.' entry"
        self.status = False
        self.output = ""

    def run(self):
        path = os.environ["PATH"]
        path = path_command.split(":")
        for i in path:
            if i == ".":
                self.status = True
                self.output = "Path has a '.' entry"
                break
        return self.status, self.output