class Joe(object):
    def callme(self):
        print("calling 'callme' methoh with instance: ")
        print(self)



thisjoe = Joe()

print (thisjoe.callme())
print (thisjoe)
