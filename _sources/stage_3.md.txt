# Stage 3 - Character Creation

```{topic} Learninng Intentions
By the end of this lesson you will:
* understand how classes, attributes, and methods work together
* recognise how different objects can interact inside a larger system
* identify how user actions can trigger events in an event-driven program
* create new classes and objects with relevant attributes
* link objects so they interact in meaningful ways
* write simple methods that control behaviour
* update a main loop so it responds to user input with different actions
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ufsmJYdUg1Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

Now that the user has a dungeon that they can move around, we need to make it interesting. At this stage we will populate our dungeon with characters that the user can interact with.

To achieve this we will:

```{admonition} Pseudocode
:class: pseudocode
- Define a character class
- Create characters
- Add characters to the rooms
- Include characters in the room descriptions
- Create character interactions
   - talk method
   - hug method
   - fight method
- Add interactions to the main loop
```

### Class Diagram

The `Character` class is a new class, so it will require a second class diagram.

We also need to add a `character` attribute to the `Room` class so we can record who is in each room.

![lesson 3 class diagram](./assets/lesson_3_class_diagram.png)

## Define the Character class

In Thonny create a new file and enter the code below. Then save it as ***character.py*** in the same folder as ***main.py*** and ***room.py*** (remember capitalisation).

```{code-block} python
:linenos:
:emphasize-lines: 1, 3, 5-9
# character.py

class Character():
    
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None
```

Let's investigate this code:

```{admonition} Code Explaination
:class: info
* `# character.py` &rarr; a note to remind us which file this code belongs to
* `class Character():` &rarr; creates a new type of object called `Character`
* `def __init__(self, name):` &rarr; this special method runs every time you make a new Character
* `# initialises the character object` &rarr; a note explaining what the method is for
* `self.name = name` &rarr; saves the character’s name inside the object
* `self.description = None` &rarr; sets up a description for the character, but leaves it empty for now
* `self.conversation = None` &rarr; sets up something the character might say, but also leaves it empty for now
```

## Create characters

Now that we have a `Character` class, we can go to ***main.py*** and create `Character` objects.

Open ***main.py*** and add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 4, 22-24, 26-28
# main

from room import Room
from character import Character

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
ugine = Character("Ugine")
ugine.description = "a huge troll with rotting teeth."

nigel = Character("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''
```

Investigating that code:

```{admonition} Code Explaination
:class: info
* `from character import Character` &rarr; brings the Character class into this file so we can use it
* `# create characters` &rarr; a note showing this section is where we make characters
* `ugine = Character("Ugine")` &rarr; makes a new Character named Ugine and stores it in the variable `ugine`
* `ugine.description = "a huge troll with rotting teeth."` &rarr; gives Ugine a description
* `nigel = Character("Nigel")` &rarr; makes a new Character named Nigel and stores it in the variable `nigel`
* `nigel.description = "a burly dwarf with golden bead in woven through his beard."` &rarr; gives Nigel a description
* `nigel.conversation = "Well youngan, what are you doing here?"` &rarr; gives Nigel something he can say
* Ugine has no conversation set, so his conversation stays empty (None)
```

## Add Characters to the Rooms

Now we have two classes that work together: `Room` and `Character`. We need a way for our code to show which character is in which room. In the Room class diagram, you can see we added a new `character` attribute. This lets each room store the character that’s inside it.

![lesson 3 class diagram](./assets/lesson_3_class_diagram.png)

This is an arbitrary decision. We could easily had added the new attribute to the `Character` class showing this is the room the character is in. Both are valid. The important thing is to be consistent, and to document your decision for others to understand. That's why the class diagram is so important.

### Add character attribute to Room class in ***room.py***

Return to ***room.py*** and add the highlighted line below.

```{code-block} python
:linenos:
:emphasize-lines: 10
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        
    def describe(self):
        # sends a description of the room to the terminal
        print(f"\nYou are in the {self.name}")
        print(self.description)
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

Investigating that code:

```{admonition} Code Explaination
:class: info
- `self.character = None` &rarr; creates a new attribute called `character` and assigns `None` to it.
```

### Add characters to the rooms in ***main.py***

The return to ***main.py*** and add characters to our rooms using the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 32-33
# main.py

from room import Room
from character import Character

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
ugine = Character("Ugine")
ugine.description = "a huge troll with rotting teeth."

