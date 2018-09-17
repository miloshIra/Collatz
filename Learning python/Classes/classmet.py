class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

print(a.val)
print(b.val)
print(c.val)
