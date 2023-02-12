# Stage 4 - Character Types

```{topic} In this lesson you will:

- Learn about the OOP concepts of inheritence and polymorphism
- Learn about the different types of programming errors
- Refactor code
- Use testing to identify errors
- Troubleshoot a logic error
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/J8U97_SRx7s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

So far we have created a multiple-room dungeon that the user can move between. We have also populated the dungeon with characters that the user can interact with.

During this stage we will refine our characters by:

- defining two character types:
  - friend
  - enemy
- change our current characters to one of these types of characters
- adjust our interactions to allow for different types of characters

### Class Diagram

Our new class diagram has two new classes `Enemy` and `Friend`.

![lesson 4 class diagram](./assets/lesson_4_class_diagram.png)

Notice that they both have arrows pointing towards the `Character` class, that's because they are both child classes of the parent class. A child class **inherits** all the attributes and methods from the parent class. In addition, they may have extra attributes and methods, or they can even overwrite an attribute or method they inherit. Let's look at our class diagram to see this in action.

```{admonition} Inheritance
Inheritance is a concept in object-oriented programming (OOP) that allows you to create a new class based on an existing class. Think of it like a family tree, where a child class inherits characteristics from its parent class, just like how a child inherits traits from their parents.

Inheritance makes it easier to reuse code and add new classes without having to rewrite the same information over and over again. It also makes it easier to keep track of different types of animals and what they have in common and what makes them unique.
```

#### Enemy class

The `Enemy` class:

- inherits from the `Character class` the `name`, `description`, and `conversation` attributes as well as the `describe`, `talk`, and `hug` methods.
- adds the `weakness` attribute
- overwrites the `Character` `fight` method with its own `fight` method

#### Friend class

- inherits from the `Character class` the `name`, `description`, and `conversation` attributes as well as the `describe`, `talk`, and `fight` methods.
- overwrites the `Character` `hug` method with its own `hug` method

#### Why use inheritance?

In the end our two child classes operate similarly to two classes with the following class diagrams (blue text indicates overwritten methods).

![lesson 4 child classes](./assets/lesson_4_child_classes.png)

So why don't we just two separate classes?

Remember the DRY principle? &rarr; **D**on't **R**epeat **Y**ourself?

If we have two describe methods that are exactly the same, we want to only write it once. This ensures code that is more accurate and easier to maintain.

For example, if I want to change the wording of the `describe` method, I will only need to change it in the `Character` class. The change will flow down to the `Friend` and `Enemy` classes. Similarly, if there is an error in the `talk` method, then I only need to fix it in the `Character` class.

```{admonition} OOP Terminology
OOP can have several names for the same concept. I will be consistent throughout this course, but if you use other resources, they may use different terminology.

- parent class &rarr; superclass or base class
- child class &rarr; subclass or derived class
```

Let's make these changes to the code.

## Define different character types

Open your **character.py** file and add the highlighted code below to create the `Friend` class:

### Create Friend class

```{code-block} python
:linenos:
:emphasize-lines: 30, 32-34
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

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)
```

Investigating that code:

- `class Friend(Character):` &rarr; defines the `Friend` class
  - `(Character)` &rarr; tells Python that `Character` is the parent class of `Friend`
- `def __init__(self, name):` &rarr; automatically runs when you create a `Friend` object
- `# initialise the Friend object by calling the character initialise` &rarr; method descriptive comment
- `super().__init__(name)` &rarr; this is very new
  - tells Python to run the `__init__` method of the parent class (superclass)
    - running `Character` `__init__` will inherits all the attributes and method from `Character`
  - the `__init__` of `Character` requires a `name` so we pass the `name` argument

### Create Enemy class

To create the `Enemy` class, add the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 36, 38-41
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

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

