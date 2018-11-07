# Object serialization  .. storage of python objects
# Using picle for dumping and loading


import pickle

list = ['a', 'b', 'c', 'z']

with open('Ser.txt', 'wb') as fh:
    pickle.dump(list, fh)

# Dumping into ser.txt file

with open('Ser.txt', 'rb') as fh:
    unpicklist = pickle.load(fh)

print (unpicklist)

# Reading from ser.txt file
int = 55
str = 'nice string bruh'

dict_of_list = { 'a': [1,2,3], 'b': [4,5,6]}

qr = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]

with open('datafile.txt', 'wb') as fh:
    pickle.dump((int, str, dict_of_list, qr), fh)

with open('datafile.txt', 'rb') as fh:
    tup = pickle.load(fh)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
