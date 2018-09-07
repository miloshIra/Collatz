class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print ("{} eats {}".format(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print("{} goes after then {}".format(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print("{} shreds the string!".format(self.name))


r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
f.eat('puke')
r.eat('Fluffy')
r.swatstring()
