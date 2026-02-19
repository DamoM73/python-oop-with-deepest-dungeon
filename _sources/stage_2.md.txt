# Stage 2 - Movement

```{topic} Learning Intentions
By the end of this lesson you will:
* understand event-driven programming and the role of a main loop
* know how methods use arguments and return values to control behaviour
* create a method that returns a new state
* build a main loop that reads user input and triggers event handlers
* test branching code and handle invalid commands with clear feedback 
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hZd1FcDApCI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

In Stage 1 you made three rooms, connected them, and got the program to describe each one. That was a good start, but it’s not much of a game yet. In Stage 2 you’ll write code that lets the player move between rooms, which means changing the game’s **state** (for example, which room you are in), and you’ll build the **main loop**.

```{admonition} State machines
:class: note
A state machine is a way of thinking about how a program changes as things happen. At any moment, the program is in one **state** (like being in a certain room in your game). When an event happens, such as the player typing a command, the program follows a rule that decides what the next state should be. 

For example, typing “east” might move you from the Armoury to the Lab. Each state has certain things you can do, and each action can move you to a new state. It’s like following a map where every choice leads to a different place, and the program always knows exactly where it is and what it should do next.
```

The main loop is a key part of **event-driven programming**. Your ***main.py*** file will set up the game and create all the objects it needs. Then it will enter the **main loop**, where the program waits for the player to type something and then reacts to that input.

```{admonition} Event-driven programming
:class: note
Event-driven programming is when a program doesn’t just run straight from top to bottom, but instead waits for things to happen and reacts to them. These things are called **events**, like the user typing a command, clicking a button, or a sensor sending data. 

The program sits in a loop, **listening** for these events, and when one occurs, it runs the code that matches that event. This makes programs more flexible because they only do something when there’s a reason to, just like you don’t answer someone until they speak to you first.
```

To achieve this we will need to complete the following steps:

```{admonition} Pseudocode
:class: pseudocode
- Create the `move` method
- Initialize the starting room
- Create the main loop which:
   - describes current room
   - accepts user input
   - responds to user input
```

### Class Diagram

We have updated the `Room` class diagram to reflect the Stage 2 work.

![lesson 2 class diagram](./assets/lesson_2_class_diagram.png)

Notice we have a new method `move(direction):room`

- accepts one argument (direction)
- returns a `Room` object

## Create the move method

Open the ***room.py*** file and add the code highlighted below:

```{code-block} python
:linenos:
:emphasize-lines: 22-28
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        
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

We need to create the **main loop** before we call this code, but let's **investigate** our new code anyway.

```{admonition} Code Explaination
* `def move(self, direction):` &rarr; defines the `move` function and takes one input: the direction the player wants to go.
* `# returns the room linked in the given direction` &rarr; a comment explaining what the function does.
* `if direction in self.linked_rooms.keys():` &rarr; checks whether the direction the player typed is actually one of the directions this room allows.
  * `self.linked_rooms.keys()` &rarr; gets all the possible directions you can go from this room.
  * `if direction in` &rarr; checks if the player’s direction is one of those options.
* `return self.linked_rooms[direction]` &rarr; returns the room in that direction if it’s valid.
  * `self.linked_rooms[direction]` &rarr; retrieves the room object linked to that direction from the dictionary.
* `else:` &rarr; runs if the direction isn’t allowed.
  * `print("You can't go that way")` &rarr; tells the player they tried an invalid direction.
  * `return self` &rarr; keeps the player in the same room because the move didn’t work.
```

## Initialize starting room

Now go to the ***main.py*** file and make the highlighted changes below

```{code-block} python
:linenos:
:emphasize-lines: 21-26, 28-29
# main.py

from room import Room

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

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''

# initialise variables
current_room = cavern
```

Let's **investigate** the new code

```{admonition} Code Explaination
* The `'''` on lines 21 and 26 &rarr; turns the room descriptions into a big comment, so Python ignores that code.
  * You could delete it, but leaving it commented out means you can bring it back later if you need it for debugging.
* `# initialise variables` &rarr; a comment to explain what the next lines of code are doing.
* `current_room = cavern`
  * makes a variable that tracks which room the player is currently in.
  * starts the player in the `cavern` room.
```

## Create main loop

Still working in the ***main.py*** file, we will now make the main loop.

Add the highlighted code below so you can see the main loop for the first time.

```{code-block} python
:linenos:
:emphasize-lines: 30, 32-36
# main.py

from room import Room

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

'''
# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
'''

# initialise variables
current_room = cavern
running = True

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
```

Finally we can run our code, but don't forget **PRIMM**. **Predict** you think the program will do, then **run** the program.

```{admonition} Escaping an infinite loop
:class: info
If your Python program gets stuck in an infinite loop, you can stop it by pressing `Ctrl + C` on Windows or `Control + C` on a Mac. 

If you’re using Thonny, you can also click the **stop** button to end the program.
```

Let's **investigate** the new code line-by-line.

```{admonition} Code Explaination
* `running = True` &rarr; used to keep the **main loop** going until the player decides to quit.
  * This is called a **flag variable**&mdash;it starts as `True`, and when the player wants to exit, it gets changed to `False`.