class Enemy(Character):
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
```

Now unpack the code that create the `Enemy` class:

- `class Enemy(Character):` &rarr; define the `Enemy` class as a child of the `Character` class
- `def __init__(self,name):` &rarr; automatically runs when an `Enemy` object is created
- `# initialise the Enemy object by calling the character initialise` &rarr; method descriptive comment
- `super().__init__(name)` &rarr; runs the parent class' `__init__` method which causes inheritance
- `self.weakness = None` &rarr; adds an additional `weakness` attribute to all `Enemy` objects

Now that we have two character types, we need to change the characters that we have created.

## Change character types

Return to **main.py**, and change the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 4, 24, 26, 28
# main.py

from room import Room
from character import Friend, Enemy

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

Investigating that code:

- `from character import Friend, Enemy` &rarr; we will no longer have `Character` objects, but rather `Friend` and `Enemy` objects
- `ugine = Enemy("Ugine")` &rarr; changes `Ugine` to an `Enemy` object
- `ugine.weakness = "cheese"` &rarr; `Enemy` object have a `weakness` attribute, Ugine's is cheese
- `nigel = Friend("Nigel")` &rarr; changes `Nigel` to a `Friend` object

### Refactoring testing

What we have just done is called **refactoring** our code. That is, we have made a change to our code, without changing what it does. Whenever you refactor your code the next step should always be testing, so let's test.

What do we need to test. We need to make sure that we can still have all the same interactions with both Ugine and Nigel. Draw up the testing table below and then complete it.

| Character | Interaction | Expected Result | Actual Result |
| :-------- | :---------- | :-------------- | :------------ |
| Ugine | talk | | |
| Ugine | hug | | |
| Ugine | fight | | |
| Nigel | talk | | |
| Nigel | hug | | |
| Nigel | fight | | |

If all your expected results match your actual results then there is no problems, otherwise, you need to troubleshoot where your mistakes.

## Adjusting the interactions

We want to change our interactions according to the character's type. We don't want to hug our enemies, nor do we want to fight our friends. In OOP this is called **polymorphism**.

```{admonition} Polymorphism
Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different classes to respond to the same method call in different ways. This is like having multiple people with different jobs, all able to perform the same action, but in their own unique way.

Polymorphism allows for objects of different classes to be treated as objects of their class or as objects of a parent class, without having to know the exact type of the object. This makes it easier to write generic code that can work with objects of multiple classes, making your code more flexible and adaptable to changes in the future.
```

### Adjusting the hug method

Currently, the `hug` method is inherited from the `Character` class, which basically says the character doesn't want to hug you. This is fine for enemies, so we don't have to change the `Enemy` class, but this is not what we want our friends to do, so let's change the `Friend` class.

Return to the **character.py** file and add the highlighted code:

```{code-block} python
:linenos:
:emphasize-lines: 36-38
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

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")

class Enemy(Character):
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
```

Investigating the code:

- `def hug(self):` &rarr; defines the `hug` method for the `Friend` class
  - same name as `Character` method &rarr; replaces `hug` method for all `Friend` objects
- `# the friend responds to a hug` &rarr; method's explanatory comment
- `print(f"{self.name} hugs you back.")` &rarr; display message using object's `name`

### Adjusting the fight method

Now it's time to adjust the `fight` method for our `Enemy` class. We have a simple fight mechanic. Each `Enemy` has a `weakness`. If you use their `weakness` to fight them, you win, otherwise you loose.

The highlighted code below enacts this mechanic.

```{code-block} python
:linenos:
:emphasize-lines: 47-54
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

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")

class Enemy(Character):
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None

    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
```

Investing that code:

- `def fight(self, item):` &rarr; defines the `fight` method for the `Enemy` class
  - accepts the `item` argument which is the weapon the player uses
- `# fights enemy with provided item and returns if player survives` &rarr; method's explanatory comment
- `if item == self.weakness:` &rarr; checks if the `item` is this enemy's weakness
- `print(f"You strike {self.name} down with {item}.")` &rarr; displays success message
- `return True` &rarr; informs **main.py** of victory in the fight
- `else:` &rarr; when the `item` is not this enemy's weakness
- `print(f"{self.name} crushes you. Puny adventurer")` &rarr; displays failure message
- `return False` &rarr; informs **main.py** of loss in the fight

