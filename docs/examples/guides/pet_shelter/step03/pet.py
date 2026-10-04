# pet.py

class Pet():

    def __init__(self, name, age):
        # initialises the pet object
        self.name = name
        self.age = age
        self.adopted = False

    def describe(self):
        # displays the pet's details
        print(f"{self.name} is {self.age} years old.")

    def speak(self):
        # the pet makes a sound
        print(f"{self.name} doesn't make a sound.")


class Dog(Pet):

    def speak(self):
        # the dog makes its sound
        print(f"{self.name} says Woof!")


class Cat(Pet):

    def speak(self):
        # the cat makes its sound
        print(f"{self.name} says Meow!")
