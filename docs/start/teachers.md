# Introduction for Teachers

## Why teach object-oriented programming?

Introducing students to **object-oriented programming** (OOP) sets them up with skills that underpin modern software development.

OOP is a core programming paradigm used across industry. Teaching it early helps students write code that is cleaner, more secure, easier to maintain and simpler to extend.

This matters in Python. While Python supports other styles, it is fundamentally object-oriented. Most Python libraries and community resources assume readers understand classes, objects and methods. Once students grasp OOP, they can make full use of the wider Python ecosystem.

Senior secondary Digital Technologies subjects increasingly expect students to apply OOP in their solutions, which makes early exposure even more important.

A strong grounding in OOP also prepares students for further study. Tertiary programming courses expect students to work with object-oriented design from day one, and delaying exposure only makes that transition harder.

## Why this site?

I developed this site for my secondary Digital Technologies students. It's based on the resources that finally helped me learn to code effectively with OOP.

It supports my classroom practice by addressing two common issues:

- students arrive with very different levels of coding experience
- students who miss lessons and need to catch up

My teaching approach is:

- Students work through the site at their own pace.
    - Students who move quickly can progress ahead.
    - The [Extensions](../extensions/player.md) are there for students who finish early.
- I live code each stage with the class.
    - This sets the minimum expected progress.
    - Students who fall behind what's covered in class use the site to catch up.
- Any student who misses lessons or needs extra time can use this site to get back on track.

There are eight stages. Most stages take one or two lessons.

!!! warning "Corrections"
    If you find any errors in this work, please [raise an issue](https://github.com/DamoM73/python-oop-with-deepest-dungeon/issues) on GitHub so I can fix it.

## Videos

Each stage has a video. The videos were made before the website. Their content is similar, but the site gives more detail.

## Teacher resources

The source code for this site is on [GitHub](https://github.com/DamoM73/python-oop-with-deepest-dungeon). The content is licensed under CC BY-NC-SA 4.0 and the code under GPLv3. You are free to download and reuse it within those licences.

The [tutorial files zip](../downloads/deepest_dungeon.zip) has the finished code for every stage and extension. Each stage folder is a complete, runnable checkpoint, so students who fall behind can start the next stage from it.

## The hidden logic mistake

The Stage 8 final code deliberately contains one logic mistake for students to find with the debugger: after a movement command, ***main.py*** always prints `You travel <direction>`, even when the move fails and the game has just said "You can't go that way". The fix is to only print the message when the room actually changes.

## Australian Curriculum

The content of this website addresses the following Australian Curriculum v9 Digital Technologies content descriptions. Each stage starts with pseudocode and a UML class diagram, and students test their code as they build it.

| Level | Content description |
| --- | --- |
| Years 7 and 8 | [AC9TDI8P05](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY78&content-description-code=AC9TDI8P05&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
| | [AC9TDI8P06](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY78&content-description-code=AC9TDI8P06&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
| | [AC9TDI8P09](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY78&content-description-code=AC9TDI8P09&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
| Years 9 and 10 | [AC9TDI10P05](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY910&content-description-code=AC9TDI10P05&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
| | [AC9TDI10P06](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY910&content-description-code=AC9TDI10P06&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
| | [AC9TDI10P08](https://www.australiancurriculum.edu.au/f-10-curriculum/learning-areas/digital-technologies/year-7_year-8_year-9_year-10/content-description?subject-identifier=TECTDIY910&content-description-code=AC9TDI10P08&detailed-content-descriptions=0&hide-ccp=0&hide-gc=0&side-by-side=1&strands-start-index=0&subjects-start-index=0&view=quick) |
