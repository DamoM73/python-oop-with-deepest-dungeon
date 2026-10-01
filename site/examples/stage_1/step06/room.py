# room.py

class Room():

    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None

    def describe(self):
        # displays a description of the room in the UI
        print(f"\nYou are in the {self.name}")
        print(self.description)
