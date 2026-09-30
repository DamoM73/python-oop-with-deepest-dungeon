# player.py

class Player():

    def __init__(self):
        self.backpack = []

    def add_item(self, item):
        self.backpack.append(item)
        print(f"You put {item.name} into your backpack")
