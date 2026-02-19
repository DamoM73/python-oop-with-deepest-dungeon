# Extension - Player Class

```{topic} In this lesson you will:
* understand why grouping related features into a single class makes a program easier to manage 
* recognise how attributes and methods represent a thing’s data and actions
* identify when code should be moved out of one place and into a class during refactoring
* understand how objects can interact by calling each other’s methods
* create a simple class with attributes and methods, then use it in a program to replace repeated code 
```

In this tutorial, you’ll reorganise your code by making a **Player** class. This will give you a player object that can hold all the player’s features, like health, items, gear, and weapons. The first thing you’ll add is the player’s inventory, which we call the backpack.

## Planning

Right now, all the backpack code is written inside ***main.py***. Before we create our new Player class, we need to look at that code and figure out which parts should be moved into the class. So we’ll start by checking the ***main.py*** file from the end of the earlier tutorials.

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

You will notice that there are four places that ***main.py*** interacts with the player's backpack.

1. **line 54** &rarr; defines the backpack variable as an empty list
2. **lines 82 - 85** &rarr; checks if chosen weapon is in the backpack
3. **lines 101 - 106** &rarr; adds item to backpack
4. **lines 109-114** &rarr; displays the contents of the backpack

If we were to move these features to a Player class, we need to consider the nature of the four features:

1. the backpack describes part of the player &rarr; attribute
2. checking for weapon in backpack is an action &rarr; method
3. adding an item to backpack is an action &rarr; method
4. displaying the contents of the backpack is an actions &rarr; method

Therefore the class diagram would look like this:

![player class diagram](./assets/player_class_diagram.png)

Now that we have a plan. Lets implement it in our code.

## Coding

We’re going to update this code in small steps. This makes it easier to test as we go and check that we haven’t accidentally created any new bugs.

### Create Player class

First, we need to make the Player class.

1. Create a new file called ***player.py*** in the same folder as your other files.
2. Add the **Player** class and its `__init__` method using the code shown below.

```{code-block} python
:linenos:
:emphasize-lines: 1, 3, 5, 6
# player.py

class Player():
    
    def __init__(self):
        self.backpack = []
```

### Replace references to backpack

Now in ***main.py***, we’re going to make a player object so we can use the Player class in our program.

1. Import the Player class using the code shown below.

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

3. Delete the `backpack` variable on **line 58**.

```{code-block} python
:linenos:
:lineno-start: 55
# initialise variables
running = True
current_room = cavern

# ----- MAIN LOOP -----
```

4. Change the `backpack` in the **fight** command so it uses `player.backpack` instead.

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

5. Change the `backpack` in the **take** command so it uses `player.backpack` instead.

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

6. Change the `backpack` in the **backpack** command so it uses `player.backpack` instead.

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

That’s the first section of our code changes done. Now test your program to make sure everything still works.

### add_item method

To make our code cleaner, we should move all the backpack code into the **Player** class. We’ll start by adding the **add_item** method, which puts items into the backpack.

1. In ***player.py***, create the `add_item` method using the code below.

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

Now we need to take that code out of ***main.py*** and replace it with a call to the `add_item` method.

2. Remove the highlighted code in ***main.py*** shown below:

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

3. And replace it with this highlighted code:

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

Now test your program to make sure you can still add items to your backpack.

### display_contents method

Next, we’ll update the code that shows what’s inside the backpack.

1. Go back to the ***player.py*** file.
2. Add the code below to the **Player** class.

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

3. Go back to ***main.py***
4. Remove the highlighted code shown below:

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

5. And replace it with this highlighted code:

```{code-block} python
:linenos:
:lineno-start: 109
:emphasize-lines: 3
    # backpack
    elif command == "backpack":
        player.display_contents()
```

#### Test display_contents method

Run your program and check that you can still see everything inside your backpack.

### check_item_in method

Finally, we need to change how the fight command uses the backpack, and this time it’s more than a simple swap. We’re going to update the fight code so the backpack gives us the whole item, not just `item.name`. This will make it easier later to add things like weapon damage and health points for players and characters.

In ***player.py*** add the code below:

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

```{admonition} Code Explaination
* `def check_item_in(self, item_name):` sets up the function and expects you to give it the item’s name as a string.
* `for item in self.backpack:` goes through every item object in the backpack.
* `if item.name == item_name:` checks if the current item’s name matches the name you typed.
  * `return item` sends back that item and ends the function. This only happens when the names match.
* `return None` sends back `None` if no item in the backpack has the same name as what you typed.
```

In ***main.py***, change the fight command so it matches the code shown below. Pay attention to the highlighted lines.

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

```{admonition} Code Explaination
* `choice = input("What will you fight with? > ").lower()` → we changed the variable name because `weapon` will now store the actual item object returned from `check_item_in`.
* `weapon = player.check_item_in(choice)` → if the item is in the backpack, `weapon` will hold the item object. If not, `weapon` will be `None`.
* `if weapon:` → this checks if `weapon` is a real item object. If it is, this is `True`. If it’s `None`, it’s `False`.
* `if current_room.character.fight(weapon.name):` → `weapon` now has the whole item object, not just the name, but the `fight` method still needs a string, so we use `weapon.name`.
* `print(f"You don't have {choice}")` → if the item isn’t in the backpack, `weapon` is `None`, which doesn’t have a name. So instead, we just print whatever the player typed.
```

#### check_item_in test

Final test: run your program and check that all the different fight options still work properly.


