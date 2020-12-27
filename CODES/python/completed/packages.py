#!/usr/bin/env python3
import subprocess
import sys
import os

filename = input("Enter the filename or the path to python file: ")

packages = []
with open(filename, 'r') as f:
	for line in f.read().split('\n'):
		if 'import' in line and 'from' in line:
			packages.append(line.split()[1])
		elif 'import' in line:
			packages.append(line.split()[1])

for pack in packages:
	if pack not in sys.builtin_module_names:
		subprocess.run('pip3 install '+ pack, shell=True)
print("----------------------------------------------------------------------------")
print("Installed Packages: "+ ", ".join([i for i in packages if i not in sys.builtin_module_names]))
print("----------------------------------------------------------------------------")