nigel = Character("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.character = ugine
lab.character = nigel

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
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

Investigating the code:

```{admonition} Code Explaination
* `armoury.character = ugine` &rarr; puts the character Ugine into the armoury room
* `lab.character = nigel` &rarr; puts the character Nigel into the lab room
```

Let's do some testing. **Predict** what you think will happen and then **Run** the program. It should do nothing new, unless there is an error. That's because we haven't adjusted the room descriptions to include the characters. Let's do that now.

## Include characters in room description

To add the characters to the room description is a two step method:

1. Create a `describe` method in the `Character` class
2. modify the `describe` method in the `Room` class so it calls the `character.describe` method

### Add describe method to Character class

Go to ***character.py*** and add the highlighted code below to create the `describe` method

```{code-block} python
:linenos:
:emphasize-lines: 11-13
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
```

Investigating the new code:

```{admonition} Code Explaination
* `def describe(self):` &rarr; creates a describe method for characters
  * even though we already have a describe method, it’s fine because that one belongs to the Room class
  * they’re in different “namespaces,” which just means they belong to different objects
  * so `character.describe()` and `room.describe()` are completely separate
* `# sends a description of the character to the terminal` &rarr; a note explaining what the method does
* `print(f"{self.name} is here, {self.description}")` &rarr; prints the character’s name and what they look like
```

```{admonition} Name spaces
:class: note
Imagine your wardrobe at home. You have different spots for different things — shelves for shirts, drawers for socks, hangers for jackets. When you need something, you go to the right spot and grab it.

Namespaces in programming work the same way. They’re like labelled sections that keep code organised. Each namespace stores its own variables and functions, just like each part of your wardrobe stores its own type of clothes.

For example, a “math” namespace might hold maths-related functions, while a “game” namespace might hold game-related functions. They are kept separate so nothing gets mixed up.

Using namespaces keeps your code tidy and makes it easy to find exactly what you need.
```

### Modify the Room class describe method

Before we change the `describe` method, we need to fix a small issue. We have three rooms but only two characters, which means one room (the cavern) has no character in it. We don’t want the game to talk about a character unless one is actually there.

Because we set `character` to `None` when a room is empty, the cavern still has `cavern.character = None`. So, when we describe a room, we should only show the character's description if the `character` value is not `None`.

Return to ***room.py*** and modify the `describe` method as highlighted below.

```{code-block} python
:linenos:
:emphasize-lines: 16-17
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        
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

Let's investigate that code:

```{admonition} Code Explaination
* `if self.character is not None:` &rarr; checks if this room actually has a character in it
  * the `is` keyword is used to check if something is equal to `None`
* if there *is* a character, the code runs the character’s `describe` method to show their details
```

### Testing

**Predict** what you think will happen and the **Run** the code.

Test to make sure that you get character descriptions, but only when you enter a room that has a character in it.

## Create character interactions

We want to add three interactions with out characters:

- talk
- hug
- fight

If we look once again at our class diagram, we will see that in the character class, there is a method for each of these interactions.

![lesson 3 class diagram](./assets/lesson_3_class_diagram.png)

### Add new methods to Character class

Return to the ***character.py*** file. First lets add the talk method by adding code highlighted below.

```{code-block} python
:linenos:
:emphasize-lines: 15-20
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
```

Let's investigate this code:

```{admonition} Code Explaination
* `def talk(self):` &rarr; this creates the talk method for this character
* `# send conversation to the terminal` &rarr; a note explaining what the method does
* `if self.conversation is not None:` &rarr; checks if the character actually has something to say
  * in ***main.py***, Nigel has a conversation, but Ugine doesn’t
  * the method needs to handle both situations
* `print(f"{self.name}: {self.conversation}")` &rarr; if the character has a conversation, print their name and what they say
* `else:` &rarr; runs when the character has no conversation set
* `print(f"{self.name} doesn't want to talk to you")` &rarr; shows a message for characters who won’t talk
```

Now let's add both the `hug` and `fight` methods with the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 22-24, 26-28
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

    def fight(self):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
```

By this stage the code for both methods should look familiar:

- define the method with `self` as the first argument
- provide a comment describing what the method does
- display a message that uses one of the character's attributes

## Add the interactions to the main loop

Now that the player can interact with our characters, we need to add the three options (talk, hug, fight) to our event handler in the main loop.

Return to ***main.py***, and add the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 54-68
# main.py

from room import Room
from character import Character

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
ugine = Character("Ugine")
ugine.description = "a huge troll with rotting teeth."

nigel = Character("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.character = ugine
lab.character = nigel

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
            current_room.character.fight()
        else:
            print("There is no one here to fight")
    elif command == "quit":
        running = False
    else:
        print("I don't understand.")
```

Since the event handler for all three interactions is virtually the same, we'll just investigate the code for the `talk` method:

```{admonition} Code Explaination
- `elif command == "talk":` &rarr; checks if the user's command was `talk`
- `if current_room.character is not None:` &rarr; checks if there is a character in the room
  - remember that rooms can not have a character (eg. Cavern) so we need to allow for this.
- `current_room.character.talk()` &rarr; if there is a character, the call its `talk()` method
- `else:` &rarr; deals with rooms with no character
- `print("There is no one here to talk to")` &rarr; message for when there is no character
```

## Stage 3 task

Once again we have only been focusing on the first four stages of the PRIMM model. Now it is time for your to implement the **Make** phase.

In Stage 1 you created an additional room. So now it is time to populate that room.

- Create an additional character for each extra room you've added
- Add those characters to your additional rooms