Now that our `fight` method is ready, we need to change our fight event handler in **main.py**. Use the highlighted code below:

```{code-block} python
:linenos:
:emphasize-lines: 67-71
# main.py

from room import Room
from character import Enemy, Friend

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

Investigate the code:

- `weapon = input("What will you fight with? > ").lower()` &rarr; asks the user to input their weapon
- `if current_room.inhabitant.fight(weapon):` &rarr; checks to see if user wins the fight
  - `current_room.inhabitant.fight(weapon)` &rarr; calls the `fight` method displaying a message
  - `if` &rarr; since the `fight` method returns a Boolean indicating the player's success, we can use this to check the fight result.
- `current_room.inhabitant = None` &rarr; if the player won the fight, the room now has no character
- `else:` &rarr; if the player looses the fight
- `running = False` &rarr; set the main loop flag to `False` so the game will finish

### Testing

Now we changed both the `hug` and `fight` methods, time to do some testing. Again we will use our testing table, and focus on the code we have changed.

| Character | Interaction | Weapon | Expected Result | Actual Result |
| :-------- | :---------- | :----- | :-------------- | :------------ |
| Ugine | fight | cheese | | |
| Ugine | fight | not cheese | | |
| Ugine | hug | - | | |
| Nigel | fight | - | | |
| Nigel | hug | - | | |

### Friend fight error

Did you get the following error?

```{code-block} pseudocode
:linenos:
Traceback (most recent call last):
  File "h:\GIT\python-oop-with-deepest-dungeon\python_files\stage_4\main.py", line 66, in <module>
    if current_room.inhabitant.fight(weapon):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Character.fight() takes 1 positional argument but 2 were given
```

Why did we get the error? Let's read the error message:

- **line 2** &rarr; the error is at line 66 of **main.py**
- **line 3** &rarr; the error is contained in `if current_room.inhabitant.fight(weapon):`
- **line 4** &rarr; the error is specifically in the call to `fight`
- **line 5** &rarr; `fight` was only expecting one argument (`self`), but we gave two (`self`,`weapon`)

So let's think about this. We have two `fight` methods, which one was causing the problem? Well, Ugine worked fine, but Nigel didn't, so it must be the `fight` method for friends. 

That method is in our **character.py** file, so let's look at it.

```{code-block} python
:linenos:
:emphasize-lines: 26, 30-38, 47
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

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")

class Enemy(Character):
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None

    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
