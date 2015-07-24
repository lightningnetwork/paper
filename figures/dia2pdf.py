#!/usr/bin/python

#Converts .dia files to .pdf readable by latex
#To build all files in this directory: python dia2pdf.py
#To build all files beginning with Diag: python dia2pdf.py Diag

import glob
import sys
import os
import signal

#Ctrl+C inside python
sigint = False
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    os.system("rm -f *.dia~")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def system(command):
    state = os.system(command)
    #Ctrl+C outside python
    if state == 256:
        print('You pressed Ctrl+C!')
        os.system("rm -f *.dia~")
        sys.exit(0)

#Default to everything, otherwise do everything beginning with that string
argv = "*"
if len(sys.argv) > 1:
    argv = sys.argv[1]

#Get a list of files to process
files = glob.glob("./" + argv + "*.dia")

for filename in files:
    if len(filename) > 4 and not sigint:
        print("Working on " + filename)
        system("dia -e " + filename + "~ -t eps " + filename)
        system("ps2pdf -dEPSCrop " + filename + "~ " + filename[0:-4] + ".pdf")
        system("rm -f *.dia~")
