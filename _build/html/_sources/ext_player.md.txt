# Extension - Player Class

```{topic} In this lesson you will:
- learn how to refactor code by consolodating existing code into a new class.
```

In this extensions tutorial, we will refactor our code to create a Player class. This will give the game a player object which we can use to add features associated with the player (health, inventory, gear, weapons etc.). The first feature we will add is the player inventory, known in our game as the backpack.

## Planning

Currently the code dealing with the backpack is held in `main.py`. Before we plan our new class, we need to look at this code an identify all relevant feature we need to incorporate. So let's look at the `main.py` from the end of the standard tutorials.

```{code-block} python
:linenos:
:emphasize-lines: 54, 82-85, 101-106, 109-114
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

You will notice that there are four places that `main.py` interacts with the player's backpack.

- **line 54** &rarr; defines the backpack variable as an empty list
- **lines 82 - 85** &rarr; checks if chosen weapon is in the backpack
- **lines 101 - 106** &rarr; adds item to backpack
- **lines 109-114** &rarr; displays the contents of the backpack

If we were to move these features to a Player class, we need to consider the nature of the four features:

- the backpack describes part of the player &rarr; attribute
- checking for weapon in backpack is an action &rarr; method
- adding an item to backpack is an action &rarr; method
- displaying the contents of the backpack is an actions &rarr; method

Therefore the class diagram would look like this:

![player class diagram](./assets/player_class_diagram.png)

Now that we have a plan. Lets implement it in our code.

## Coding

We are going to refactor this code is little chunks. That way we can regularly test to ensure we haven't introduced new bugs

### Create Player class

First we need to create the Player Class.

1. Create a new file called **player.py**. Make sure it is in the same folder as the other program files.
2. Next add the **Player** class and it's `__init__` with the code below.

```{code-block} python
:linenos:
:emphasize-lines: 1, 3, 5, 6
# player.py

class Player():
    
    def __init__(self):
        self.backpack = []
```

### Replace references to backpack

Now in **main.py** we will create a instance of the Player class by making a player object.

1. Import the Player class (code below)

```{code-block} python
:linenos:
:lineno-start: 3
:emphasize-lines: 4
from room import Room
from character import Enemy, Friend
from item import Item
from player import Player
```

2. Create a player object before the initialization of variables

```{code-block} python
:linenos:
:lineno-start: 47
:emphasize-lines: 6-7
# add items to rooms
cavern.item = chair
armoury.item = elmo
lab.item = cheese

# create player
player = Player()
```

3. **Delete** the `backback` variable in **line 58**

```{code-block} python
:linenos:
:lineno-start: 55
# initialise variables
running = True
current_room = cavern

# ----- MAIN LOOP -----
```

4. Change the `backpack` reference in the **fight** command to refer to `player.backpack`

```{code-block} python
:linenos:
:lineno-start: 81
:emphasize-lines: 6
    # fight
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in player.backpack:
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
```

5. Change the `backpack` reference in the **take** command to refer to `player.backpack`

```{code-block} python
:linenos:
:lineno-start: 102
:emphasize-lines: 4
    # take
    elif command == "take":
        if current_room.item is not None:
            player.backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
```

6. Change the `backpack` references in the **backpack** command to refer to `player.backpack`

```{code-block} python
:linenos:
:lineno-start: 110
:emphasize-lines: 3, 7
    # backpack
    elif command == "backpack":
        if player.backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in player.backpack:
                print(f"- {item.name.capitalize()}")
```

#### Test backpack replacement

That is our first block of refactoring. Time to test to ensure everything still works.

### add_item method

To create effective code we should shift all backpack related code into the **Player** class. We will start with the **add_method** that add items to the backpack.

1. In **player.py** create the `add_item` method using the code below.

```{code-block} python
:linenos:
:lineno-start: 1
:emphasize-lines: 8-10
# player.py

class Player():
    
    def __init__(self):
        self.backpack = []
        
    def add_item(self, item):
        self.backpack.append(item)
        print(f"You put {item.name} into your backpack")
