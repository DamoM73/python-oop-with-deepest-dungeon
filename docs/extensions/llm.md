# Extension: Character LLM

!!! learn "On this page we will learn"
    - how to run a local **large language model** (LLM) with Ollama
    - how to give each character its own personality with a custom model
    - how to call the model from our `Character` class
    - how to handle errors when a character doesn't have a model

So far, our characters say the same line every time we talk to them. We can make the game more dynamic by using a local **large language model** (LLM) to create our characters' dialogue.

## Set-up

We'll use **Ollama** to run the LLM on our own computer.

1. Download and install [Ollama](https://ollama.com/download).
    - Why: Ollama runs language models locally, so no account or internet connection is needed once a model is downloaded.
    - Expected result: Ollama opens with a chat box.
2. Choose the **gemma3:4b** model from the model list in the chat box.
3. Type "Hello" in the chat box.
    - Why: sending a first message downloads the model.
    - Expected result: after the download finishes, the model replies.

!!! warning "Choosing other models"
    We can choose other models, and this process will be mostly the same. But the bigger the model, the more memory it needs and the slower it is to reply.

    Models are measured by their number of **parameters**: a 4b model has 4 billion parameters, while a 7b model has 7 billion. We can use Ollama's chat box to try different models and see which one works best for our game.

    The list of available models is on the [Ollama website](https://ollama.com/search).

Ollama works on two levels. There's a chat window we can type in, but it's powered by a **server** running on our computer. Our game can send requests to this server and get replies from the model.

## Create custom models

Rather than using the same model for every character, we'll create a custom model for each one. This gives each character a unique personality and style. All the models use the same base model, but each has a different **system prompt**: instructions that tell the model who it is.

### The Modelfile

Let's start with a model for Nigel. Create a new file in Thonny, add the text below, and save it as ***nigel.txt*** in the ***deepest_dungeon*** folder.

```text title="nigel.txt"
FROM gemma3:4b

SYSTEM You are Nigel, a friendly, but grumpy dwarf who specialises in alchemy

PARAMETER temperature 0.2
PARAMETER num_ctx 4096
```

??? note "Code explanation"
    - `FROM` → sets the base model for our custom model. If we chose a different model, we change this to match.
    - `SYSTEM` → sets the system prompt, which gives the character its personality. We can change this to create different characters.
    - `PARAMETER temperature` → controls how creative the replies are, from 0.0 to 2.0. Higher values give more creative replies.
    - `PARAMETER num_ctx` → controls how much text the model can take into account when it replies.

!!! tip "Modelfile reference"
    More parameters and options are in the [Ollama Modelfile documentation](https://docs.ollama.com/modelfile).

### Create the model

Now we need to open a terminal to run an Ollama command.

1. In Thonny, go to **Tools** → **Open system shell…**.
    - Why: `ollama` is a command for the computer's terminal, not for Python.
    - Expected result: a terminal window opens in the folder of the current file.
2. Check that the folder in the terminal prompt is ***deepest_dungeon***.
3. Type the command below and press ++enter++.

```bash
ollama create nigel -f nigel.txt
```

??? note "Code explanation"
    - `ollama` → runs the Ollama program.
    - `create` → tells Ollama to create a new model.
    - `nigel` → names the new model. We'll always name a character's model after the character, in lower case.
    - `-f nigel.txt` → tells Ollama to build the model from the file ***nigel.txt***, which must be in the current folder.

!!! warning "Correct folder"
    If the terminal isn't in the ***deepest_dungeon*** folder, Ollama can't find ***nigel.txt***.

Go back to Ollama's chat window. Our new `nigel` model should be in the model list. Select it and chat with it to get a feel for how it replies.

### Adjust the model

To change the model, edit ***nigel.txt*** and run the `ollama create` command again. Try different system prompts and parameters to create different personalities.

## Add the model to the game

Now let's connect the model to our game. We'll use a Python library called `ollama` to send requests to the Ollama server.

### Install the ollama library

1. In Thonny, go to **Tools** → **Manage packages…**.
2. Search for `ollama` and click **Install**.
    - Expected result: Thonny shows that `ollama` is installed.

### Store each character's model name

First, each character needs an attribute that stores the name of its model. We always name the model after the character, so Nigel's model is `nigel`.

Change the dunder init method in ***character.py*** as highlighted below.

```python linenums="1" hl_lines="8"
--8<-- "examples/ext_llm/step01/character.py"
```

??? note "Code explanation"
    - **line 8** → creates the `model` attribute from the character's name in lower case, so `Nigel` uses the `nigel` model.

### The chat method

Now let's add a `chat` method to the `Character` class. It sends the player's message to the character's model and prints the reply. Add the highlighted code below.

```python linenums="1" hl_lines="3 34-40"
--8<-- "examples/ext_llm/step02/character.py"
```

??? note "Code explanation"
    - **line 3** → imports the `ollama` library.
    - **line 34** → defines the `chat` method, which takes the player's message.
    - **lines 36–39** → send the message to this character's model and store the model's reply in `response`.
    - **line 40** → prints the text of the reply.

### Talk with chat

Now let's change the `talk` command in ***main.py*** so it asks the player what they want to say, and uses `chat` instead of `talk`. Make the highlighted changes below.

```python linenums="1" hl_lines="69-70"
--8<-- "examples/ext_llm/step03/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we talk to Nigel, and when we talk to Ugine. Be specific.
    2. **Run** the program. Make sure Ollama is running first.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 69** → asks the player what they want to say to the character, and stores it in `message`.
    - **line 70** → calls the character's `chat` method with the player's message.

### Characters without a model

Talking to Nigel works, but talking to Ugine crashes the game with a `ResponseError`, because there's no `ugine` model. Rather than making every character have a model, let's make `chat` fall back to the old `talk` method when there isn't one.

Change the `chat` method in ***character.py*** as highlighted below.

```python linenums="1" hl_lines="36-43"
--8<-- "examples/ext_llm/step04/character.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we talk to Nigel, and when we talk to Ugine. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 36** → starts a `try` block, which runs the code inside it and watches for errors.
    - **lines 37–40** → send the message to the character's model, as before.
    - **line 41** → prints the reply, starting with the character's name.
    - **line 42** → catches the `ResponseError` that Ollama raises when the model doesn't exist…
    - **line 43** → …and runs the character's normal `talk` method instead.

!!! warning "Ollama must be running"
    If Ollama isn't running, `chat` raises a `ConnectionError` and the game stops. Start Ollama before playing.

## Up to you

Now it's our turn. Can you:

- create models for your other characters, each with its own personality?
- keep a conversation history for each character, so they remember what the player said earlier?
