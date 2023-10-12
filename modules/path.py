from alperton import COLORS, STATUS

def run():
    print( STATUS.info + " Checking $PATH")
    path = os.environ["PATH"]
    path = path.split(":")
    for i in path:
        if i == ".":
            print(STATUS.good + " Path has a '.' entry")
            break
    print("")