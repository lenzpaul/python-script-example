#!/usr/bin/python3


"""
For each file with .txt extension in this directory, move the file to subdirectory 
which name is the date of last modification to the file.
"""

import os
from datetime import datetime
import pathlib  # python 3.5+ only

# Loop through files in current directory. 
# If files has .txt extensions, move file
def move_files():
    directory = os.fsencode(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            # The date of last modification to file `arg`.
            # timestamp is the number of seconds since the epoch 
            timestamp = os.path.getmtime(filename)

            # Formating the timestamp as YYYY-MM-DD
            formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            
            # create directory for date if it doesn't exist
            pathlib.Path(formatted_timestamp).mkdir(parents=True, exist_ok=True) 

            # Move the file to  `formatted_timestamp/filename` sub directory
            dest = formatted_timestamp + "/" + filename
            os.rename(filename, dest)

            continue
        else:
            continue


move_files()

