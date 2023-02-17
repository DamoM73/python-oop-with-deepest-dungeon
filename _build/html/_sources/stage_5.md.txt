# Stage 5 - Item Creation

```{topic} In this lesson you will:

- Create items
- Add the items to their room
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/jYSs_-wY8ys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

Now our dungeon is starting to take shape. The user can move between multiple rooms in which they can interact with different characters. We have two different types of characters, with different user interactions.

In this stage we will continue to fill out our dungeon. Most Dungeon crawlers will contain different items that the player can interact with, so let's create some items.

To achieve this we will:

- Define an Item class
- Create Item objects
- Add the Item objects to the rooms
- Include the Item objects in the room description.

### Class Diagram

The new class diagram shows our new Items class, as well as the new item attribute in our Room class.

![lesson 5 class diagram](./assets/lesson_5_class_diagram.png)

## Define the Item class

In Thonny create a new file and enter the code below. Then save it as **item.py** in the same folder as **main.py**, **character.py** and **room.py**.

```{code-block} python
:linenos:
:emphasize-lines: 1, 3, 5-8
# item.py

class Item():
    
    def __init__(self,name):
        # initialise the Item object
        self.name = name.lower()
        self.description = None
```

In investigating the code everything should be familiar:

- defining the `Item` class
- defining our `__init__` method
- assigning the `name` argument to the `self.name` attribute
- creating a placeholder `self.description` attribute to be assigned a value later

## Create Item objects

To create the Item objects, move to the **main.py** file and add the code below:

```{code-block} python
:linenos:
:emphasize-lines: 5, 36-38, 40-41, 43-44
# main.py

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

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''

# initialise variables
running = True
current_room = cavern

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.inhabitant is not None:
            current_room.inhabitant.talk()
        else:
            print("There is no one here to talk to")
    elif command == "hug":
        if current_room.inhabitant is not None:
            current_room.inhabitant.hug()
        else:
            print("There is no one here to hug")
    elif command== "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
                running = False
        else:
            print("There is no one here to fight")
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

**Predict** what you think will happen and **run** the code.

Again, in investigating the code this should all be familiar.

For each of the items, we have:

- imported our new class (Item)
- called `Item()` to create a Item object and then assigned it to a variable
- assigned a string to the Item object's  `description` attribute

## Add the item object to the the rooms.

To add the Item objects to the rooms, we need to first adjust the `Room` class, so go to **room.py** and add the code below.

```{code-block} python
:linenos:
:emphasize-lines: 11
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
    def describe(self):
        # sends a description of the room to the terminal
        print(f"\nYou are in the {self.name}")
        print(self.description)
        if self.character is not None:
            self.character.describe()
        for direction in self.linked_rooms.keys():
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")
    
    def link_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
        
    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
```

Save the **room.py** file and then return to the **main.py** file, add the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 46-49
# main.py

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

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''

# initialise variables
running = True
current_room = cavern

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.inhabitant is not None:
            current_room.inhabitant.talk()
        else:
            print("There is no one here to talk to")
    elif command == "hug":
        if current_room.inhabitant is not None:
            current_room.inhabitant.hug()
        else:
            print("There is no one here to hug")
    elif command== "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
                running = False
        else:
            print("There is no one here to fight")
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

**Predict** what you think will happen and then **run** the program.

Investigating this code, and it will all look familiar to you.

For each item we assigned it to the `item` attribute of a Room object.

## Include the Item objects in the room description

Despite writing all this code, your program *should* run the same as when we started. That's because none of these changes have been outputted. For the Item objects we are going to follow the same process that we did for the Character objects:

- create a `describe` method in the `Item` class
- call the Item `describe` method from the Room `describe` method

First we need to go to the **item.py** file and add the code below:

```{code-block} python
:linenos:
:emphasize-lines: 10-12
# item.py

class Item():
    
    def __init__(self,name):
        # initialise the Item object
        self.name = name.lower()
        self.description = None

    def describe(self):
        # prints description of item to the terminal
        print(f"You see {self.name} in the room. It is {self.description}.")    
```

In investing this code, you should already recognise all the elements:

- defining method
- method describing comment
- display to terminal using attributes of the object.

Now head to **room.py** and add the following code:

```{code-block} python
:linenos:
:emphasize-lines: 17-18
class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
    def describe(self):
        # sends a description of the room to the terminal
        print(f"\nYou are in the {self.name}")
        print(self.description)
        if self.inhabitant is not None:
            self.inhabitant.describe()
        if self.item is not None:
            self.item.describe()
        for direction in self.linked_rooms.keys():
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")
    
    def link_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
        
    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
```

**Predict** and **run** the code. 

**Investigate** the code and you will notice that it is very similar to the character description:

- check if there is an item in the room
- when an item is present, call it's describe method.

Go a step further and test the code by going to each room and checking that the correct item is displayed.

| Room | Item expected | Item described |
| :--- | :------------ | :------------- |
| Cavern | chair | |
| Armoury | elmo | |
| Lab | cheese | |

## Stage 5 task

Now it is time for your to implement the **Make** phase.

You should:

- make an additional item for each of your additional rooms
- add your additional items to their room.