* `# ----- MAIN LOOP -----` &rarr; a comment showing where the main loop begins.
* `while running:` &rarr; starts the **main loop**.
  * The loop keeps repeating as long as `running` is `True`.
* `current_room.describe()` &rarr; runs the `describe` function for whatever room is stored in the `current_room` variable.
  * At the start, this is the `cavern`.
* `command = input("> ").lower()` &rarr; reads what the player types.
  * `input("> ")` &rarr; shows `"> "` on the screen and waits for the player to type something.
  * `.lower()` &rarr; turns the input into lowercase so the program can read it more easily.
  * `command =` &rarr; stores the final text in the `command` variable.
```

Notice that no matter what the player types, the same thing keeps happening. That’s because we’ve built the **main loop**, which is waiting for events (the player’s input), but we haven’t written any code to react to those events yet. 

In a **state machine**, the game should change state when something happens&mdash;like moving to a new room&mdash;but right now there are no rules telling the program how to change state when an event occurs. So the loop just repeats without doing anything new.

## Responding to commands

In Event Driven Programming the entering of user's commands is called an **event**. Now we have to create code that responds to those events. This kind of code is called an **event handler**.

Back in our ***main.py*** we're going to create an **event handler** to deal with the entry of a direction (`"north"`, `"south"`, `"east"` or `"west"`). Add the highlighted code.

```{code-block} python
:linenos:
:emphasize-lines: 38-39
# main.py

from room import Room

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
```

**Predict** you think the program will do, then **run** the program.

Let's **investigate** that code.

```{admonition} Code Explaination
* `if command in ["north", "south", "east", "west"]:` &rarr; runs this block only if the player typed a direction.
  * `["north", "south", "east", "west"]` &rarr; the list of directions the game will accept.
  * `if command in` &rarr; checks whether what the player typed is in that list.
* `current_room = current_room.move(command)` &rarr; works out which room to go to next.
  * `current_room.move(command)` &rarr; calls the `move` function, using the player’s direction to find the next room.
  * `current_room =` &rarr; updates `current_room` so the game’s state now matches the new room.
```

### Testing

```{admonition} Testing branching code
:class: note
Whenever you test branching code, it is important to ensure you methodically test **all** possible branches.

To do this:
- create a table which lists every possible branch
- for each branch, list the expected results
- record the actual results
- idenfiy any discrepancies
```

Now that we can move between all our rooms, we can test that our code is working correctly. Draw up a  table to test each option. Below is an example of my table.

| Current Room | Command | Expected Result | Actual Result |
| :-- | :-- | :-- | :-- |
| cavern | `north` | "You can't go that way" | "You can't go that way" |
| cavern | `south` | moved to armoury | moved to armoury |
| cavern | `east` | "You can't go that way" | "You can't go that way" |
| cavern | `west` | "You can't go that way" | "You can't go that way" |
| armoury | `north` | moved to cavern | moved to cavern |
| armoury | `south` | "You can't go that way" | "You can't go that way" |
| armoury | `east` | moved to lab | moved to lab |
| armoury | `west` | "You can't go that way" | "You can't go that way" |
| lab | `north` | "You can't go that way" | "You can't go that way" |
| lab | `south` | "You can't go that way" | "You can't go that way" |
| lab | `east` | "You can't go that way" | "You can't go that way" |
| lab | `west` | moved to armoury | moved to armoury |

Notice that I tested each of the four directions in each of the three rooms in my dungeon.

### Exiting

Although the user can now move around our dungeon, they cannot exit the game. Now we need to make an **event handler** to deal with the user wanting to quit the game.

```{code-block} python
:linenos:
:emphasize-lines: 40-41
# main.py

from room import Room

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
```

**Predict** you think the program will do, then **run** the program.

Make sure you test the **quit** option

Let's **investigate** that code

```{admonition} Code Explaination
- `elif command == "quit":` &rarr; if the command is not an acceptable direction, then check if it is `quit`
- `running = False` change our **flag variable** to `False`
  - this means that when the loops returns to the top, `where running` will be `False` and the loop will exit.
```

### Capture incorrect commands

The code now understands the movement commands and the quit command, but what if the player types something completely different? The loop just keeps going and shows the same room again. That’s not very helpful. 

We should tell the player when their command doesn’t make sense, so they know they need to try something else. Let’s fix that.

Change ***main.py*** to include the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 42-43
# main.py

from room import Room

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

**Predict** you think the program will do, then **run** the program.

Make sure you test our error capturing by entering some incorrect commands.

Let's **investigate** the new code:

```{admonition} Information
:class: info
- `else:` &rarr; a catch-all option for any input which is not a recognised command.
- `print("I don't understand.")` &rarr; lets the user know their command doesn't make sense.
```

### Testing
Now we need to test those two additional features. Draw up a table to test each option. Below is an example of my table.

| Command | Expected Result | Actual Result |
| :-- | :-- | :-- |
| `south` | moved to armoury | moved to armoury |
| `dog` | "I don't understand." | "I don't understand." |
| `quit` | program exits | program exits |

---

## Stage 2 task

There is not much to do for our **Make** phase of this stage, but you do need to test that you can navigate to and from your stage 1 task additional room.

Take the table you used to test navigating the rooms and expand it to also test navigating to your stage 1 task room.
 

