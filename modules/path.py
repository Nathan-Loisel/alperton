#from alperton import COLORS, STATUS

def run():
    #print( STATUS.info + " Checking $PATH")
    path_command = os.environ["PATH"]
    path_command = path_command.split(":")
    for i in path_command:
        if i == ".":
    #        print(STATUS.good + " Path has a '.' entry")
            break
    print("")