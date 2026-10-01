# Developing a New Program

!!! learn "On this page we will learn"
    - how to define the problem our program will solve
    - how to design classes, attributes and methods before we code
    - how to build a program in small stages, testing as we go
    - how to test and evaluate our program against its requirements

Throughout Deepest Dungeon, each stage came with a plan: pseudocode, a class diagram and the code to build. That got us a working game, but when we start our own program, nobody hands us the plan. We need to figure it out ourselves.

So in this guide we'll go through the same process we used in the stages, but from the very start. We'll use a small example, a **pet shelter** program, so we can see each part of the process in action.

The process has four parts:

1. **Define** the problem.
2. **Design** the solution.
3. **Build** it in small stages.
4. **Test and evaluate** it.

## 1. Define the problem

Before we write any code, we need to be clear about what our program has to do. If we don't know where we're going, we won't know when we've got there. So we start by writing a list of **requirements**. These are short statements of what the program must do, written so we can test them later.

Our pet shelter wants a program that lets visitors see the animals and adopt one. So the requirements are:

| ID | Requirement |
| --- | --- |
| R1 | The program stores each pet's name and age. |
| R2 | Visitors can list the pets that are available for adoption. |
| R3 | Dogs and cats make different sounds. |
| R4 | Visitors can adopt a pet by name, and an adopted pet is no longer listed. |
| R5 | The program responds helpfully to unknown commands and pet names. |

!!! tip "Testable requirements"
    A good requirement is something we can check with a test. "The program is fun" can't be tested, but "the program lists every pet that hasn't been adopted" can. Give each requirement an ID (R1, R2 …), because we'll use them again when we evaluate the program.

## 2. Design the solution

### Find the classes

Now that we know what the program needs to do, we need to figure out which classes we need. A simple way to start is to look for the **nouns** in the requirements: pet, dog, cat, shelter and visitor. Each of these could be a class, so let's think about each one:

- pet → holds the details of one animal → **`Pet` class**
- dog and cat → kinds of pet that make different sounds → **child classes** of `Pet`
- shelter → holds all the pets and lets visitors adopt them → **`Shelter` class**
- visitor → the person using the program → handled by ***main.py***, not a class

### Find the attributes and methods

Next, we work out what each class needs to **know** and what it needs to **do**. Remember from the [OOP Primer](../start/oop_primer.md):

