# Extension - Character LLM

```{topic} Learning Intentions
In this lesson you will:
- Understand how to integrate a local Large Language Model (LLM) into your game.
```

In the previous sections, we have been using a simple function to generate dialogue for our characters. However, we can make our game more dynamic and engaging by using a local Large Language Model (LLM) to provide the dialogue for our characters.

## Setup

We will be using Ollama to run our local LLM. To do this you will need to install Ollama and downoad a model. 

1. Download and install [Ollama](https://ollama.com/download)
2. Start Ollama and Then choose the **Gemma3:4b** model from the drop down in the chat box.
3. Type "Hello" in the chat box to trigger the model download.

```{admonition} Choosing other models
:class: warning
You can choose other models, and this process will be mostly the same, but be aware that the bigger the model, the more memory it will require and the slower it will be in generating responses. 

Models are measured by the number of parameters they have, so a 4b model has 4 billion parameters, while a 7b model has 7 billion parameters. You can use the Ollama UI to experiment with different models and determine which one works best for your game.

The list of available models can be found [here](https://ollama.com/search).
```

Ollama works on two levels. There is a UI to chat in, but this UI is supported by a local server running on your laptop. We can send requests to this server to get responses from the model, which is how we will integrate it into our game.

## Creating custom models

Rather than the same llm for all our chartacters, we will create custom models for each character. This will allow us to give each character a unique personality and style of dialogue. All models will be based on the same base model, but we will use different system prompts to create different personalities for each character.

### Modelfile

We will start with and exmaple model for Nigel.

To do this we need to create a new file in your ***deepest_dungeon*** directory, then add this code to it:

```{code-block}
:linenos:
FROM gemma3:4b

SYSTEM You are Nigel, a friendly, but grumpy dwarf who specialises in alchemy

PARAMETER temperature 0.2
PARAMETER num_ctx 4096
```

```{admonition} Code Explaination
- **FROM** &rarr; this is the base model for our custom model. If you chose a different model, you will need to change this to match the model you chose.
- **SYSTEM** &rarr; this is the system prompt that will be used to generate responses for this character. You can change this to create different personalities for your characters.
- **PARAMETER** &rarr; these are parameters that control how the model generates responses. 
    - **temperature** controls how creative the responses are, with higher values resulting in more creative responses. It can range between 0.0 and 2.0
    - **num_ctx** parameter controls how much of the conversation history the model can see when generating a response.
```

Save the file as ***nigel.txt*** in the Deepest Dungeon directory.

```{admonition} ModelFile Reference
:class: note
Additional parameters and options for the model can be found in the [Ollama documentation](https://docs.ollama.com/modelfile).
```

### Create the model

Now in Thonny we need to launch your computer's terminal. 

You can do this by:
1. going to the **Tools** menu
2. selecting **Open system shell**. 
3. Then type the following command to build your custom model:

```{admonition} Correct directory
:class: warning
Make sure the directory in your terminal prompt is the ***deepest_dungeon*** directory.
```

```bash
ollama create nigel -f nigel.txt
```

```{admonition} Code Explaination
- **ollama** &rarr; calls the ollama server rnning on your laptop
- **create** &rarr; this is the command to create a new model
- **nigel** &rarr; this is the name of the new model. You can change this to match the name of your character.
- **-f** &rarr; this flag tells ollama to use a file to create the model
- **nigel.txt** &rarr; this is the file that contains the instructions for creating the model. This file needs to be in the current directory.
```

You can now go back to the Ollama UI and you should see your new model in the drop down menu. Select the model and chat with it to get a feel for how it responds.

### Audjusting the model

If you want to change the model, you can edit the ***nigel.txt*** file and then run the `ollama create` command again to update the model. You can experiment with different system prompts and parameters to create different personalities for your characters.

## Integrating the model into the game

Now to integrate the model into our game. We will be using a Python library called `ollama` to send requests to the Ollama server and get responses from our model. 

### Setup

To install this package in Thonny

1. go to the "Tools" menu
2. select "Manage packages" Then search for "ollama" and click "Install".

### Using the model

First you will need to create a new attribute in your character class to store the name of the model that character will use. To make our life easier, we will add always call our models the same as the character, so for Nigel we will call his model "nigel". 

Change your characters dunder init method to look like this:

```{code-block} python
:linenos:
:
:emphasize-lines: 8
# character.py

class Character():
    
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.model = name.lower()
        self.description = None
        self.conversation = None
```

Now we need to create a new method in our character class to send requests to the Ollama server and get responses from our model. We will call this method `chat`.

```{code-block} python
:linenos:
:emphasize-lines: 3, 34-40
# character.py

import ollama

class Character():
    
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.model = name.lower()
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

    def fight(self,item):
        # the character response to a threat
        print(f"{self.name} doesn't want to fight you")
        return True
    
    def chat(self, message):
        # use the character's model to have a conversation
        response = ollama.generate(
            model='self.model',
            prompt=message
        )
        print(response['response'])
```

## Up to you

Now you will need to adjust your program so that when you talk to a character, it uses the `chat` method instead of the `talk` method. You will also need to make other models for your other characters. You might want to consider how to maintain a conversation history for each character.
