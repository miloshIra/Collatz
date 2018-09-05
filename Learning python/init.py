class myNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val= value

    def incerment(self):
        self.val = self.val +1

aa=myNum('hello')
dd=myNum(100)
aa.incerment()
aa.incerment()
dd.incerment()
print(aa.val)
print(dd.val)
