import os

class ConfigDict(dict):

    def __init__(self, filename):

        self._filename = filename                 #FILE DOESNT EXIST ?
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write('{0}={1}'\n'.format(key, val))

    def __getitem__(self, key):
    ....                                            # assaiment for later!!
            raise ConfigKeyError(self, key)

cd = ConfigDict('path/to/somefile.txt')

print(cd['nonexistant_key'])
