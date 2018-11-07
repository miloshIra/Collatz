# Serilization Class

import pickle

class myClass(object):

    def __init__(self, init_val):
        self.val = init_val
    def increment(self):
        self.val += 1

cc = myClass(5)
cc.increment
cc.increment

with open('file.txt', 'wb') as fh:
    pickle.dump(cc, fh)

with open('file.txt', 'rb') as fh:
    un_cc = pickle.load(fh)

print(un_cc)
print(un_cc.val)
