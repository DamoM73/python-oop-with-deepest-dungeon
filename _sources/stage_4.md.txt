# Stage 4 - Character Types

```{topic} Learning Intentions
In this lesson you will:
* understand what inheritance is and how child classes get attributes and methods from a parent class
* explain polymorphism and how different classes can use the same method in different ways
* identify the three types of programming errors: syntax, runtime, and logic errors
* refactor code to use child classes without changing behaviour
* test and troubleshoot code by comparing expected and actual results to find and fix logic and runtime errors
errors 
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/J8U97_SRx7s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

So far we have created a multiple-room dungeon that the user can move between. We have also populated the dungeon with characters that the user can interact with.

During this stage we will refine our characters by:

```{admonition} Pseudocode
:class: pseudocode
- define two character types:
  - friend
  - enemy
- change our current characters to one of these types of characters
- adjust our interactions to allow for different types of characters
```

### Class Diagram

The class diagram now shows two new classes: `Enemy` and `Friend`.

![lesson 4 class diagram](./assets/lesson_4_class_diagram.png)

Both classes have arrows pointing to `Character` because they are child classes. This means they **inherit** everything the `Character` class has. They can also add new features or replace methods they inherited.

The diagram shows how these new classes build on top of the original `Character` class.

```{admonition} Inheritance
:class: note
Inheritance in OOP means making a new class that is based on an existing one. It’s like a family tree: a child class gets traits from its parent class.

This helps you avoid rewriting the same code and makes it easier to organise different types of things by what they share and what makes them different.
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

The two child classes end up working a lot like the classes shown in the diagrams.

![lesson 4 child classes](./assets/lesson_4_child_classes.png)

But why not just make two completely separate classes? Because of the DRY rule: **Don’t Repeat Yourself**.

If both classes use the same `describe` method, it’s better to write it once in the `Character` class. Then `Friend` and `Enemy` automatically get it. This makes the code easier to fix and update.

If you ever change the `describe` or `talk` method, you only change it in one place — the `Character` class — and both child classes get the updated version.

```{admonition} OOP Terminology
:class: note
In OOP, different books and websites sometimes use different words for the same idea. Here are the main ones you might see:

* **parent class** can also be called a **superclass** or **base class**
* **child class** can also be called a **subclass** or **derived class**
```

Let's make these changes to the code.

## Define different character types

Open your ***character.py*** file and add the highlighted code below to create the `Friend` class:

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

```{admonition} Code Explaination
* `class Friend(Character):` &rarr; creates a new class called `Friend`, and the `(Character)` shows that `Friend` comes from the `Character` parent class.
* `def __init__(self, name):` &rarr; is a special method that runs automatically whenever you make a new `Friend` object.
* The comment explains that this sets up the `Friend` object using the parent class.
* `super().__init__(name)` &rarr; tells Python to run the parent class’s `__init__` method first. This gives `Friend` all the attributes and methods that `Character` has. Because `Character` needs a `name`, we pass the `name` through.

```

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

Now unpack the code that creates the `Enemy` class:

```{admonition} Code Explaination
* `class Enemy(Character):` &rarr; creates the `Enemy` class and shows it is a child of the `Character` class.
* `def __init__(self, name):` &rarr; runs automatically when you make a new `Enemy` object.
* The comment explains that this sets up the `Enemy` by using the parent class first.
* `super().__init__(name)` &rarr; runs the parent class’s `__init__` so the `Enemy` gets all the usual character features.
* `self.weakness = None` &rarr; adds a new attribute called `weakness` that every enemy will have.
```

Now that we have two character types, we need to change the characters that we have created.

## Change character types

Return to ***main.py***, and change the highlighted code:

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

```{admonition} Code Explaination
* `from character import Friend, Enemy` &rarr; means we’re now creating characters as either `Friend` or `Enemy`, not as basic `Character` objects anymore.
* `ugine = Enemy("Ugine")` &rarr; creates Ugine as an `Enemy`.
* `ugine.weakness = "cheese"` &rarr; sets Ugine’s weakness, because all enemies have a `weakness` attribute.
* `nigel = Friend("Nigel")` &rarr; creates Nigel as a `Friend`.
```

### Refactoring testing

Refactoring connects directly to the code we just changed. You updated your code to use the new `Friend` and `Enemy` classes instead of the original `Character` class. Now you need to make sure those changes didn’t break anything.

Refactoring means you changed *how* the code is written, not *what* it should do. So the next job is to test it. Check that Ugine and Nigel still behave the same as before by filling in the testing table.


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

We want the game to react differently depending on the type of character. You shouldn’t hug an enemy, and you shouldn’t fight a friend. When different classes respond to the same action in different ways, this is called **polymorphism**.