```

Looking closely at the code:

- **lines 30 - 38** &rarr; the `Friend` class does not have a `fight` method, so it is using the inherited `fight` method from the `Character` class
- **line 26** &rarr; the `Character` `fight` method only accepts one argument `(self)`, but how does this compare to the `Enemy` `fight` method?
- **line 47** &rarr; the `Enemy` `fight` method accepts two arguments `(self, item)`

Ok so we've found a discrepancy, but which one do we want to change? Remember we changed our **main.py** code to deal with fighting with a weapon, so the easiest way to solve this error is to add another argument to the `Character` `fight` method.

So make the following changes to **character.py**:

```{code-block} python
:linenos:
:emphasize-lines: 26
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

    def fight(self, item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")

class Friend(Character):
    
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

    def hug(self):
        # the friend responds to a hug
        print(f"{self.name} hugs you back.")

class Enemy(Character):
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None

    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
```

### Test again

Now we changed both the `hug` and `fight` methods, time to do some testing. Again we will use our testing table, and focus on the code we have changed.

| Character | Interaction | Weapon | Expected Result | Actual Result |
| :-------- | :---------- | :----- | :-------------- | :------------ |
| Ugine | fight | cheese | | |
| Ugine | fight | not cheese | | |
| Ugine | hug | - | | |
| Nigel | fight | - | | |
| Nigel | hug | - | | |

Wait, another problem fighting Nigel, but this one is different. There is no error message, the program just ends when you fight him. This is what we call a **logic error**.

```{admonition} Types of programming errors
There are three basic categories of programming errors:

- **syntax errors** 
    - caused by not following the programming language rules
    - Python will not even run the program, and immediately display an error message
- **runtime errors**
    - caused when Python tries to execute a command, but something is wrong
    - Python will run the program, but display an error when it comes across a runtime error
    - our `fight` method error was a runtime error
- **logic errors**
    - caused when the program does exactly what you tell it to do, but not what you want it to do
    - Python will never display an error, but the program doesn't do what you want it to do
    - these are the hardest to troubleshoot
```

Here is the interaction I got from running the code before it ended:

```{code-block}
:linenos:
You are in the laboratory
A strange odour hangs in a room filled with unknownable contraptions.
Nigel is here, a burly dwarf with golden bead in woven through his beard.
To the west is the armoury
> fight
What will you fight with? > dog
Nigel doesn't want to fight you
```

### Troubleshooting a logic error

Troubleshooting logic errors is a bit like detective work. You need to trace the program flow to work out where the error is.

So we'll start our investigation in the **main.py**. Looking at the main loop, we can be confident that the problem involves the `fight` event handler, so let's zoom into that.

```{code-block} python
:linenos:
:lineno-start: 65
:emphasize-lines: 4, 7
    elif command== "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
                running = False
        else:
            print("There is no one here to fight")
```

In the test when the user fought Nigel:

- the user got the message `Nigel doesn't want to fight you` 
  - this comes from the call to the `fight` method
  - **line 68** must of been executed
- the game ended
  - therefore `running` needed to be changed to `False`
  - **line 71** must of been executed
- the only way that **line 71** could have been executed would be if the user lost their fight with Nigel
- **line 68** determines if the user won the fight, so lets look closely at this.
  - `if current_room.inhabitant.fight(weapon):` &rarr; makes a call to the `fight` method and gets a Boolean response indicating success
  - since Nigel is a friend we need to look at the `Friend` `fight` method

So zooming into the `fight` method in the `Character` class in **character.py**:

```{code-block} python
:linenos:
:lineno-start: 26
    def fight(self, item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
```

Now I can see the problem. If **main.py** is expecting a Boolean value, it won't get one because the `Character` `fight` method doesn't return anything. 

Well, that's not entirely correct. All Python functions (including methods) return a value. If the `return` statement is not used, then the default values of `None` is returned, but why does that stop our game?

Let's zoom back in to the fight handler in **main.py** to understand.

```{code-block} python
:linenos:
:lineno-start: 65
:emphasize-lines: 4, 6-7
    elif command== "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.inhabitant.fight(weapon):
                current_room.inhabitant = None
            else:
                running = False
        else:
            print("There is no one here to fight")
```

Looking at **line 4**:

- for Nigel `current_room.inhabitant.fight(weapon)` will return `None`
- **line 4** becomes `if None:` which equates to `if False:`
- jumps to the `else` statement on **line 6**
- which means **line 7** is executed changing `running` to `False`

Ok, that all makes sense. Now we have to fix the problem. What we need is for **line 4** to receive a `True` when it calls the `Character` `fight` method.

Jump back to **character.py** and add the highlighted code below to solve our logic error.

```{code-block} python
:linenos:
:emphasize-lines: 29
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

    def fight(self, item):
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
    
    def __init__(self,name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None

    def fight(self, item):
        # fights enemy with provided item and returns if player survives
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventurer")
            return False
```

### Third test lucky

Let's test and make sure that our logic error has been solved. Again, complete the test table below.

| Character | Interaction | Weapon | Expected Result | Actual Result |
| :-------- | :---------- | :----- | :-------------- | :------------ |
| Ugine | fight | cheese | | |
| Ugine | fight | not cheese | | |
| Ugine | hug | - | | |
| Nigel | fight | - | | |
| Nigel | hug | - | | |

Hopefully all your test have passed.

## Stage 4 task

Now it is time for your to implement the **Make** phase.

Consider the additional character or characters that you have added, and change them into either a Friend, or an Enemy. Don't forget their weakness if they are an enemy.