```

Now we need to remove that code from **main.py**, and replace it with a call to the `add_item` method.

2. **replace** the highlighted **main.py** code below:

```{code-block} python
:linenos:
:lineno-start: 102
:emphasize-lines: 4-5
    # take
    elif command == "take":
        if current_room.item is not None:
            player.backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            print("There is nothing here to take")
```

3. with this highlighted code:

```{code-block} python
:linenos:
:lineno-start: 102
:emphasize-lines: 4
    # take
    elif command == "take":
        if current_room.item is not None:
            player.add_item(current_room.item)
            current_room.item = None
        else:
            print("There is nothing here to take")
```

#### Test add_item method

Now go and test that you can still add items to your backpack.

### display_contents method

Next we will refactor the code that displays the contents of the backpack.

1. Return to the **player.py** file
2. Add the code below to the **Player** class

```{code-block} python
:linenos:
:lineno-start: 1
:emphasize-lines: 12-18
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
```

3. Go back to **main.py**
4. **Replace** the highlighted code below:

```{code-block} python
:linenos:
:lineno-start: 109
:emphasize-lines: 3-8
    # backpack
    elif command == "backpack":
        if player.backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in player.backpack:
                print(f"- {item.name.capitalize()}")
```

5. with this code:

```{code-block} python
:linenos:
:lineno-start: 109
:emphasize-lines: 3
    # backpack
    elif command == "backpack":
        player.display_contents()
```

#### Test display_contents method

Run your code and ensure that you can still see your backpack content.

### check_item_in method

Finally we need to change the backpack interaction in the fight command, but we're going to do more than just a simple replace. We're going to change the fight section so that the backpack returns the item rather than just item.name. This will allow future extensions including weapons with damage and players and characters with hit points.

In **player.py** add the code below:

```{code-block} python
:linenos:
:lineno-start: 1
:emphasize-lines: 20 - 24
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
```

This code is different, so lets **investigate** it:

- `def check_item_in(self, item_name):` &rarr; defines the function and expects the item name (a string) to be provided.
- `for item in self.backpack:` &rarr; iterate through each item object stored in `self.backpack`
- `if item.name == item_name:` &rarr; checks if the current item's name is the same as the `item_name` provided
  - `return item` &rarr; returns the current item ending the method. Note this only happens if the names match
- `return None` &rarr; returns a `None` value to indicate that none of the items in `self.backpack` have the same name as the `item_name` provided

In **main.py** change the fight command code to the same as below. Take note of the highlighted lines.

```{code-block} python
:linenos:
:lineno-start: 81
:emphasize-lines: 4 - 7, 15
    # fight
    elif command== "fight":
        if current_room.character is not None:
            choice = input("What will you fight with? > ").lower()
            weapon = player.check_item_in(choice)
            if weapon:
                if current_room.character.fight(weapon.name):
                    current_room.character = None
                    if Enemy.num_of_enemy == 0:
                        print("You have slain the enemy. You are victorious!")
                        running = False
                else:
                    running = False
            else:
                print(f"You don't have {choice}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("There is no one here to fight")
```

Lets **investigate** those lines of code.

- `choice = input("What will you fight with? > ").lower()` &rarr; we had to change the variable name, since weapon will be used to hold the item object return from `check_item_in`
- `weapon = player.check_item_in(choice)` &rarr; if the requested item is in the back, the item object is stored in `weapon` otherwise, `None` will be stored there.
- `if weapon:` &rarr; uses the **Truthiness** of objects. If there is an item_object in `weapon` then this will equate to `True`, if `None` is stored in `weapon` then this will equate to `False`
- `if current_room.character.fight(weapon.name):` &rarr; `weapon` now stores a item object rather than a name, but the `fight` method requires a string of the item name. So we have to pass the `weapon.name` attribute.
- `print(f"You don't have {choice}")` &rarr; if the `choice` is not in the backpack, then `weapon` will be `None`, but `None` doesn't have a name attribute, so we can use the same trick we use in **line 87**. Rather we will just feedback what the user entered.

#### check_item_in test

Final test. Run your code and make sure that all the fight options work.