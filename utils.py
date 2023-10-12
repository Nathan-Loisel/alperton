# Styles
class COLOR:
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m'

class STATUS:
    info = COLOR.blue + "[-]" + COLOR.reset
    good = COLOR.green + "[+]" + COLOR.reset
    bad = COLOR.red + "[!]" + COLOR.reset

class OUTPUT_TYPE:
    alert = 1
    info = 2