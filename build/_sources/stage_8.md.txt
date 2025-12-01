# Stage 8 - Useability

```{topic} Learning Intentions
In this lesson you will:
* understand why making something easy to use is important for the person using it
* know what UI and UX mean and why they matter when people use a program
* understand how comments and neat code make a program easier to read and fix
* improve a program by adding features that help the user, like a help option or clearer messages
* tidy up a program by removing code you don’t need and organising it so it’s easier to read and use
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lHSCfn0U45k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

Our dungeon works, but before we finish we need to make it easier to use and clean up the code.

We will:

```{admonition} Pseudocode
:class: pseudocode
* add a **help** command
* make the program easier to read and use
* add a goodbye message at the end
* write more comments in the code
* delete code we don’t need
* make our spacing neat and consistent
```

## Help command

We know the commands because we wrote the code. A new player won’t know what they’re allowed to type. Right now, if they type something wrong, the program just says “I don’t understand,” which isn’t very helpful.

To fix this, we should add a **help** command that shows all the commands. But players won’t know the help command exists unless we tell them. So we update the final `else:` section to remind them to type “help” when they get something wrong.

Now add the highlighted code to ***main.py***.

```{code-block} python
:linenos:
:emphasize-lines: 117-124, 128
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
armoury.character = ugine
lab.character = nigel

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
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    cif isinstance(current_room.character, Enemy):
                        current_room.character = None
                        if Enemy.get_num_of_enemy() == 0:
                            print("You have slain all the enemies. You are victorious!")
                            running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
    elif command == "backpack":
        if backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
    elif command == "help":
        print("Type which direction you wish to move,")
        print("or use one of these commands:")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
    elif command == "quit":
        running = False
    else:
        print("Enter 'help' to list the copmmands.")
```

You’ve seen this kind of code many times now, so you should already understand how it works without investigating it.

## Improving the UI and UX

Even though our program looks simple, people still have to use it, so we need to think about the UI and UX &mdash; how it looks and how easy it is to use.


```{admonition} UI and UX
:class: note
UI means **User Interface**. It’s the stuff you actually see on the screen when you use an app or website — things like buttons, menus, icons, and colours. UI is about making everything look clear and easy to use.

UX means **User Experience**. It’s about what it *feels* like to use the app — if it’s easy, confusing, fun, or annoying. UX is about making sure the user has a smooth and enjoyable time using the program.
```

We’ve already fixed some UI and UX issues by adding the **help** command. Now play the game and see if you can spot anything else that feels confusing.

You might notice that after you type a command, the game shows the response and then instantly prints the room description again. This makes it easy to miss what the game just told you. To fix that, we’ll show the response and then make the user press a key before the game continues.

To do this, add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 129
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
armoury.character = ugine
lab.character = nigel

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
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    if isinstance(current_room.character, Enemy):
                        current_room.character = None
                        if Enemy.get_num_of_enemy() == 0:
                            print("You have slain all the enemies. You are victorious!")
                            running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
    elif command == "backpack":
        if backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
    elif command == "help":
        print("Type which direction you wish to move,")
        print("or use one of these commands:")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
    elif command == "quit":
        running = False
    else:
        print("Enter 'help' to list the copmmands.")
    input("\nPress <Enter> key to continue")
```

Save the file, **predict** and then **run** the code.

How does that work? Let's **investigate**:

```{admonition} Code Explaination
* `input("\nPress <Enter> key to continue")` is basically a little trick. We’re using `input` in a way it’s not normally meant to be used.
  * Normally, `input` waits for the user to type something, which is why it pauses the game.
  * The user presses **Enter** to continue, which ends the pause.
  * We don’t save what the user types, so whatever they enter is ignored and disappears.
```

## Farewell message

When the game ends, it just shuts off straight away. No message, even if you win or lose. To make the ending feel a bit nicer, we should add a goodbye message.

Add the highlighted code below to include the farewell message.

```{code-block} python
:linenos:
:emphasize-lines: 130
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
armoury.character = ugine
lab.character = nigel

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
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    if isinstance(current_room.character, Enemy):
                        current_room.character = None
                        if Enemy.get_num_of_enemy() == 0:
                            print("You have slain all the enemies. You are victorious!")
                            running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
    elif command == "backpack":
        if backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
    elif command == "help":
        print("Type which direction you wish to move,")
        print("or use one of these commands:")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
    elif command == "quit":
        running = False
    else:
        print("Enter 'help' to list the copmmands.")
    input("\nPress <Enter> key to continue")
print("Thank you for playing Deepest Dungeon")
```

## In-code comments

We already have a few comments in the code to help explain what parts do, but most of the main loop doesn’t have any. Adding comments there will make the code easier to read and easier to fix later.


```{admonition} Code maintainability
:class: note
Code maintainability means making your code easy to understand, fix, and update later. If your code is neat, well-organised, and has clear comments, you or someone else can quickly figure out how it works. This makes it easier to find bugs, add new features, and change things without breaking the program.
```

Let's first start with ***main.py***

```{code-block} python
:linenos:
:emphasize-lines: 70, 73, 79, 85, 107, 115, 123, 132, 135
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
armoury.character = ugine
lab.character = nigel

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
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    # move
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    # talk    
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    if isinstance(current_room.character, Enemy):
                        current_room.character = None
                        if Enemy.get_num_of_enemy() == 0:
                            print("You have slain all the enemies. You are victorious!")
                            running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
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
        print("Enter 'help' to list the copmmands.")
    input("\nPress <Enter> key to continue")
print("Thank you for playing Deepest Dungeon")
```

When you make classes, it’s a good idea to add a comment explaining what each method does. If you check the classes in ***room.py***, ***item.py***, and ***character.py***, you’ll see we’ve already done this there.

## Remove unused code

Remember the code in ***main.py*** that we commented out. Well we no longer need it. Go ahead and **delete** the code highlighted below.

```{code-block} python
:linenos:
:emphasize-lines: 52-57
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
armoury.character = ugine
lab.character = nigel

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
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    # move
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    # talk    
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                    if Enemy.get_num_of_enemy() == 0:
                        print("You have slain all the enemies. You are victorious!")
                        running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
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
        print("Enter 'help' to list the copmmands.")
    input("\nPress <Enter> key to continue")
print("Thank you for playing Deepest Dungeon")
```

## Final code

Whitespace is the empty lines in your code. You can use it to break your code into clear sections and make it easier to read.

Finalise your code by adjusting it so to look the same as the following code:

### ***main.py***

```{code-block} python
:linenos:
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
armoury.character = ugine
lab.character = nigel

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
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is no one here to talk to")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                    if Enemy.num_of_enemy == 0:
                        print("You have slain the enemy. You are victorious!")
                        running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
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
```

### ***room.py***

```{code-block} python
:linenos:
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
        if self.item is not None:
            self.item.describe()
        for direction in self.linked_rooms.keys():
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")
    
    def link_rooms(self, room, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room
        
    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
```

### ***character.py***

```{code-block} python
:linenos:
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
    
    num_of_enemy = 0
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        Enemy.num_of_enemy += 1
        
    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            Enemy.num_of_enemy -= 1
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
    
    def get_num_of_enemy():
        return Enemy.num_of_enemy
```

### ***item.py***

```{code-block} python
:linenos:
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

## Final Make

The tutorials are finished. Now it’s your turn to make the dungeon your own by adding new features. You can check the Extension Ideas page for inspiration.

There are a few logic mistakes in the code, but you’ll need to test the game to find them and work out how to fix them. Make sure you use your debugger to help.

Good luck on your adventure.

