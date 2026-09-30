# Stage 8: Usability

!!! learn "In this lesson we will learn"
    - what UI and UX mean and why they matter to the people who use our program
    - how to add features that help the user, like a help command and clearer messages
    - how comments and neat code make a program easier to read and fix
    - how to tidy a program by removing code we don't need

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lHSCfn0U45k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Introduction

Our dungeon works, but before we finish we need to make it easier to use and clean up the code.

### Pseudocode

```text title="Stage 8 pseudocode"
- Add a help command
- Make the program easier to read and use
- Add a goodbye message at the end
- Write more comments in the code
- Delete code we don't need
- Make our spacing neat and consistent
```

## Help command

We know the commands because we wrote the code, but a new player won't know what they're allowed to type. Right now, if they type something wrong, the program just says "I don't understand.", which isn't very helpful.

To fix this, let's add a `help` command that lists all the commands. Players won't know `help` exists unless we tell them, so we'll also change the final `else` to remind them to type `help` when they get something wrong.

Add the highlighted code to ***main.py***.

```python linenums="1" hl_lines="117-124 128"
--8<-- "examples/stage_8/step01/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 117** → checks whether the player's command was `help`…
    - **lines 118–124** → …and prints how to move and the list of commands.
    - **line 128** → tells the player to type `help` when their command isn't recognised.

## Improve the UI and UX

Even though our program looks simple, people still have to use it, so we need to think about its UI and UX: how it looks and how easy it is to use.

!!! tip "UI and UX"
    **UI** means **user interface**. It's what we actually see on the screen when we use an app or website, such as buttons, menus, icons and colours. UI is about making everything look clear and easy to use.

    **UX** means **user experience**. It's about what it *feels* like to use the app: easy, confusing, fun or annoying. UX is about making sure the user has a smooth and enjoyable time using the program.

We've already fixed some UI and UX issues by adding the `help` command. Now play the game and see if you can spot anything else that feels confusing.

You might notice that after we type a command, the game shows the response and then instantly prints the room description again. This makes it easy to miss what the game just told us. To fix that, we'll show the response and then make the player press ++enter++ before the game continues.

Add the highlighted code below.

```python linenums="1" hl_lines="129"
--8<-- "examples/stage_8/step02/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 129** → uses `input` as a little trick to pause the game. `input` waits until the player presses ++enter++, and because we don't store what they type, it's ignored. It's indented one level, so it runs at the end of every loop, whatever the command was.

## Farewell message

When the game ends, it just stops straight away, with no message whether we win or lose. To make the ending feel nicer, let's add a goodbye message.

Add the highlighted code below.

```python linenums="1" hl_lines="130"
--8<-- "examples/stage_8/step03/main.py"
```

??? note "Code explanation"
    - **line 130** → prints a goodbye message. It isn't indented, so it's outside the main loop and only runs once the loop has stopped.

## In-code comments

We already have some comments that explain what parts of the code do, but most of the main loop doesn't have any. Adding comments there makes the code easier to read and easier to fix later.

!!! tip "Code maintainability"
    **Code maintainability** means making our code easy to understand, fix and update later. If our code is neat, well organised and has clear comments, we or someone else can quickly work out how it works. This makes it easier to find bugs, add new features and change things without breaking the program.

Let's start with ***main.py***. Add the highlighted comments.

```python linenums="1" hl_lines="70 73 79 85 107 115 123 132 135"
--8<-- "examples/stage_8/step04/main.py"
```

When we make classes, it's a good idea to add a comment explaining what each method does. If we check ***room.py***, ***item.py*** and ***character.py***, we'll see we've already done this.

## Remove unused code

Remember the code in ***main.py*** that we turned into a string? We don't need it any more. **Delete** the highlighted lines below.

```python linenums="1" hl_lines="52-57"
--8<-- "examples/stage_8/step05/main.py"
```

## Final code

**Whitespace** is the blank lines and spaces in our code. We can use blank lines to break our code into clear sections, which makes it easier to read.

Tidy your code so it looks the same as the code below.

### ***main.py***

```python linenums="1"
--8<-- "examples/stage_8/step06/main.py"
```

### ***room.py***

```python linenums="1"
--8<-- "examples/stage_8/step07/room.py"
```

### ***character.py***

```python linenums="1"
--8<-- "examples/stage_8/step08/character.py"
```

### ***item.py***

```python linenums="1"
--8<-- "examples/stage_8/step09/item.py"
```

## Final make

The stages are finished. Now it's our turn to make the dungeon our own by adding new features. The [Extension Ideas](../extensions/extension_ideas.md) page has some inspiration, and the [Extensions](../extensions/player.md) walk through two bigger changes.

There's at least one logic mistake hidden in the final code. We'll need to test the game to find it, and work out how to fix it. Use the [debugger](../guides/debugging.md) to help.

Good luck on your adventure.
