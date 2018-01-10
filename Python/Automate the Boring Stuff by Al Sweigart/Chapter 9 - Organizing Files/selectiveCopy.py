#! python3
# selectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension (such as .pdf or.jpg)
#                    Copies these files from current location to new folder.

# will need shutil for copy functions, os for path and walk functions, re for identifying extensions
import shutil, os, re

def selectiveCopy(folder, ext)  # Specify the file extension and what folder is to be searched
    folder = os.path.abspath(folder)
    print("Searching files in %s for files with the %s extension..." % (folder, ext))

    searchHit = re.compile(r".*" + re.escape(ext))

# TODO: Walk specified folder tree, find files with the specified extension ignore files without using if & re, copy correct files to new folder,
    for foldername, subfolders, filenames in os.walk(folder):


        for filename in filenames:
            if filename
            print("Copied %s," % (filename))

    print("Done.")