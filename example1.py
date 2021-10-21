#!/usr/bin/python3

import os
import sys
from datetime import datetime

# print(str(sys.argv[1]))
# print(os.getcwd())

# echo myfilename-"`date +"%d-%m-%Y"`
# os.path.getmtime(path)

if(len(sys.argv)>1): arg = sys.argv[1]
else: raise Exception("Must pass 1 argument")


# the number of seconds since the epoch 
timestamp = os.path.getmtime(arg)

formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

print(formatted_timestamp)


