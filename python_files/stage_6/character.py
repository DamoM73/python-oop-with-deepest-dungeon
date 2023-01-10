class Character():
    
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None
        
    def describe(self):
        # sends a description of the character to the terminal
        print(f"{self.name} is here, {self.description}")
        
    def talk(self):
        # send converstation to the terminal
        if self.conversation is not None:
            print(f"{self.name}: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")
    
    def hug(self):
        # the character responds to a hug
        print(f"{self.name} doesn't want to hug you")

    def fight(self,item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
        return True
        
class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)
        
    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")
        
class Enemy(Character):
    
    def __init(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        
    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
        
        