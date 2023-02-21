# Stage 7 - Victory Conditions

```{topic} In this lesson you will:

- Count the number of enemies
- Create victory conditions
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hTGv542obJo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

We are close to finishing our text-based adventure game. We now have a dungeon in which the user can move around, collect different items, interact with different characters and have the result of those interactions determined by the character type.

In this stage we will look at establishing victory conditions for the game.

We will do this by:

- keeping a count of the number of enemies
- reducing the enemy count when each enemy is defeated
- declare the player victorious when there are no enemies left

### Class Diagram

Look to our class diagram for this stage and you will notice something new. 

The `Enemy` class has a new: 

- `num_of_enemy` attribute
- `get_num_of_enemy` method

![lesson 7 class diagram](./assets/lesson_7_class_diagram.png)

Notice the `num_of_enemy` attribute is underlined. This indicates that this is a **class variable**. This means that the variable is shared across to all instances of that class. Each instance of that class can access and modify the variable, and any changes will be shared with other classes.

In our example, the `num_of_enemy` will be shared with all the `Enemy` objects we create in our game.

## Count Number of Enemies

To keep track of the number of `Enemy` objects in the game, we need to add a **class variable** to the `Enemy` class.

So we need to open the **character.py** file, and add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 43, 49
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

    def __init(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        Enemy.num_of_enemy += 1
        
    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
```

Save the code, and **run** it to ensure there are no errors.

**Investigating** the code:

- `num_of_enemy = 0` &rarr; creates our **class variable**
  - important to note the location and the indent level of **class variables**:
    - need to be placed before the `__init__` method
    - indented once &rarr; same level as method definitions
  - also note that, unlike the other attributes, `num_of_enemy` does start with `self` because it is a **class variable**
- `Enemy.num_of_enemy += 1` &rarr; increases `num_of_enemy` by one each time a new `Enemy` object is created.
  - since `__init__` runs each time a new enemy is made, the value of `num_of_enemy` will increase

Now that we are keeping track of the number of enemies, but we can't see what that number is. So let's create a method to find out how many enemies are in the dungeon

Still working in **character.py**, add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 60-61
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

    def __init(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        Enemy.num_of_enemy += 1
        
    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False

    def get_num_of_enemy():
        return Enemy.num_of_enemy
```

Let's investigate that method:

- `def get_num_of_enemy():` &rarr; defines the method
  - there is no `self` argument &rarr; this method is not tied to a particular instance, but rather the whole class.
- `return Enemy.num_of_enemy` &rarr; provides the current value of `num_of_enemy`
  - notice the `Enemy.` &rarr; tells Python this is a **class variable** of the `Enemy` class

## Reduce Enemy Count

So we have a count of the number of enemies, and we can retrieve that value, now we need to reduce the enemy count when the player defeats an enemy.

The `Enemy` class `fight` method already has code that is executed when the player defeats the enemy, so we just need to add to that.

Still in **character.py** go to insert the highlighted line below:

```{code-block} python
:linenos:
:emphasize-lines: 55
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

    def __init(self,name):
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

Save the code before we **Investigate** it:

- line `53` &rarr; already determines if the player beats the enemy
- `Enemy.num_of_enemy -= 1` &rarr; reduces the value of the **class variable** by one.

## Check for Victory

The player will be victorious when they have defeated all the enemies in the dungeon. When all the enemies have been defeated the `Enemy.num_of_emeny` will be `0`. So we need to find the best place to check this.

Let's look back at **main.py**. Line `89` is where Python decides if they player wins, so it makes sense to put out `num_of_enemy` check around here.

Add the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 91-93
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
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

**Investigating** that code:

- line `89` &rarr; already established that our new code will only run when the player defeats an enemy
- `if Enemy.get_num_of_enemy() == 0:` &rarr; checks if the **class variable** is `0`
- `print("You have slain all the enemies. You are victorious!")` &rarr; displays a victory message
- `running = False` &rarr; readies to finish the game by exiting the main loop.