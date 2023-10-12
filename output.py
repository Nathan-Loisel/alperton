from utils import COLOR, STATUS, OUTPUT_TYPE

class output:
    def __init__(self, output_type):
        self.type = output_type
        self.content = []

    def addEntry(self, tab):
        self.content.append(tab)