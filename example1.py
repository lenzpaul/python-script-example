#!/usr/bin/python3


"""
Place file in a folder which name is the date of last modification of file
"""

import os
import sys
from datetime import datetime
import pathlib  # python 3.5+ only



# check that at least 1 argument is passed 
if(len(sys.argv)>1): arg = sys.argv[1]
else: raise Exception("Must pass 1 argument")


# The date of last modification to file `arg`.
# timestamp is the number of seconds since the epoch 
timestamp = os.path.getmtime(arg)

formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

# create directory for date if it doesn't exist
# pathlib.Path(formatted_timestamp).mkdir(parents=True, exist_ok=True) 

# dest = formatted_timestamp + "/" + arg
# os.rename(arg, dest)

def move_files():
    directory = os.fsencode(os.getcwd())
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            # print(os.path.join(directory, filename))
            print(filename)
            continue
        else:
            continue


move_files()

