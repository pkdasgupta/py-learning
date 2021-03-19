# Program to demonstrate File I/O in python

f = open("sample.txt", "w")

string = '''Prasanta Kumar Dasgupta
Saraswati Nagar, Chas
Boakro Steel City
Jharkhand
827013
India'''

f.writelines(string)
f.close()

with open("sample.txt") as f:
    data = f.readlines()

print(data, len(data))