- things an object knows → **attributes** (like a pet's name and age)
- things an object does → **methods** (like listing pets or adopting one)

The **verbs** in the requirements (list, adopt, make a sound) give us a good idea of the methods we need. Putting it all together, our design looks like this:

| Class | Attributes | Methods |
| --- | --- | --- |
| `Pet` | `name: str`, `age: int`, `adopted: bool` | `describe()`, `speak()` |
| `Dog` (child of `Pet`) | inherited from `Pet` | `speak()` overrides the `Pet` version |
| `Cat` (child of `Pet`) | inherited from `Pet` | `speak()` overrides the `Pet` version |
| `Shelter` | `name: str`, `pets: list` | `add_pet(pet)`, `list_pets()`, `adopt(pet_name): Pet` |

This table holds the same information as the three rows of a UML class diagram, like the ones we used in the stages. Draw it as a class diagram for your own program, so you can check your design before you write any code.

### Plan the steps

Finally, we plan the order we'll build things in. Just like the stages, each step should give us something we can run and test, so we write the plan as pseudocode.

```text title="Pet shelter pseudocode"
- Define the Pet class with a describe method
- Define the Shelter class, add pets and list them
- Add Dog and Cat child classes that speak differently
- Add adopting, and a main loop that responds to commands
```

!!! warning "Don't skip the design"
    It's tempting to jump straight into coding. But it's much easier to change a table or a diagram than to change classes after we've built the rest of the program on top of them.

## 3. Build in small stages

Now that we have a plan, let's build it. We'll work through the pseudocode one step at a time, and run the program after each step. This makes it easier to test as we go, and if something breaks, we know it's in the code we just added.

### Step 1: the Pet class

Create a new folder for the project. Then create a new file in Thonny, add the code below and save it as ***pet.py***.

```python linenums="1" hl_lines="1 3 5-13"
--8<-- "examples/guides/pet_shelter/step01/pet.py"
```

??? note "Code explanation"
    - **line 3** → defines the `Pet` class.
    - **line 5** → defines the dunder init method, which takes the pet's name and age.
    - **lines 7–8** → store the name and age (requirement R1).
    - **line 9** → creates the `adopted` attribute, which starts as `False`.
    - **line 11** → defines the `describe` method.
    - **line 13** → prints the pet's name and age.

### Step 2: the Shelter class

Create a new file, add the code below and save it as ***shelter.py***.

```python linenums="1" hl_lines="1 3 5-19"
--8<-- "examples/guides/pet_shelter/step02/shelter.py"
```

??? note "Code explanation"
    - **line 3** → defines the `Shelter` class.
    - **line 5** → defines the dunder init method, which takes the shelter's name.
    - **line 7** → stores the shelter's name.
    - **line 8** → creates an empty list to hold the shelter's pets.
    - **line 10** → defines the `add_pet` method…
    - **line 12** → …which adds a `Pet` object to the list.
    - **line 14** → defines the `list_pets` method.
    - **line 16** → prints a heading with the shelter's name.
    - **line 17** → loops through every pet in the list.
    - **line 18** → checks whether the pet hasn't been adopted…
    - **line 19** → …and if so, calls the pet's `describe` method (requirement R2).

Now we need ***main.py*** to test both classes. Create it with the code below.

```python linenums="1" hl_lines="1 3-4 6-7 9-11 13"
--8<-- "examples/guides/pet_shelter/step02/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 3–4** → import the `Pet` and `Shelter` classes.
    - **line 7** → creates a `Shelter` object called Happy Paws.
    - **lines 10–11** → create two `Pet` objects and add them to the shelter.
    - **line 13** → lists the available pets.

### Step 3: Dog and Cat

Requirement R3 says dogs and cats make different sounds. So this is a job for **inheritance** and **polymorphism**, just like the `Friend` and `Enemy` classes in [Stage 4](../stages/stage_4.md). Go back to ***pet.py*** and add the highlighted code below.

```python linenums="1" hl_lines="15-17 20-31"
--8<-- "examples/guides/pet_shelter/step03/pet.py"
```

??? note "Code explanation"
    - **line 15** → defines a `speak` method for every pet…
    - **line 17** → …which, by default, says the pet doesn't make a sound.
    - **line 20** → defines the `Dog` class as a child of `Pet`, so it inherits every attribute and method.
    - **line 22** → overrides the `speak` method for dogs…
    - **line 24** → …so a dog says Woof!
    - **line 27** → defines the `Cat` class as a child of `Pet`.
    - **line 29** → overrides the `speak` method for cats…
    - **line 31** → …so a cat says Meow!

Then go to ***main.py*** and change the highlighted code, so we create a dog and a cat and test their sounds.

```python linenums="1" hl_lines="3 10-11 15-17"
--8<-- "examples/guides/pet_shelter/step03/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → imports the `Dog` and `Cat` classes instead of `Pet`.
    - **line 10** → creates Rex as a `Dog`.
    - **line 11** → creates Mittens as a `Cat`.
    - **line 16** → loops through every pet in the shelter…
    - **line 17** → …and calls its `speak` method. Each pet uses its own class's version, which is polymorphism.

### Step 4: adopting and the main loop

Now let's add adopting (requirement R4). Return to ***shelter.py*** and add the highlighted method below.

```python linenums="1" hl_lines="21-27"
--8<-- "examples/guides/pet_shelter/step04/shelter.py"
```

??? note "Code explanation"
    - **line 21** → defines the `adopt` method, which takes the name the visitor typed.
    - **line 23** → loops through every pet in the shelter.
    - **line 24** → checks whether this pet's name matches (ignoring capital letters) and the pet is still available…
    - **line 25** → …and if so, marks it as adopted…
    - **line 26** → …and returns the pet.
    - **line 27** → returns `None` if no available pet has that name.

Finally, we need a way for the visitor to use the program. Return to ***main.py*** and replace the test code with a main loop, like the one we built in [Stage 2](../stages/stage_2.md).

```python linenums="1" hl_lines="12 15-34"
--8<-- "examples/guides/pet_shelter/step04/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 12** → adds a third pet, so we can test adopting more than one.
    - **line 15** → creates the flag variable that keeps the main loop running.
    - **line 16** → starts the main loop.
    - **line 17** → asks the visitor for a command and turns it into lower case.
    - **lines 19–20** → list the available pets when the command is `list`.
    - **line 21** → checks whether the command is `adopt`.
    - **line 22** → asks which pet the visitor wants.
    - **line 23** → calls `adopt`, which returns the pet or `None`.
    - **line 24** → checks whether a pet was returned…
    - **lines 25–26** → …and if so, confirms the adoption and lets the pet speak…
    - **lines 27–28** → …otherwise tells the visitor that pet isn't available (requirement R5).
    - **lines 29–30** → stop the main loop when the command is `quit`.
    - **lines 31–32** → tell the visitor the valid commands when they type anything else (requirement R5).
    - **line 34** → prints a goodbye message after the loop ends.

## 4. Test and evaluate

### Test

Just like in the stages, we need to test every branch of our code. So let's draw up a testing table. Run each test and fill in the actual results.

| Test | Input | Expected result | Actual result |
| --- | --- | --- | --- |
| 1 | `list` | Rex, Mittens and Biscuit are listed | |
| 2 | `adopt`, then `rex` | "You adopted Rex!" then "Rex says Woof!" | |
| 3 | `list` | Mittens and Biscuit are listed; Rex isn't | |
| 4 | `adopt`, then `Rex` | "Rex isn't available." | |
| 5 | `adopt`, then `fish` | "fish isn't available." | |
| 6 | `adopt`, then `MITTENS` | "You adopted Mittens!" then "Mittens says Meow!" | |
| 7 | `feed` | "Please type list, adopt or quit." | |
| 8 | `quit` | "Thanks for visiting Happy Paws." and the program ends | |

If any actual result doesn't match its expected result, we've got a bug. Use the [debugger](debugging.md) to track it down.

### Evaluate

Testing tells us whether the code works, but that's not the whole story. We also need to check that the program does what it was meant to do. This is called **evaluating**. So we go back to our requirements, and check each one against our test results.

| ID | Requirement | Met? | Evidence |
| --- | --- | --- | --- |
| R1 | Stores each pet's name and age | Yes | Test 1 shows names and ages |
| R2 | Lists available pets | Yes | Tests 1 and 3 |
| R3 | Dogs and cats make different sounds | Yes | Tests 2 and 6 |
| R4 | Adopt by name; adopted pets aren't listed | Yes | Tests 2, 3 and 4 |
| R5 | Helpful responses to unknown input | Yes | Tests 5 and 7 |

Evaluating is also a good time to think about what could be better. For example, the shelter can't take in new pets while the program is running, and the visitor can't tell whether a pet is a dog or a cat. These would make good features for the next version.

## Your turn

Now it's your turn to use the same process for your own program. Work through this checklist as you go:

1. I've written my requirements as a numbered list of testable statements.
2. I've found my classes from the nouns, and my methods from the verbs.
3. I've drawn a class diagram (or table) with every class's attributes and methods.
4. I've written pseudocode that splits the build into small steps.
5. I've run and tested my program after every step.
6. I've completed a testing table that covers every branch.
7. I've evaluated my program against each requirement, and noted improvements.

!!! tip "Ideas for your own program"
    Choose something with two or three kinds of objects that work together, for example a library (books and members), a canteen (menu items and orders) or a sports team (players and matches). Keep your first version small. You can always add more features later, just like we did with Deepest Dungeon.
