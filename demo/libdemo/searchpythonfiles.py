# Search for python files where filename contains the given string
import os
import sys

if len(sys.argv) < 2:
    print("Usage : python searchpythonfiles.py  <searchstring> [startdirectory]")
    sys.exit(1)

searchstring = sys.argv[1]  # Search string
if len(sys.argv) > 2:
    startdir = sys.argv[2]  # Starting directory
else:
    startdir = os.getcwd()  # Start directory is current directory

allfiles = os.walk(startdir)

for (dirname, folders, files) in allfiles:
    for file in files:
        if file.endswith(".py") and file.find(searchstring) >= 0:  # Found string in filename
            print(dirname + "\\" + file)
