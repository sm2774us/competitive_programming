#!/usr/bin/env python

import os

if __name__ == "__main__":
    # working_dir = os.getcwd()
    working_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = "."
    # Use a one-line list comprehension to get all the files in a given directory with a given file basename.
    res = [
        os.path.join(dp, f)
        for dp, dn, filenames in os.walk(root_dir)
        for f in filenames
        if os.path.basename(f) == "test.py"
    ]
    # res = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and os.path.basename(f) == "test.py"]
    # os.path.join joins a directory and a filename into a path. You can also split a path name into directory and file with
    # os.path.split(), and you can split a filename with extension into filename and extension with os.path.splitext()
    # os.path.expandUser() will expand '~' to the absolute path of the current user's home directory on Windows, Linux or Mac
    # The rest of the os.path module:
    # http://docs.python.org/lib/module-os.path.html
    for f in res:
        # print("python ", os.path.join(root_dir, f))
        print("Running test case(s) for the directory: " + os.path.dirname(f))
        os.chdir(os.path.dirname(os.path.realpath(f)))
        print("Changed the working directory to " + os.getcwd())
        os.system("python " + os.path.join(os.path.basename(f)))
        os.chdir(working_dir)
        print("Changed the working directory back to " + working_dir)
