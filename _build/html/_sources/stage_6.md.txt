# Stage 6 - Use Items

```{topic} In this lesson you will:

- Take an items
- Create a backpack to place items
- Limit weapons to items in dungeon
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/JsUGdNxLlLM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

OU game is progressing nicely. They player can move between multiple rooms, interact with different types of characters. We also have different items in these room.

The next step is to allow the player to collect the items and use them.

To achieve this we will:

- create a backpack variable that can store items
- add a take command that collects the items
- add a backpack command to list the items in the backpack
- restrict the fight weapon to items in the backpack

### Class Diagram

If we look at the class diagram, we notice that there are no changes. All of the changes in this section will be made in the **main.py** file, and will not involve adjusting any classes.

![lesson 6 class diagram](./assets/lesson_5_class_diagram.png)

## Creating a backpack

The first thing we need to create is a backpack variable, so we can store the items we collect. To achieve this, we need a variable type that can hold multiple values. In Python these are called **collections**. We will be using **lists**, a type of **collection** that you will be familiar with.

```{admonition} Collections in Python
In Python, a collection is a way to group things together. There are different types of collections like lists, sets, and dictionaries. You can use them to store a bunch of values or items, like a shopping list or a list of names. Each type of collection has different rules and ways to use it. By choosing the right type of collection for what you need, it can help you write better code that works faster and is easier to read.

Python has following collections built it:

- **Lists:** ordered collections of values, which can be of any data type. They are created using square brackets [] and values are separated by commas.
- **Tuples:** similar to lists, but they are immutable, which means that their values cannot be changed after they are created. They are created using parentheses () and values are separated by commas.
- **Sets:** unordered collections of unique values. They are created using curly braces {} or the set() constructor.
- **Dictionaries:** unordered collections of key-value pairs. They are created using curly braces {} and key-value pairs are separated by commas, with a colon : between the key and value.

It also has modules to support other collections:

- **Arrays:** used to store a sequence of values of the same data type. They are created using the array module.
- **Queues:** data structures that use a first-in, first-out (FIFO) method to store and retrieve data. They are implemented using the queue module.
- **Stacks:** Stacks are data structures that use a last-in, first-out (LIFO) method to store and retrieve data. They are implemented using the stack module.
```

Lists are the perfect collection for our purposed. It can start as empty and we can then use the `append()` method to add items as they are picked up by the user. We can also check if out backpack contains an item using the `in` operator. We can access the time using list indexation, as well as using `pop` to remove the item from the backpack. So let's create it.

Open **main.py** and add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 61
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
backpack = []

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
    elif command == "fight":
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

We don't need to **investigate** this line of code, as we all know what it does.

## Add take command

Now that we have a backpack we need to create a command that allows the user to pick up items in the room and place them in the backpack. We will use **take** as that command.

Still working in **main.py** add the take command using the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 90-96
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
backpack = []

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
    elif command == "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
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
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

Save **main.py** **predict** what you think will happen and then **run** the code. What happens to the room description after you take an item?

In **investigating** this code, most of it should be familiar from our previous command event handlers. The different code is:

- `backpack.append(current_room.item)` &rarr; take the `Item` object in the room and adds it to the end of the `backpack` list.
- `print(f"You put {current_room.item.name} into your backpack")` &rarr; informs the user that they have collected the item
- `current_room.item = None` &rarr; removes the `Item` object from the room by setting the `Room` object's `item` attribute to `None`

## Add backpack command

Now that we are putting items in the backpack, we need to create a way for the user to see what they have. We will make a new **backpack** command that lists the `Item` objects stored in their backpack.

Still working in **main.py**, add the code below:

```{code-block} python
:linenos:
:emphasize-lines: 97-103
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
backpack = []

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
    elif command == "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
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
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

Save the **main.py** file, **predict** and then **run** your code. This time we should do some serious testing.

We need to make sure that:

- we can pick up all the items in all the rooms
- the items are added to the backpack when they are picked up
- the items are removed from the room when they are picked up

If your testing all works out, then it's time to **investigate** the code.

- `elif command == "backpack":` &rarr; the event handler for the `backpack` command
- `if backpack == []:` &rarr; checks if the backpack is empty
- `print("It is empty")` &rarr; informs the user that the backpack is empty
- `else:` &rarr; if the backpack is not empty
- `print("You have:")` &rarr; displays a message before listing backpack items
- `for item in backpack:` &rarr; iterates over each item in the backpack
- `print(f"- {item.name.capitalize()}")` &rarr; capitalizes and prints the name of the current `item` that the `for` loop is dealing with.

## Adjusting the fight command

Finally we will adjust the `fight` event handler so the user can only use items they currently have in their backpack.

Still working in **main.py**, add the code below.

```{code-block} python
:linenos:
:emphasize-lines: 84-95
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
backpack = []

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
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
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
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

Save **main.py**. **Predict** what you think will happen, and then **run** the code.

Let's **investigate** that code, but be aware that there are a number of different sections to that code.

First we need to check that the user actually has the entered weapon in their backpack.

- `available_weapons = []` &rarr; creates a new list that contains the `name` attribute for all items in the backpack.
  - the backpack stored `Item` objects
  - the user entered the item name as a string
  - therefore, we need to create a list of the name of all the items in the backpack
- `for item in backpack:` &rarr; iterates over each item in the backpack
- `available_weapons.append(item.name)` &rarr; add the `name` attribute of the current item to the `available_weapons` list.
- `if weapon in available_weapons:` &rarr; checks that the weapon entered by the user is in the list of available weapons.
  
If the user entered an available weapon, then we need to fight with this weapon. Lines `88` to `91` are the same as before, but the have been indented one level. To to this easily increase a block of code's indentation:

- highlight lines `88` to `91`, ether using the mouse or **shift** + **arrow** keys.
- then press the **Tab** key once

If the user didn't enter an available weapon, then we need to inform them, then make them loose the fight and end the game. This happens in lines `92` to `95`

- `else:` &rarr; the weapon entered is not in the `available_weapons` list
- `print(f"You don't have {weapon}")` &rarr; inform the user that they do not have that item in the backpack
- `print(f"{current_room.character.name} strikes you down.")` &rarr; resolves the fight as a defeat for the user
- `running = False` ends the game by exiting the main loop.

## Testing

We now need to test our code. This code now has nested branches of if statements so we have to be aware of testing all the possible options. We will test with Ugine as we know his weakness is cheese. 

| Collected Cheese | Fought Ugine | Weapon Used | Expected Result | Actual Result |
| :--------------- | :----------- | :---------- | :-------------- | :------------ |
| Yes | Yes | Cheese | You strike Ugine down with cheese. | |
| Yes | Yes | Elmo | Ugine crushes you. Puny adventurer | |
| No | Yes | Cheese | You don't have cheese... | |

If your code passes all the tests, it's time to **make** some code in the stage 6 task.

## Stage 6 task

You need to apply the changes we made to your other characters. Especially if you have another enemy. Make sure that the user can collect their weakness and use it against them.
