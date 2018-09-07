class MaxSizeList(object):

    def __init__(self, max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(0)

    def get_list(self):
        return self.innerlist


a = MaxSizeList(2)
b = MaxSizeList(2)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
