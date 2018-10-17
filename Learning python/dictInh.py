

class mydict(dict):
    def __setitem__(self, key, val):
        print("setting a key and value!")
        dict.__setitem__(self, key, val)

dd = mydict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))
