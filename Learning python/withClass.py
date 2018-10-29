class myClass(object):

    def __enter__(self):                      #special magic method
        print("we have entered 'with'")
        return(self)

    def __exit__(self, type, value, traceback):      #special magic method
        print('error type: {0}'.format(type))
        print('error value: {0}'.format(value))
        print('error traceback:  {0}'.format(traceback))

    def sayhi(self):
        print('hi, instance {}'.format(id(self)))

with myClass()as cc:  # same as cc = myClass() but with useing with statment
    cc.sayhi()

print('after the "with" block')


#Used when you need to clean-up ... or close useage to network, files, memory or database connection.
# Can also handle exceptions withing the with block ??

#Read further  on Metaclasses, Newstyle classes and descriptors.
