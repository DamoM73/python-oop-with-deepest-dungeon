# Stage 6 - Use Items

```{topic} Learning Intentions
In this lesson you will:
* understand why a list is a suitable way to store multiple pieces of data
* explain how user commands can trigger different branches of code
* describe how different objects interact through attributes and methods
* create and update a list in Python to store and manage items
* implement new commands that use lists to control what actions are allowed
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/JsUGdNxLlLM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

Our game is coming along well. You can move around, meet different characters, and find items in the rooms.

Now we want the player to pick up items and actually use them.

To do this we will:

```{admonition} Pseudocode
:class: pseudocode
* make a backpack variable to hold the items you collect
* add a take command so you can pick up items
* add a backpack command so you can see what you’re carrying
* make sure you can only fight using items that are actually in your backpack
```

### Class Diagram

When you check the class diagram, nothing new has been added. Everything in this part of the lesson will be changed only in ***main.py***, and you won’t need to edit any classes.

![lesson 6 class diagram](./assets/lesson_5_class_diagram.png)

## Creating a backpack

First, we need to make a backpack variable so we can keep the items we pick up. To do that, we need a type of variable that can store more than one thing at a time. In Python, these are called **collections**. This is the second type of collection you’ve used — the first was **dictionaries**. Now we’ll use a **list**, which is another collection type you already know.

```{admonition} Collections in Python
:class: note
In Python, a **collection** is just a way to store a bunch of things together. You’ve already used some of these before. Different collection types work in different ways, and choosing the right one makes your code easier to understand and faster to run.

Here are the main built-in collection types:

* **Lists:** store things in order and can hold any type of value. You make them with square brackets `[]`.
* **Tuples:** like lists, but you can’t change them once they’re made. You create them with parentheses `()`.
* **Sets:** store values with no duplicates and don’t keep any order. You make them with `{}` or `set()`.
* **Dictionaries:** store pairs of information using a key and a value. You make them with `{key: value}`.

Python also has extra modules for other collection types:

* **Arrays:** store lots of values of the same type.
* **Queues:** store items so the first thing in is the first thing out (FIFO).
* **Stacks:** store items so the last thing in is the first thing out (LIFO).
```

Lists work really well for what we need:
* They can start empty, and we can use `append()` to add items when the player picks them up. 
* We can also check whether the backpack has a certain item using the `in` operator. 
* Lists let us access items by their position
* We can use `pop()` to remove an item from the backpack.

Open ***main.py*** and add the highlighted code below:

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
    elif command == "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                current_room.character = None
            else:
                running = False
        else:
            print("There is no one here to fight")
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

**Investigating** this line of code.

```{admonition} Code Explaination
* `backpack = []` &rarr; creates an empty list and assigns it the name `backpack`
```

## Add take command

Now that we’ve made a backpack, we need a command that lets the player pick up items from the room and put them into it. We’ll use **take** as that command.

Still working in ***main.py*** add the take command using the highlighted code below:

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
    elif command == "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                current_room.character = None
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

Save ***main.py*** **predict** what you think will happen and then **run** the code. What happens to the room description after you take an item?

In **investigating** this code, most of it should be familiar from our previous command event handlers. The different code is:

```{admonition} Code Explaination
* `backpack.append(current_room.item)` &rarr; puts the item from the room into the backpack list.
* `print(f"You put {current_room.item.name} into your backpack")` &rarr; tells the player what item they picked up.
* `current_room.item = None` &rarr; clears the item from the room so it’s no longer there.
```

## Add backpack command

Now that we can collect items, we need a way for the player to check what they’re carrying. We’ll add a new **backpack** command that shows all the items currently inside it.

Still working in ***main.py***, add the code below:

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
    elif command == "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                current_room.character = None
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

Save the ***main.py*** file, **predict** and then **run** your code. This time we should do some serious testing.

We need to make sure that:

- we can pick up all the items in all the rooms
- the items are added to the backpack when they are picked up
- the items are removed from the room when they are picked up

Here is an example for the Cavern testing table. Make sure you also make one for each room.

| Room | Command | Expected result | Actual results |
| :--- | :--- | :--- | :--- |
| Cavern | Backpack | It is empty | |
| Cavern | Take | You put chair into your backpack | |
| Cavern | Backpack | Chair | |
| Cavern | Take | There is nothing here to take | |

If your testing all works out, then it's time to **investigate** the code.

```{admonition} Code Explaination
* `elif command == "backpack":` &rarr; this runs when the player types **backpack**.
* `if backpack == []:` &rarr; checks whether the backpack has nothing in it.
* `print("It is empty")` &rarr; tells the player the backpack is empty.
* `else:` &rarr; runs if the backpack has at least one item.
* `print("You have:")` &rarr; shows a heading before listing the items.
* `for item in backpack:` &rarr; goes through each item in the backpack, one at a time.
* `print(f"- {item.name.capitalize()}")` &rarr; prints the name of each item, with a capital letter at the start.
```

## Adjusting the fight command

Lastly, we need to change the `fight` command so the player can only use items that are actually in their backpack.

Still working in ***main.py***, add the code below.

```{code-block} python
:linenos:
:emphasize-lines: 84-96
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

Save ***main.py***. **Predict** what you think will happen, and then **run** the code.

Let's **investigate** that code, but be aware that there are a number of different sections to that code.

```{admonition} Code Explaination
First, we need to make sure the player actually has the weapon they typed.

* `available_weapons = []` &rarr; makes a new list to hold the **names** of all items in the backpack.

  * the backpack stores `Item` objects
  * the player types a weapon as a **string**
  * so we need a list of item **names**, not item objects
* `for item in backpack:` &rarr; goes through each item in the backpack
* `available_weapons.append(item.name)` &rarr; adds the name of each item to the `available_weapons` list
* `if weapon in available_weapons:` &rarr; checks if the player really has that weapon

If the player *does* have the weapon, we fight using it. Those lines are the same as before, just moved in one tab:

* To indent those lines quickly:

    * highlight lines 88–91
    * press **Tab** once

If the player *doesn’t* have the weapon, we tell them and they lose the fight:

* `else:` &rarr; runs when the weapon isn’t in `available_weapons`
* `print(f"You don't have {weapon}")` &rarr; tells the player they don’t have that item
* `print(f"{current_room.character.name} strikes you down.")` &rarr; the enemy defeats them
* `running = False` &rarr; ends the game by stopping the main loop
```

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


