# Extension Ideas

!!! learn "On this page we will learn"
    - ideas for new features that make the dungeon our own
    - which parts of our code each idea would change

Now that we've finished Deepest Dungeon, it's time to make it ours by extending it. Below are some ideas for features we could add. To build a completely new program instead, see [Developing a New Program](../guides/developing.md).

## The dungeon

- add more rooms
- add more directions to travel (for example up and down)
- add rooms with locked doors

## The characters

- give characters more than one line of conversation (try choosing randomly from a list)
- make more character types (there are more than just friends and enemies)
- use a local LLM to create the characters' dialogue (see [Character LLM](llm.md))

## The player

Once we have a [Player class](player.md), we can easily add more attributes. For example:

- give the player money so they can buy items
- let the player equip weapons or armour

## The fight

At the moment, fights are over very quickly. We could make them more interesting by:

- giving the player and enemies health that goes down during a fight
- making different items cause different damage
- giving each character their own losing message

## The UI

Text-based games can look quite plain. There are libraries that make the terminal look more exciting.

!!! warning "Challenging"
    These libraries are challenging to use, and some features don't display in Thonny's Shell, so we may need to run our game in a terminal.

- [Rich](https://rich.readthedocs.io/en/stable/introduction.html)
- [Textual](https://textual.textualize.io/)
