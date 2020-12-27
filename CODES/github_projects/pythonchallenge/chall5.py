import pickle

with open('resources/chall5.txt','rb') as file:
    data = pickle.loads(file.read())
    
for line in data:
    print("".join([k * v for k, v in line]))