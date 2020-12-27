import re

with open('resources/chall3.txt', 'r') as file:
    content = file.read()
    thenga = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', content)
    print(thenga)