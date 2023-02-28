# OOP Primer

This course will teach you about using Object orientated programming (OOP) in Python. Before we explore using OOP in Python, we need to cover some of the basic concepts you will encounter during the course.

## What is OOP?

OOP is a style of programming which organises software design around representations of data called objects. You can imagine an object as a digital model of some &lsquo;thing&rsquo;.

OOP involves various models interacting with each other. The best way to get your head around this concept is to use a real world example we all understand. Let's say we want to represent students and the subjects they're enrolled in.

## What is an object?

The first &lsquo;thing&rsquo; in our example is a student. &lsquo;Things&rsquo; in OOP are called **classes**. So your program would have a *student class*, and each student in your program will be represented using this class.

Let's use this image to represent our student class:

![student](./assets/oop_intro_1.png)

All students have some &lsquo;things&rsquo; in common, a shared list of qualities. In OOP these qualities are called **attributes**.

In addition, all students will do similar &lsquo;things&rsquo;, a shared list of actions. In OOP these actions are called **methods**.

So below is our student **class** with their respective **attributes** (yellow) and **methods** (blue). Think of it as a blueprint for all the examples of students that we will have in our program. *Every* student will have *all* the attributes and can access *all* the methods.

![student class with attributes and methods](./assets/oop_intro_4.png)

Now that the program has a blueprint for students (the student class), different **instances** of students can be created. Below is an example of six instances of the *student class*. An instance of a class is called an **object**. You can see that each **object** gets their **attributes** and **methods** from the **class**.

![student objects](./assets/oop_intro_5.png)

## How does an Object Orientated Program work?

An Object orientated program works through manipulating the **objects** via their **methods**. For example, using the *Change name* method to change the value stores in the student's name attribute.

Objects can also interact with each other. To explain this let's introduce some subject objects to our example.

![subject objects](./assets/oop_intro_10.png)

So to enrol a student in a subject we need to use the subject's *Enrol student* method. Below is an example of enrolling Peter in English.

![subject objects](./assets/oop_intro_11.png)

## Encapsulation and Abstraction

Notice the code written under the last diagram? This is how the code would look in Python. Does is look familiar? Does is remind of code like `my_ttl.forward(10)`? That's because Python is a object orientated language. 

Consider the code below:

```{code-block} python
:linenos:
:emphasize-lines: 3, 5
import turtle

my_ttl = turtle.Turtle()

my_ttl.forward(100)
```

`my_ttl = turtle.Turtle()` creates a new object called `my_ttl` by using the `Turtle` class from the `turtle` library.

`my_ttl.forward(100)` uses the `forward` method the `my_ttl` object got from the `Turtle` class, to make `my_ttl` move forward.

All the time you have been programming in Python you have been using an object orientated language, you just didn't know it. This is a perfect example of two main principles of OOP, **encapsulation** and **abstraction**.

**Encapsulation** means that important information is contained within the object. Anything outside of the object can only access its information through call its methods. For example, the `my_ttl` has both and `x` coordinate value, but you can only access it through the `xcor()` method.

**Abstraction** means that the internal code of the object is also hidden from the outside and is also accessed through calling methods. For example, you don't not see the internal workings that changes `my_ttl` coordinates when you call the `forward()` method.

## Other OOP Principles

OOP has two more principles, **Inheritance** and **Polymorphism**. We will learn about these later in the course.
