import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir('.')
    return str(files)

# This little snippet of code defines a run function that lists all of the
# files in the current directory and returns that list as a string.
