# Glossary

This glossary lists every technical term used on this site, in alphabetical order. Each term links to the page where it is first explained. Each page lists its new terms in a Terminology callout at the top. Terms already introduced in an earlier tutorial site aren't repeated in those callouts, but they are all listed here.

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [W](#w)

## A

- **abstraction** – the OOP principle of hiding the complicated code inside an object so we only need to call its methods. ([OOP Primer](../start/oop_primer.md))
- **argument** – a value we send into a function or method when we call it. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **array** – a collection that stores lots of values of the same type. ([Stage 6: Use Items](../stages/stage_6.md))
- **attribute** – a quality that every object of a class has, such as a student's name, stored as data inside the object. ([OOP Primer](../start/oop_primer.md))

## B

- **branch** – one of the possible paths through code that uses `if`, `elif` and `else`, each of which needs to be tested. ([Stage 2: Movement](../stages/stage_2.md))
- **breakpoint** – a place we mark in our code where the debugger pauses the program. ([Debugging with Thonny](../guides/debugging.md))
- **bug** – a mistake in a program that causes unexpected results. ([Debugging with Thonny](../guides/debugging.md))

## C

- **child class** – a class based on another class that inherits all of its attributes and methods, also called a subclass or derived class. ([Stage 4: Character Types](../stages/stage_4.md))
- **class** – a blueprint that describes a kind of thing, which we use to make objects that share the same attributes and methods. ([OOP Primer](../start/oop_primer.md))
- **class diagram** – a UML (Unified Modelling Language) drawing of a class as a table with three rows: the class name, its attributes and its methods. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **class variable** – a variable that belongs to the whole class and is shared by every object made from it, so a change by one object is seen by all. ([Stage 7: Victory Conditions](../stages/stage_7.md))
- **code maintainability** – how easy our code is for other people, or our future selves, to read, understand and change. ([Stage 8: Usability](../stages/stage_8.md))
- **collection** – a data type that stores a group of values together, such as a list, tuple, set or dictionary. ([Stage 6: Use Items](../stages/stage_6.md))
- **comment** – a line starting with `#` that Python ignores, written to help humans understand the code. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **computational thinking** – breaking a real-world problem into precise, ordered and unambiguous steps that a computer can follow exactly. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **constructor** – the special `__init__` method, called the dunder init, that runs automatically each time we create an object and sets up its attributes. ([Stage 1: Create Rooms](../stages/stage_1.md))

## D

- **debugger** – a tool that runs our code one step at a time so we can see what it is doing and find mistakes. ([Debugging with Thonny](../guides/debugging.md))
- **debugging** – the process of finding and fixing bugs in a program. ([Debugging with Thonny](../guides/debugging.md))
- **dictionary** – a collection that stores values with names, called keys, so we can look each value up by its name. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **DRY** – short for Don't Repeat Yourself, the principle that we shouldn't write the same code over and over again. ([Stage 4: Character Types](../stages/stage_4.md))

## E

- **encapsulation** – the OOP principle of storing important data inside an object and getting to that data through the object's methods. ([OOP Primer](../start/oop_primer.md))
- **evaluation** – checking that a program does what it was meant to do by comparing each requirement against our test results. ([Developing a New Program](../guides/developing.md))
- **event** – something that happens while a program runs, such as a button press or two objects colliding, that the program responds to. ([Stage 2: Movement](../stages/stage_2.md))
- **event handler** – the code that responds to a particular event, such as moving the player when they type a direction. ([Stage 2: Movement](../stages/stage_2.md))
- **event-driven programming** – a style of programming where the program keeps checking for things to happen and then responds to them. ([Stage 2: Movement](../stages/stage_2.md))

## F

- **falsy** – describes a value that acts like `False` in an `if` statement, such as `None`, `0`, an empty string or an empty list. ([Stage 4: Character Types](../stages/stage_4.md))
- **flag variable** – a variable that stores `True` or `False` to control part of a program, such as `running` keeping the main loop going. ([Stage 2: Movement](../stages/stage_2.md))

## I

- **infinite loop** – a loop whose condition is always `True`, so it never stops on its own. ([Stage 2: Movement](../stages/stage_2.md))
- **inheritance** – the OOP principle of making a new class based on an existing one, so the new class gets the existing class's attributes and methods. ([Stage 4: Character Types](../stages/stage_4.md))
- **instance** – another name for an object, describing it as one particular copy made from a class. ([OOP Primer](../start/oop_primer.md))
- **instance variable** – an attribute, such as `name`, where each object has its own separate copy. ([Stage 7: Victory Conditions](../stages/stage_7.md))
- **inventory** – the collection of items a player is carrying in a game, such as the backpack in Deepest Dungeon. ([Player Class](../extensions/player.md))

## K

- **key:value pair** – one entry in a dictionary, where the key is the label we look up and the value is the information stored with it. ([Stage 1: Create Rooms](../stages/stage_1.md))

## L

- **large language model** – an AI model, also called an LLM, that has learnt from huge amounts of text and can write replies such as a character's dialogue. ([Character LLM](../extensions/llm.md))
- **library** – a collection of ready-made code that we import to use in our programs. ([Character LLM](../extensions/llm.md))
- **list** – a collection of items stored in a set order inside `[` and `]`, with commas between them. ([Stage 6: Use Items](../stages/stage_6.md))
- **local variable** – a variable that only exists inside the function that created it. ([Debugging with Thonny](../guides/debugging.md))
- **logic error** – a mistake where the code runs without crashing but doesn't do what we expected. ([Stage 4: Character Types](../stages/stage_4.md))

## M

- **main loop** – the part of a program, inside `while True:`, that repeats forever to read inputs, make decisions and control outputs. ([Stage 2: Movement](../stages/stage_2.md))
- **method** – a function that belongs to an object or value, written after a dot, such as `name.upper()`. ([OOP Primer](../start/oop_primer.md))
- **model parameter** – one of the values a language model has learnt, used to measure its size, so a 4b model has 4 billion parameters. ([Character LLM](../extensions/llm.md))
- **Modelfile** – a text file that tells Ollama how to build a custom model, including its base model, system prompt and settings. ([Character LLM](../extensions/llm.md))

## N

- **namespace** – a labelled section that keeps names organised, so each class can have its own attributes and methods without them getting mixed up. ([Stage 3: Character Creation](../stages/stage_3.md))
- **naming convention** – an agreed habit for naming things that makes code easier to read, but doesn't cause an error if we break it. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **nested if statement** – an `if` statement placed inside another `if` statement, which creates more paths that each need testing. ([Stage 6: Use Items](../stages/stage_6.md))
- **None** – a special Python value that means nothing, used when there is no value yet. ([Stage 1: Create Rooms](../stages/stage_1.md))

## O

- **object** – a thing in our program, made from a class, that holds its own data and has methods that make it do things, such as a motor or a game character. ([OOP Primer](../start/oop_primer.md))
- **object-oriented programming** – a way of programming, also called OOP, where we organise our code around objects that hold data and actions together. ([Introduction for Students](../start/students.md))
- **Ollama** – a program that runs large language models on our own computer, without needing an account or internet connection once a model is downloaded. ([Character LLM](../extensions/llm.md))
- **override** – to replace an inherited method by writing a method with the same name in the child class. ([Stage 4: Character Types](../stages/stage_4.md))

## P

- **parent class** – the existing class that a child class is based on, also called a superclass or base class. ([Stage 4: Character Types](../stages/stage_4.md))
- **polymorphism** – the OOP principle that different classes can have a method with the same name that does different things. ([Stage 4: Character Types](../stages/stage_4.md))
- **pseudocode** – a plan for our code written in plain words, without worrying about the rules of a programming language. ([Stage 1: Create Rooms](../stages/stage_1.md))

## Q

- **queue** – a collection where the first item put in is the first item taken out, like a line of people waiting. ([Stage 6: Use Items](../stages/stage_6.md))

## R

- **refactoring** – changing our code to make it better without changing what it does. ([Stage 4: Character Types](../stages/stage_4.md))
- **requirement** – something specific that a system needs to do, such as stopping when an object is within 100 mm. ([Developing a New Program](../guides/developing.md))
- **return value** – the value a function or method sends back to the code that called it. ([Stage 2: Movement](../stages/stage_2.md))
- **runtime error** – an error that happens while the program is running, which makes it crash. ([Stage 4: Character Types](../stages/stage_4.md))

## S

- **self** – the first argument of every method, which means "this object" so the method can use that object's own attributes. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **server** – a program running on a computer that receives requests, such as our game's messages, and sends back replies. ([Character LLM](../extensions/llm.md))
- **set** – a collection of values with no order and no repeats, such as the buttons being pressed right now. ([Stage 6: Use Items](../stages/stage_6.md))
- **Shell** – the panel in Thonny that shows what our program prints and any error messages. ([Introduction for Students](../start/students.md))
- **stack** – a collection where the last item put in is the first item taken out. ([Stage 6: Use Items](../stages/stage_6.md))
- **state** – the situation a program is in at a particular moment, such as which room the player is in. ([Stage 2: Movement](../stages/stage_2.md))
- **state machine** – a way of thinking about a program as always being in one state, with rules that decide the next state when an event happens. ([Stage 2: Movement](../stages/stage_2.md))
- **string** – a group of characters, like letters, numbers or symbols, inside quotation marks. ([Stage 1: Create Rooms](../stages/stage_1.md))
- **syntax error** – an error that happens when our code doesn't follow Python's rules. ([Stage 4: Character Types](../stages/stage_4.md))
- **system prompt** – the instructions that tell a language model who it is, which gives each character its own personality. ([Character LLM](../extensions/llm.md))

## T

- **temperature** – a model setting from 0.0 to 2.0 that controls how creative the replies are, with higher values giving more creative replies. ([Character LLM](../extensions/llm.md))
- **terminal** – a window where we type commands for the computer itself, such as `ollama`, rather than Python code. ([Character LLM](../extensions/llm.md))
- **testing table** – a table that lists each test with its expected result and actual result, so we can spot any differences. ([Stage 2: Movement](../stages/stage_2.md))
- **Thonny** – a program for writing, running and debugging Python code that is designed for beginners. ([Introduction for Students](../start/students.md))
- **truthy** – describes a value that acts like `True` in an `if` statement, such as a non-empty string, a non-zero number or a list with items in it. ([Stage 4: Character Types](../stages/stage_4.md))
- **try block** – code inside `try` that Python runs while watching for errors, so a matching `except` can catch an error instead of the program crashing. ([Character LLM](../extensions/llm.md))
- **tuple** – a group of values written in round brackets that works like a list but can't be changed. ([Stage 6: Use Items](../stages/stage_6.md))

## U

- **UI** – short for user interface, the screen of a program that we see and use. ([Stage 8: Usability](../stages/stage_8.md))
- **UX** – short for user experience, what it feels like to use a program, such as easy, confusing, fun or annoying. ([Stage 8: Usability](../stages/stage_8.md))

## W

- **whitespace** – the blank lines and spaces in our code, which we use to break it into clear sections. ([Stage 8: Usability](../stages/stage_8.md))
