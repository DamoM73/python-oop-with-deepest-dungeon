# Stage 1 - Create Rooms

```{topic} Learning Intentions
By the end of this lesson, you will be able to:
* understand how classes, attributes, and methods work together
* read simple UML class diagrams and identify the class name, its attributes, and its methods
* make a basic Python class with an `__init__` method and another method you create
* create objects from a class and give them values for their attributes
* connect objects to each other and show those connections in your output
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/GeSTPYPPEfU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## How we plan

When working with computers you need to break problems into clear, logical steps that a computer can follow exactly. Humans can rely on shortcuts, guesses, and experience to fill in gaps, but computers cannot use those heuristics. A computer only does exactly what it is told, so every step must be precise, ordered, and unambiguous. 

This computational thinking helps you turn a messy real-world problem into a series of simple, complete instructions that a computer can execute without ever needing to “figure things out” on its own.

To aid in this planning we will use **pseudocode**. Pseudocode is a simple way of writing out the steps of a program using plain English instead of real code, so you can focus on the logic without worrying about exact syntax. It shows what the program should do, in order, using clear instructions like IF, ELSE, REPEAT, and OUTPUT. 

It doesn’t run on a computer, but it helps you plan your thinking before you start writing real code, making mistakes easier to spot and your final program easier to build.

## Planning

In this lesson we want to create three rooms and link those rooms together. Below is a rough map of our dungeon.

![map](./assets/dungeon_map.png)
 
To achieve this we will need to create two files:

- ***main.py*** &rarr; runs the program
- ***room.py*** &rarr; stores information about the `Room` class

In those two files we will need to do the following:

```{admonition} Stage 1 Pseudocode
:class: pseudocode
- Define the `Room` class
- Create `Room` object
- Describe `Room` objects
- Link the `Room` objects
- Include the linked `Rooms` when each `Room` object is described
```

### Class diagram

UML **class diagrams** are a simple way to show what a class looks like and how it works with other classes.

In UML, classes are represented by the three row table.

![class diagram](./assets/class_diagrams.png)

- The class name goes in row 1
- All the class attributes go in row 2, along with their datatype
- The class methods are shown in row 3, along with the arguments and datatype of any returned value

The case diagram for the `Room` class is as follows:

![lesson 1 class diagram](./assets/lesson_1_class_diagram.png)

From the diagram we can tell:

- The class name is `Room`
- The attributes are:
  - `name` which is a **string** datatype
  - `description` which is a **string** datatype
  - `linked_rooms` which is a **dictionary**
- The methods are:
  - `describe` which takes no arguments and returns no values
  - `link_room` which returns nothing and takes two arguments:
    - `room`
    - `direction`

## Define the Room class

Open up Thonny and, if needed, create a new file.

Then type the code below into the new file

```{code-block} python
:linenos:
:emphasize-lines: 1,3
# room.py

class Room():
```

```{admonition} Code Explaination
- `# room.py` - is a simple comment containing the file name. Since this program involves multiple files, this is a simple way to keep track of which file you are currently working on.
- `class Room():` - defined the `Room` class object
```

```{admonition} Naming conventions
:class: note
Most Python names use `snake_case`, but class names are different. Class names must use `CamelCase`, like `Room`.

Python won’t give you an error if you break this rule, but following it makes your code easier to read and maintain.

File names should stay lowercase. This matters when you import your class from the file.
```

### Dunder init method

Every Python class has a special method called the **dunder init**. Its real name is `__init__` — the “double underscores” are why we call it **dunder**.

The dunder init runs automatically every time you create a new object from a class. It sets up the object’s attributes and gets it ready to use. You can also use it to run any other setup the object needs.

Now we’ll make a dunder init for our `Room` class.

```{code-block} python
:linenos:
:emphasize-lines: 5-6, 8-9
# room.py

class Room():

    def __init__(self, room_name):
        # intialise the room object

        self.name = room_name.lower()
        self.description = None
```

```{admonition} Code Explaination
* `def __init__(self, room_name):` this line starts the dunder init method.
  * `self` is always the first argument in any class method. It means “this object”. If you make a `cavern` room, then inside the code `self` means “this specific cavern room”.
  * `room_name` is the text you give the room when you create it. It’s the name the object will use.
