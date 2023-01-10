from room import Room
from character import Enemy, Friend
from item import Item

# create rooms
cavern = Room("Cavern")
cavern.description = ("A room so big that the light of your torch doesn’t reach the walls.")

armoury = Room("Armoury")
armoury.description = ("The walls are lined with racks that once held weapons and armour.")

lab = Room("Laboratory")
lab.description = ("A strange odour hangs in a room filled with unknownable contraptions.")

# link rooms
cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
lab.link_rooms(armoury,"west")

# create characters
ugine = Enemy("Ugine")
ugine.description = "a huge troll with rotting teeth."
ugine.weakness = "cheese"

nigel = Friend("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.inhabitant = ugine
lab.inhabitant = nigel

# create items
cheese = Item("Cheese")
cheese.description = "super smelly"

chair = Item("Chair")
chair.description = "designed to be sat on"

elmo = Item("Elmo")
elmo.description = "wanting to be tickled"

# add items to rooms
cavern.item = chair
armoury.item = elmo
lab.item = cheese

# initialise variables
running = True
current_room = cavern
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    # move
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        print(f"You travel {command}")
    # talk
    elif command == "talk":
        if current_room.inhabitant is not None:
            current_room.inhabitant.talk()
        else:
            print("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.inhabitant is not None:
            current_room.inhabitant.hug()
        else:
            print("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.inhabitant.fight(weapon):
                    current_room.inhabitant = None
                    if Enemy.num_of_enemy == 0:
                        print("You have slain the enemy. You are victorious!")
                        running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.inhabitant.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
    # take
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
    # backpack
    elif command == "backpack":
        if backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
    # help
    elif command == "help":
        print("Type which direction you wish to move,")
        print("or use one of these commands:")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
    # quit
    elif command == "quit":
        running = False
    # incorrect command
    else:
        print("Enter 'help' for list of commands")
    input("\nPress <Enter> to continue")
    
print("Thank you for playing Darkest Dungeon")