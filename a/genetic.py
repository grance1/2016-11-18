class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass

class Cat(Animal):
    pass
dog = Dog()
print dog.run()

cat = Cat()
print cat.run()
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
dog = Dog()
print dog.run()

cat = Cat()
print cat.run()
b = Animal()
c = Dog()


print isinstance(b, Animal)

print isinstance(c, Dog)

print isinstance(c, Animal)
b = Animal()
print isinstance(b, Dog)

def run_twice(animal):
    animal.run()
    animal.run()
print run_twice(Animal())
print run_twice(Dog())
print run_twice(Cat())
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


print run_twice(Tortoise())