* `# initialise the room object` &rarr; this is just a comment explaining what the method does. Comments help keep your code easy to read.
* `self.name = room_name.lower()` &rarr; this sets the room’s name.
  * `self.name` means “this room’s name”.
  * `room_name.lower()` changes the name to lowercase before storing it.
* `self.description = None` &rarr; this creates a description attribute for the room and sets it to `None` for now.
  * `self.description` means “this room’s description”.
  * It’s good practice to create all attributes inside `__init__`, even if they don’t have a value yet. Setting them to `None` keeps things organised.
```

### Save ***room.py***

```{admonition} Saving files
:class: warning
Since this program will be using multiple files, the location they are saved is important. 

The ***main.py*** file will be importing classes from the your other files. The first place it will look is within the local directory (ie. the folder it is saved in).

To minimise potential problems, you need to create a new folder for these tutorials.

It is also important to ensure you file names are correct, inlcuding the capilatisation and the ***.py*** extension.
```

Make a folder called ***deepest_dungeon***. Calling your ***room.py*** save it in your ***deepest_dungeon*** folder.

## Create Room objects

Create a new file. Save it as ***main.py*** in your ***deepest_dungeon*** folder. This file is going to control our game.

Then type to following code into the ***main.py***

```{code-block} python
:linenos:
:emphasize-lines: 1, 3, 5-6, 8, 10, 12
# main.py

from room import Room

# create rooms
cavern = Room("Cavern")

armoury = Room("Armoury")

lab = Room("Laboratory")

print(cavern.name)
```

We're going to run our program for the first time, but before let's introduce the **PRIMM** concept.

```{admonition} PRIMM
:class: note
Throughout this course we will use the **PRIMM** process to reinforce our learning. **PRIMM** stands for **Predict**, **Run**, **Investigate**, **Modify**, and **Make**. It reflects effective programming practices and encourages curiosity in programming.

**Predict**: Before you run the code you need to predict what you think will happen. Go ahead and have a guess at what you think will happen.

**Run**: Then run the program and see how accurate your prediction was. If your prediction was incorrect, how was the result different?

**Investigate**: Go through the code and work out what each line of code does.

**Modify**: Edit the code. Change it around and see that results your get

**Make**: Use your new understanding of the code to make a different program.
```

Lets run through the **PRIMM** process now

**Predict** in detail what you think the program will do, then **run** the program.

Let's **investigate** the new code line-by-line.

```{admonition} Code Explaination
* `# main.py` &rarr; this is just a comment so you know which file you’re looking at.
* `from room import Room` &rarr; this imports your own class.
  * `Room` is the class you created.
  * `room` is the file ***room.py*** where that class lives.
  * This line basically means: import the `Room` class from the file ***room.py***.
  * The class name is CamelCase (`Room`), and the file name is lowercase (***room***).
* `# create rooms` &rarr; another comment to organise your code. ***main.py*** will get long, so comments help keep things clear.
* `cavern = Room("Cavern")` &rarr; this creates your first room.
  * `Room("Cavern")` makes a new `Room` object.
    * When you create it, the `__init__` method runs automatically.
    * `"Cavern"` gets sent into `__init__`, which saves it as the room’s name.
  * `cavern =` stores the new room object in a variable called `cavern`.
* `armoury = Room("Armoury")` &rarr; makes another `Room` object using the name `"Armoury"` and stores it in `armoury`.
* `lab = Room("Laboratory")` &rarr; makes a third room using `"Laboratory"` and stores it in `lab`.
* `print(cavern.name)` &rarr; prints the name stored inside the `cavern` room object.
  * `cavern.name` gets the value of that attribute.
  * `print` shows it on the screen.
```

**Modify** the code so that it prints the names of the other two `Room` objects.

## Describe Room objects

If we look at the `Room` class we will notice that there is a `description` attribute which currently stores `None`.

```{code-block} python
:linenos:
:emphasize-lines: 9
# room.py

class Room():

    def __init__(self, room_name):
        # intialise the room object

        self.name = room_name.lower()
        self.description = None
```

We want our `Room` objects to have descriptions, so let's assign some values to them.

```{code-block} python
:linenos:
:emphasize-lines: 7, 10, 13, 16
# main.py

