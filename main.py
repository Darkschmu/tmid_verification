#!/usr/bin/env python3

import os
import sys
import json
import traceback
import datetime
import time
import subprocess
import importlib
from pathlib import Path

def main(INPUT):
    if len(INPUT) == 3:
        if os.path.isfile(INPUT[1]):
            print("Proceeding with file 1 " + INPUT[1])
            INPUTFILE1 = INPUT[1]
        else:
            print("Invalid filename given: " + INPUT[1])
            sys.exit(2)
        if os.path.isfile(INPUT[2]):
            print("Proceeding with file 2 " + INPUT[2])
            INPUTFILE2 = INPUT[2]
        else:
            print("Invalid filename given: " + INPUT[2])
            sys.exit(2)
    elif len(INPUT) == 1:
        print("No file given, gimme two files pls")
        sys.exit(2)
    else:
        print("Error in arguments")
        sys.exit(1)

    ## Write the lists of titles and their spec files
    with open(INPUTFILE1, 'r') as f:
        input_dict1 = json.load(f)
    with open(INPUTFILE2, 'r') as f:
        input_dict2 = json.load(f)
        
    if len(input_dict1) == len(input_dict2):
        print("Both file are of equal length")
    else:
        print("Both files are not of equal length")
    
    for key in input_dict1:
        #print(key)
        if input_dict1[key] != input_dict2[key]:
            print("Key value for {0} does not match".format(str(key)))
            #print("File1: ", input_dict1[key])
            #print("File2: ", input_dict2[key])

    tranList1=input_dict1['transactionList']
    tranList2=input_dict2['transactionList']

    for key in tranList1:
        #print(key)
        #print(key['transactionId'])
        #print(key['tmid'])
        #print(tranList2[key['transactionId']])
        if key not in tranList2:
            print("Item doesnt match: ", key)
    #assert [key for key in tranList1 if key not in tranList2] == []
    res = tranList2 == tranList1
    print(res)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        print("Error")
        traceback.print_exc()
