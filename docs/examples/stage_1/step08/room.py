# room.py

class Room():

    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}

    def describe(self):
        # displays a description of the room in the UI
        print(f"\nYou are in the {self.name}")
        print(self.description)

    def link_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
