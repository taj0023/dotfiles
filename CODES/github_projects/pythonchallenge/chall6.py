import subprocess
import re

next_nothing = '90052'


while True:
    with open('resources/chall6/'+next_nothing+'.txt') as file:
        thenga = file.readline()
        unda = re.findall('[0-9]+',thenga)
        next_nothing = unda[0]
        print(next_nothing)


        ####not complete !! need to get comments from each file