```{admonition} Polymorphism
:class: note
Polymorphism in OOP means different classes can use the same method but do different things with it. It’s like asking different people to “work” — they all do it, but the way they work depends on their job.

This lets your code treat different objects in a similar way, even if they aren’t the same type. It makes your programs easier to write, easier to update, and more flexible when things change.
```

### Adjusting the hug method

Right now, the `hug` method comes from the `Character` class, and it always says the character doesn’t want to hug you. That’s okay for enemies, so we’ll leave them as they are. But friends *should* hug you back, so we need to change the `Friend` class to make that happen.

Return to the ***character.py*** file and add the highlighted code:

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

```{admonition} Code Explaination
* `def hug(self):` &rarr; creates a new `hug` method for the `Friend` class. Because it has the same name as the one in `Character`, it replaces the old version for all friends.
* The comment explains what the method is meant to do.
* `print(f"{self.name} hugs you back.")` &rarr; shows a message using the friend’s name.
```

### Adjusting the fight method

Now we need to update the `fight` method for the `Enemy` class. The fighting system is simple: every enemy has a **weakness**. If you fight them using their weakness, you win. If you use anything else, you lose.

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

```{admonition} Code Explaination
* `def fight(self, item):` &rarr; creates the `fight` method for enemies. The `item` is the weapon the player chooses.
* The comment explains that this method checks the weapon and returns whether the player survives.
* `if item == self.weakness:` &rarr; checks if the weapon matches the enemy’s weakness.
* `print(f"You strike {self.name} down with {item}.")` &rarr; shows a message if you win.
* `return True` &rarr; tells ***main.py*** that the player won the fight.
* `else:` &rarr; runs when the weapon is not the enemy’s weakness.
* `print(f"{self.name} crushes you. Puny adventurer")` &rarr; shows the losing message.
* `return False` &rarr; tells ***main.py*** that the player lost.
```

Now that the `fight` method is finished, we need to update the fight section in ***main.py*** so the game uses the new system. Replace that part of the code with the updated version shown.

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

Investigate the code:

```{admonition} Code Explaination
* `weapon = input("What will you fight with? > ").lower()` &rarr; asks the player to type the weapon they want to use.
* `if current_room.character.fight(weapon):` &rarr; checks if the player wins the fight.
  * `current_room.character.fight(weapon)` &rarr; calls the `fight` method, which also prints the fight message.
  * The `if` works because `fight` returns `True` if you win and `False` if you lose.
  * You don't have to say `== true` or `== false` because the `if` statement checks for truthy or falsy values
* `current_room.character = None` &rarr; removes the character from the room when the player wins.
* `else:` &rarr; runs if the player loses the fight.
* `running = False` &rarr; stops the main loop, which ends the game.
```

```{admonition} Truthy and Falsy Values
:class: note
In Python, some values act like **True** and some act like **False** when used in an `if` statement, even if they aren’t actually the words `True` or `False`. These are called **truthy** and **falsy** values. 

Truthy values include things like non-empty strings, non-zero numbers, and lists with items in them, while falsy values include `None`, `0`, empty strings, empty lists, and `False` itself. 

This matters because when you write something like `if current_room.character:`, Python checks whether that value is truthy (meaning it exists or has content) or falsy (meaning it’s empty or `None`), and runs the code based on that.
```

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

```{code-block} error
:linenos:
Traceback (most recent call last):
  File "h:\GIT\python-oop-with-deepest-dungeon\python_files\stage_4\***main.py***", line 66, in <module>
    if current_room.character.fight(weapon):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Character.fight() takes 1 positional argument but 2 were given
```

Why did we get the error? Let's read the error message:

- **line 2** &rarr; the error is at line 66 of ***main.py***
- **line 3** &rarr; the error is contained in `if current_room.character.fight(weapon):`
- **line 4** &rarr; the error is specifically in the call to `fight`
- **line 5** &rarr; `fight` was only expecting one argument (`self`), but we gave two (`self`,`weapon`)

So let's think about this:
1. We have two `fight` methods, which one was causing the problem? 
2. Ugine's fight worked fine, but Nigel didn't, so it must be the `fight` method for friends.
3. That method is in our ***character.py*** file, so let's look at it.

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

4. Looking closely at the code:

   * **lines 30 - 38** &rarr; the `Friend` class does not have a `fight` method, so it is using the inherited `fight` method from the `Character` class in **line 26**.
   * **line 26** &rarr; the `Character` `fight` method only accepts one argument `(self)`, but how does this compare to the `Enemy` `fight` method in **line 47**?
   * **line 47** &rarr; the `Enemy` `fight` method accepts *two* arguments `(self, item)`

