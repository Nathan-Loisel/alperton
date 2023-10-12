import os
import subprocess
from utils import COLOR, STATUS, OUTPUT_TYPE
from output import output

class mod_suid:
    def __init__(self):
        self.name = "SUID"
        self.output = output(OUTPUT_TYPE.alert)

    def run(self):
        COMMON_SUID_BINARIES = ["/bin/mount", \
                                "/bin/umount", \
                                "/bin/ping", \
                                "/bin/ping6", \
                                "/bin/su", \
                                "/usr/bin/sudo", \
                                "/usr/bin/passwd", \
                                "/usr/bin/newgrp", \
                                "/usr/bin/chsh", \
                                "/usr/bin/chfn"]
        suid = subprocess.Popen(["find", "/", "-perm", "-4000", "-type", "f"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = suid.communicate()
        suid = out.decode("utf-8").split("\n")
        suid = list(filter(None, suid))
        for i in suid:
            if i in COMMON_SUID_BINARIES:
                suid.remove(i)
        if len(suid) > 0:
            out = ""
            for i in suid:
                out += i + "\n"
            self.output.addEntry(["SUID binaries found", out])

        return self.output