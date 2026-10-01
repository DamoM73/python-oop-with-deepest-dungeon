# character.py

class Character():

    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None

    def describe(self):
        # sends a description of the character to the terminal
        print(f"{self.name} is here, {self.description}")
