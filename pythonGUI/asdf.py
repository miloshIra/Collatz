import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0
    def set_val(self, value):
        self.val = value
    def get_val(self):
        return self.val
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)
    def showdoc(self):
        print('GetSetInt object ({0}), only accept' 'integer valies'.format(id(self)))

# x = GetSetInt(3)
# x.set_val(5)
# print(x.get_val())
# x.showdoc()

class GetSetList(GetSetParent):
    def __init__(self, value = 0):
        self.vallist = [ value ]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print('GetSetList object, len {0}, stores''history of value set'.format(len(self.vallist)))

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()
