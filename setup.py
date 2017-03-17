#!/usr/bin/env python

import os

os.system("mkdir /opt/elpscrk")
print "[+] Creating file directories..."
os.system("mv elpscrk.py /opt/elpscrk/elpscrk.py")
print "[+] Configuring the file..."
os.system("chmod 777 /opt/elpscrk/elpscrk.py")
print "[+] Giving the necessary permissions to the file..."
fl = open(os.path.expanduser('~')+"/.bashrc", "a")
print "[+] Creating terminal shortcut..."
fl.write("alias elpscrk='/opt/elpscrk/elpscrk.py'")
print "[+] Successfully installed..."
