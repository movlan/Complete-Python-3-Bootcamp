class Sample():
    pass


# my_sample = Sample()

# print(type(my_sample))
# print(type(Sample))


# class Dog():

#     # CLASS OBJECT ATTRIBUTE
#     # SAME FOR ANY INSTANCE OF A CLASS
#     species = 'mammal'

#     def __init__(self, breed, name, spots):
#         # Attributes
#         # We take in the argument
#         # Assign it using self.attribute_name
#         self.breed = breed
#         self.name = name

#         # Expect boolean
#         self.spots = spots

#     # OPERATIONS / ACTIONS ----> Methods
#     def bark(self, number):
#         print(f'WOOF! My name is {self.name},and number is {number}')


# my_dog = Dog('Lab', 'Frankie', False)

# print(my_dog.breed)
# print(my_dog.species)
# print(my_dog.name)
# print(my_dog.bark(42))


class Circle():

    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # methods
    def get_circumference(self):
        return self.radius * self.pi * 2


# my_circle = Circle(12)
# print(my_circle.radius)
# print(my_circle.get_circumference())
# print(my_circle.pi)


class Animal():

    def __init__(self) -> None:
        print("Animal created")

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError(
            'Subclass must implement this abstract method')


# my_animal = Animal()

# print(my_animal.eat())
# print(my_animal.who_am_i())


class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


# niko = Dog('niko')
# felix = Cat('felix')

# print(niko.speak())
# print(felix.speak())


# Dunder methods in class

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages


b = Book('Python rocks', 'Jose', 200)

print(b)
print(len(b))
