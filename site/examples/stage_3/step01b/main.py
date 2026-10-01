# main.py

from room import Room
from character import Character

# create rooms
cavern = Room("Cavern")
cavern.description = ("A room so big that the light of your torch doesn’t reach the walls.")

armoury = Room("Armoury")
armoury.description = ("The walls are lined with racks that once held weapons and armour.")

lab = Room("Laboratory")
lab.description = ("A strange odour hangs in a room filled with unknowable contraptions.")

# link rooms
cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
lab.link_rooms(armoury,"west")

# create characters
ugine = Character("Ugine")
ugine.description = "a huge troll with rotting teeth."

nigel = Character("Nigel")
nigel.description = "a burly dwarf with golden beads woven through his beard."
nigel.conversation = "Well youngun, what are you doing here?"

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''
