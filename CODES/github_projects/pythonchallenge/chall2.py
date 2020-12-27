from collections import Counter


with open('resources/chall2.txt', 'r') as file:
    content = file.read()
    thenga = Counter(content)
    for key in thenga.keys():
        print(key, end = '')


