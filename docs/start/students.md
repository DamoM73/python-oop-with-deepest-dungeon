# Introduction for Students

!!! learn "On this page we will learn"
    - what we will build in Deepest Dungeon
    - how to set up Thonny and our project folder
    - how the text on this site is formatted

!!! terms "Terminology"
    - **object-oriented programming** – a way of programming, also called OOP, where we organise our code around objects that hold data and actions together.
    - **Thonny** – a simple program for writing, running and debugging Python code, with a built-in debugger.
    - **Shell** – the panel at the bottom of Thonny where our program's output appears and where we type input.

In this project, we'll build our own text-adventure game step by step. As we create rooms, characters and items, we'll start using a way of coding called **object-oriented programming** (OOP). We don't need to know what that means yet; we'll learn it by doing.

Each stage of the game teaches a new idea, shows how it works in code, and lets us test it straight away. By the end, we'll understand how bigger programs are organised, and we'll be able to expand the dungeon with our own ideas.

## Getting set up

### Thonny

We will write our code in Python, using a program called **Thonny**.

1. Download Thonny from the [Thonny website](https://thonny.org/) and install it.
    - Why: Thonny is a simple Python editor with a built-in debugger, which we use in [Debugging with Thonny](../guides/debugging.md).
    - Expected result: Thonny opens with an empty editor at the top and the **Shell** at the bottom.

### Create a project folder

Deepest Dungeon is made of several Python files that import from each other, so they must all be saved in the same folder.

1. Go to your subject folder.
2. Create a new folder called ***deepest_dungeon***.
    - Why: when ***main.py*** imports a class, Python looks for the file in the same folder first.
    - Expected result: an empty ***deepest_dungeon*** folder, ready for Stage 1.

!!! warning "One folder, exact file names"
    Save every file for this project in ***deepest_dungeon***, and check each file name carefully. Use lower case and include the ***.py*** extension (for example ***room.py***, not ***Room.py*** or ***room***).

## Different text formatting

Throughout this site, the formatting has the following meaning:

- `text inside grey boxes` → code
- ***bold and italic text*** → file and folder names
- **bold text** → important concepts

The [Home](../index.md) page explains the coloured callouts and the code blocks.
