
import random

class myClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = myClass()
myinst.dothis()
print(myinst.rand_val)