from room import Room

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn’t reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour."

lab = Room("Laboratory")
lab.description = "A strange odour hangs in a room filled with unknownable contraptions."

print(cavern.name)
print(cavern.description)
```

**Predict** in detail what you think the program will do, then **run** the program.

Let's **investigate** the *new* code line-by-line.

```{admonition} Code Explaination
* `cavern.description = "A room so big that the light of your torch doesn’t reach the walls."` &rarr; this sets the `description` of the `cavern` room. You’re giving the room a sentence that describes it.
* `armoury.description = "The walls are lined with racks that once held weapons and armour."` &rarr; this gives the `armoury` room its description.
* `lab.description = "A strange odour hangs in a room filled with unknownable contraptions."` &rarr; this gives the `lab` room its description.
* `print(cavern.description)` &rarr; this looks at the cavern’s description and prints it on the screen.
```

**Modify** the code so that it prints the descriptions of the other two `Room` objects.

### Describe method

It’s better programming practice to use methods instead of grabbing an object’s attributes directly. In the class diagram, the `Room` class has a `describe()` method for this purpose.

![lesson 1 class diagram](./assets/lesson_1_class_diagram.png)

Using a method like `describe()` is a cleaner and safer way to show a room’s details, so we’ll add that method to our code.

Go back to the ***room.py*** file and add the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 10-13
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        
    def describe(self):
        # displays a description of the room in the UI
        print(f"\nYou are in the {self.name}")
        print(self.description)
```

Then go back to ***main.py*** and replace lines 15 and 16 with the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 15-18
# main.py

from room import Room

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn’t reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour."

lab = Room("Laboratory")
lab.description = "A strange odour hangs in a room filled with unknownable contraptions."

# describe rooms
cavern.describe()
armoury.describe()
lab.describe()
```

**Predict** in detail what you think the program will do, then **run** the program.

Let's **investigate** the *new* code line-by-line. First the code in ***room.py***:

```{admonition} Code Explaination
* `def describe(self):` &rarr; this line starts the `describe` method.
  * `def` is how you define a function or method in Python.
  * `describe` is the method’s name.
  * `(self)` means “this object”, just like in `__init__`.
  * The `:` tells Python the indented block below belongs to this method.
  * Methods inside a class must be indented one level.
* `# displays a description of the room in the UI` &rarr; this comment explains what the method does. Comments make your code easier to understand.
* `print(f"\nYou are in the {self.name}")` &rarr; this line takes the room’s name and puts it into a sentence, then prints it to the screen.
  * `self.name` &rarr; “this room’s name”.
* `print(self.description)` &rarr; this prints whatever description the room has.
```

Now the code in ***main.py***

```{admonition} Code Explaination
* `# describe rooms` &rarr; this is just a comment to organise the code.
* `cavern.describe()` &rarr; this runs the `describe` method for the `cavern` room.
* `armoury.describe()` &rarr; this runs the `describe` method for the `armoury` room.
* `lab.describe()` &rarr; this runs the `describe` method for the `lab` room.
```

## Link rooms

If you look at our map you will notice that the rooms are linked, so that our adventure can move between them.

- Cavern &darr; Armoury
- Armoury &uarr; Cavern
- Armoury &rarr; Lab
- Lab &larr; Armoury

![map](./assets/dungeon_map.png)

The class diagram shows that each room uses an attribute called `linked_rooms` and a method called `link_room(room, direction)` to connect rooms together.


![lesson 1 class diagram](./assets/lesson_1_class_diagram.png)

`linked_rooms` is a dictionary. A dictionary stores information in **key:value** pairs.

* The **key** will be a direction like north, south, east, or west.
* The **value** will be the `Room` object that sits in that direction.

For example, the Armoury’s `linked_rooms` dictionary might look like a list of directions that lead to other rooms.

```{code-block} python
:linenos:
{
  "north" : cavern,
  "east" : lab
}
```

```{admonition} Dictionaries
:class: note
A Python dictionary is like a real-life dictionary, but for your code.

In a real dictionary, you look up a **word** to find its **meaning**. In a Python dictionary, you look up a **key** to get its **value**.