We’ve found the problem, but now we need to decide what to fix. Since we updated ***main.py*** so that fighting always uses a weapon, the simplest solution is to update the `Character` class’s `fight` method so it also accepts the extra argument.

So make the following changes to ***character.py***:

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

There’s another problem when you try to fight Nigel, but this time it’s different. You don’t get an error message—the program just stops. This type of mistake is called a **logic error**.

```{admonition} Types of programming errors
:class: note
There are three main types of programming errors:
* **Syntax errors** happen when you break the rules of Python. The program won’t run at all and will instantly show an error.
* **Runtime errors** happen while the program is running. Python tries to do something but can’t, so it crashes and shows an error. The earlier fight error was one of these.
* **Logic errors** happen when the program runs without crashing, but it doesn’t do what you meant. Python won’t warn you, so these are the hardest to find.
```

This is what the game showed right before the program suddenly stopped:

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

Fixing logic errors is kind of like being a detective. You have to follow what the program is doing step by step to spot where things go wrong.

We’ll start by checking ***main.py***. Since the issue happens when you try to fight Nigel, the problem is probably in the part of the main loop that handles the `fight` command, so that’s the section we need to look at closely.

```{code-block} python
:linenos:
:lineno-start: 65
:emphasize-lines: 4, 7
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                current_room.character = None
            else:
                running = False
        else:
            print("There is no one here to fight")
```

In the test when we fought Nigel:

* We saw the message `Nigel doesn't want to fight you`, which means the `fight` method ran and **line 68** was used.
* Then the game ended, so `running` must have been set to `False`, which happens on **line 71**.
* **Line 71** only runs if the player loses the fight with Nigel.
* **Line 68** is where the program checks if the player won or lost, using `if current_room.character.fight(weapon):`, which calls the `fight` method and expects a `True` or `False` answer.
* Because Nigel is a friend, we now need to look at the `fight` method that friends use, which is in the `Character` class.

So zooming into the `fight` method in the `Character` class in ***character.py***:

```{code-block} python
:linenos:
:lineno-start: 26
    def fight(self, item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
```

Here’s the issue: ***main.py*** expects the `fight` method to return a True or False value, but the `Character` class’s `fight` method doesn’t return anything.

In Python, if a function doesn’t have a `return` statement, it still returns something — the default value `None`.

The problem is that `None` counts as `False` in an `if` statement, so the game thinks the player lost the fight, which makes the program end.

Let's zoom back in to the fight handler in ***main.py*** to understand.

```{code-block} python
:linenos:
:lineno-start: 65
:emphasize-lines: 4, 6-7
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                current_room.character = None
            else:
                running = False
        else:
            print("There is no one here to fight")
```

Looking at **line 4**:

* When fighting Nigel, `current_room.character.fight(weapon)` returns `None`.
* That means the line becomes `if None:`, which works the same as `if False:`.
* So the program skips the “win” part and goes straight to the `else` on line 6.
* Line 7 then runs and sets `running` to `False`, which ends the game.

So now we know what’s happening. To fix it, the `Character` class’s `fight` method needs to return `True` so line 4 treats it as a win. 

Update the method in ***character.py*** to solve the logic error.

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

```{admonition} Code Explaination
* **line 29** now returns `True` when you fight a friend, which means the **line 71** of the ***main.py*** `running == False` does not run.
```

### Third test lucky?

Let's test and make sure that our logic error has been solved. Again, complete the test table below.

| Character | Interaction | Weapon | Expected Result | Actual Result |
| :-------- | :---------- | :----- | :-------------- | :------------ |
| Ugine | fight | cheese | | |
| Ugine | fight | not cheese | | |
| Ugine | hug | - | | |
| Nigel | fight | - | | |
| Nigel | hug | - | | |

Were you able to hug Nigel after fighting him? Probably not. That’s because the game treated the fight as a win, so it deleted Nigel from the room. We need to fix that so friends don’t disappear when you “fight” them.

In ***main.py*** adjust the highlighted code below.

```{code-block} python
:linenos:
:lineno-start: 65
:emphasize-lines: 5,6
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            if current_room.character.fight(weapon):
                if isinstance(current_room.character, Enemy):
                    current_room.character = None
            else:
                running = False
        else:
            print("There is no one here to fight")
```

```{admonition} Code Explaination
* `if isinstance(current_room.character, Enemy):` &rarr; checks whether the character in the room is an **Enemy**.
  * This is `True` only when the character was created using the `Enemy` class.
```

### Final test

Finally check that you can attempt to fight Nigel, and then still hug him afterwards.

## Stage 4 task

Now it is time for your to implement the **Make** phase.

Consider the additional character or characters that you have added, and change them into either a Friend, or an Enemy. Don't forget their weakness if they are an enemy.

