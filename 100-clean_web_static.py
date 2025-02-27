#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["54.172.219.93", "54.237.102.1"]


def do_clean(number=0):
    """Delete out-of-date archives,,
    Args:
        no. (int): The no. of archives to keep,,
    If number is 0 or 1, keeps only the most recent archive. If
    no is 2, keeps most and second-most recent archives,
    etc,,
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
