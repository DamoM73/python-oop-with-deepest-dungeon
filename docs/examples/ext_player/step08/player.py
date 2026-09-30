# player.py

class Player():

    def __init__(self):
        self.backpack = []

    def add_item(self, item):
        self.backpack.append(item)
        print(f"You put {item.name} into your backpack")

    def display_contents(self):
        if self.backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in self.backpack:
                print(f"- {item.name.capitalize()}")

    def check_item_in(self, item_name):
        for item in self.backpack:
            if item.name == item_name:
                return item
        return None