Dictionaries are useful when you want to group information together and label it clearly so you can find it later.
```

The `link_room` method takes two pieces of information — the room you want to connect and the direction it’s in. It then adds this information to the `linked_rooms` dictionary so the room knows what’s next to it.

So lets implement this. First go back to ***room.py***, and add the code highlighted below

```{code-block} python
:linenos:
:emphasize-lines: 9, 16-18
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        
    def describe(self):
        # displays a description of the room in the UI
        print(f"\nYou are in the {self.name}")
        print(self.description)
    
    def link_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
```

Then open the ***main.py*** and add the code highlighted below:

```{code-block} python
:linenos:
:emphasize-lines: 15-19
# main.py

from room import Room

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn’t reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour."

lab = Room("Laboratory")
lab.description = "A strange odour hangs in a room filled with unknownable contraptions."

# link rooms
cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
lab.link_rooms(armoury,"west")

# describe the rooms
cavern.describe()
armoury.describe()
lab.describe()
```

**Predict** in detail what you think the program will do, then **run** the program.

Did you predict that nothing would change? We'll fix that later. In the meanwhile, let's **investigate** the **new** code line-by-line. 

First the code in ***room.py***:

```{admonition} Code Explaination
* `self.linked_rooms = {}` &rarr; this line creates the `linked_rooms` attribute.
* `def link_rooms(self, room_to_link, direction):` &rarr; this defines the `link_rooms` method. It takes three arguments:
  * `self` &rarr; means “this room”.
  * `room_to_link` &rarr; the room you want to connect to.
  * `direction` &rarr; north, south, east, or west.
* `# links the provided room, in the provided direction` &rarr; a comment explaining what the method does.
* `self.linked_rooms[direction.lower()] = room_to_link` &rarr; this adds the connection to the dictionary.
  * `direction.lower()` &rarr; turns the direction into lowercase.
  * `self.linked_rooms[direction.lower()]` finds the correct spot in the dictionary.
  * `= room_to_link` &rarr; stores the room in that direction.
    * If the direction wasn’t there yet, it creates it.
    * If it was already there, it replaces the old value.
```

Then in ***main.py***:

```{admonition} Code Explaination
- `# link rooms` &rarr; code structuring comment
- `cavern.link_rooms(armoury,"south")` &rarr; links the `cavern` and the `armoury` to the `"south"` of it.
- `armoury.link_rooms(cavern,"north")` &rarr; links the `armoury` and the `cavern` to the `"north"` of it.
- `armoury.link_rooms(lab,"east")` &rarr; links the `armoury` and the `lab` to the `"east"` of it.
- `lab.link_rooms(armoury,"west")` &rarr; links the `lab` and the `armoury` to the `"west"` of it.
```

Notice that each connection needs two calls to the `link_rooms` method.

## Include linked Rooms in description

When you ran the code, nothing looked different, but the rooms were actually linked together. We just weren’t showing those links on the screen. Now we’ll fix that by adding the connected rooms to the room’s description.

Go to your ***room.py*** file and include the highlighted code below.

```{code-block} python
:linenos:
:emphasize-lines: 15-16
# room.py

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        
    def describe(self):
        # displays a description of the room in the UI
        print(f"\nYou are in the {self.name}")
        print(self.description)
        for direction in self.linked_rooms:
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")
    
    def link_rooms(self, room_to_link, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link
```

**Predict** in detail what you think the program will do, then **run** the program.

Let's **investigate** the new code line-by-line.

```{admonition} Code Explaination
* `for direction in self.linked_rooms:` &rarr; this loop goes through every entry in the `linked_rooms` dictionary.
  * Dictionaries can be used in a `for` loop, just like lists.
  * Here, `direction` will be each key in the dictionary, like `"north"`, `"south"`, `"east"`, or `"west"`.
* `print(f"To the {direction} is the {self.linked_rooms[direction].name}")` &rarr; this line prints a sentence showing which room is in that direction.
  * `direction` is the current direction (for example, `"north"`).
  * `self.linked_rooms[direction].name` gets the name of the room linked in that direction.
```

---

## Stage 1 task

During this lesson we have only been focusing on the first four stages of the PRIMM model. Now it is time for your to implement the **Make** phase.

Taking the knowledge your have gained through this lesson, you need to:

- create one, or more additional rooms
- link those additional rooms to one or more of your other rooms.

