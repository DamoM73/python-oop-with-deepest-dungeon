class Item():
    
    def __init__(self,name):
        # initialise the Item object
        self.name = name.lower()
        self.description = None
        
    def describe(self):
        # prints description of item to the terminal
        print(f"You see {self.name} in the room. It is {self.description}.")