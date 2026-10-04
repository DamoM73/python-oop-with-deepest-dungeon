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
