import random

class Animail(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{} is eating {}.'format(self.name, food))

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle','Mutt'])

    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))

d =  Dog('dogname')

print(d.name)
