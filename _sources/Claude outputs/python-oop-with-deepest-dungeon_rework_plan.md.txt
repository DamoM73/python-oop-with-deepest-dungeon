# Deepest Dungeon (Python OOP): audit and rework plan

- Live site: https://damom73.github.io/python-oop-with-deepest-dungeon/
- Repo: `D:\GIT\python-oop-with-deepest-dungeon` (GitHub: DamoM73/python-oop-with-deepest-dungeon)
- Current build: Sphinx + MyST + Furo, two custom directives (`pseudocode`, `question`) in `conf.py`, orange theme in `_static/custom.css`, deployed to `gh-pages` by an old Actions workflow (`actions/checkout@v2.3.4`, Python 3.9)
- Target: Zensical on a `zensical` branch; `main` stays live until go-live

## Decisions

| Area | Decision |
| --- | --- |
| Audience | Year 9/10 students, plus the teacher page |
| Editor | Thonny |
| Site type | Mixed: sequential project stages (template B) + extensions + guides (template D) |
| Nav | Tabs: Start, Stages, Extensions, Guides |
| Videos | Keep all eight stage videos (already `youtube-nocookie.com`) |
| Pseudocode | Keep, as a titled plain-text code block (the five-callout standard has no pseudocode type) |
| Class diagrams | Keep all PNGs |
| Debugging with Thonny | Keep as a guide page with all 33 screenshots |
| Extensions | Keep Player Class and Character LLM |
| Code | Every program shown on a page becomes a snippet file under `docs/examples/`, included with `hl_lines` for new/changed lines. The code itself is kept as is (no restructuring into minimal examples) |
| Make tasks | Keep each stage's open Make task, rephrased as a question under `## Exercises`; no starter files or solutions |
| Licences | Content CC BY-NC-SA 4.0, code GPLv3 (unchanged) |

## Page inventory

| New page | Source | Video | Change |
| --- | --- | --- | --- |
| Home (`index.md`) | `index.md` | – | Rewrite: purpose, how to use the site, callouts, code blocks, error messages, tutorial files |
| Start / Teachers (`start/teachers.md`) | `introduction.md` | – | Remove `_build/html` portable note; keep AC v9 table (link-check in VS Code) |
| Start / Students (`start/students.md`) | `student_intro.md` | – | Keep Thonny + project folder setup; move "coloured boxes" explanation to Home |
| Start / OOP Primer (`start/oop_primer.md`) | `oop_introduction.md` | – | Guide template |
| Stage 1: Create Rooms | `stage_1.md` | GeSTPYPPEfU | Move "How we plan" pseudocode explanation here as a tip; PRIMM intro as page text |
| Stage 2: Movement | `stage_2.md` | hZd1FcDApCI | |
| Stage 3: Character Creation | `stage_3.md` | ufsmJYdUg1Y | |
| Stage 4: Character Types | `stage_4.md` | J8U97_SRx7s | Contains the site's only error block |
| Stage 5: Item Creation | `stage_5.md` | jYSs_-wY8ys | |
| Stage 6: Use Items | `stage_6.md` | JsUGdNxLlLM | |
| Stage 7: Victory Conditions | `stage_7.md` | hTGv542obJo | |
| Stage 8: Usability | `stage_8.md` | lHSCfn0U45k | Keep "Final code" section as four snippets; keep the deliberate logic mistakes |
| Extensions / Player Class | `ext_player.md` | – | Add learn callout |
| Extensions / Character LLM | `ext_llm.md` | – | Unfinished (see open questions) |
| Extensions / Extension Ideas | `extention.md` | – | Rename file `extension_ideas.md` |
| Guides / Debugging with Thonny | `debugging.md` | – | Guide template; `buggy_code.py` as snippet + zip |
| Guides / Licencing | `licencing.md` | – | Unchanged content |

## Proposed nav

```
Home
Start
  Introduction for Teachers
  Introduction for Students
  OOP Primer
Stages
  Stage 1: Create Rooms … Stage 8: Usability
Extensions
  Player Class
  Character LLM
  Extension Ideas
Guides
  Debugging with Thonny
  Licencing
```

## Repo layout

```
zensical.toml
requirements.txt                         # zensical==<pinned>
docs/
  index.md
  start/teachers.md, students.md, oop_primer.md
  stages/stage_1.md … stage_8.md
  extensions/player.md, llm.md, extension_ideas.md
  guides/debugging.md, licencing.md
  examples/stage_N/stepK/{main,room,character,item}.py   # each program version shown
  examples/ext_player/stepK/…, examples/ext_llm/…
  examples/guides/buggy_code/main.py
  assets/                                # existing PNGs, logo, favicon
  stylesheets/extra.css
  downloads/deepest_dungeon_tutorials.zip   # stage checkpoints + buggy_code
scripts/make_zip.py, check_explanations.py
```

## Syntax conversion specific to this site

| Sphinx | Zensical |
| --- | --- |
| `{topic} Learning Intentions` | `!!! learn "In this lesson we will learn"` under the title, above the video |
| `{pseudocode}` | `### Pseudocode` + ```` ```text title="Stage N pseudocode" ```` |
| `{admonition}` `:class: note` Code Explanation | `??? note "Code explanation"` after a `!!! primm` callout, rewritten to `**line N** →` format |
| `{admonition}` `:class: hint` and `{hint}` | `!!! tip "Title"` |
| `{question} Make` | `## Exercises` → `### Exercise 1`, "Can you …?" |
| `{code-block} python` + `:emphasize-lines:` | `--8<--` snippet with `hl_lines` |
| `:lineno-start:` fragments (Stage 4, Player Class) | full-file snippet with `hl_lines`, or `linenums="81"` for fragments |
| `{code-block} error` | ```` ``` { .text .error linenums="1" } ```` |
| `{literalinclude}` / `{download}` | snippet + link to the zip |

## Bugs and outdated facts found

Code (python_files)
- `python_files/stage_N/` is stale: it uses `room.inhabitant`, while every page uses `room.character`. The pages are treated as the source of truth; the new snippet files are built from the pages.
- `print("Thank you for playing Darkest Dungeon")` in Stage 8 and Player Class; should be Deepest Dungeon.
- `Enemy.get_num_of_enemy()` has no `self` and no decorator, so it fails if called on an object (`ugine.get_num_of_enemy()`). It is also never used; the main loop reads `Enemy.num_of_enemy` directly, which contradicts the encapsulation message.

Stage 1
- Class diagram and text say `link_room(room, direction)`; the code uses `link_rooms(room_to_link, direction)`.
- "intialise" in code comments; "The case diagram"; "Calling your room.py save it"; "type to following code".
- Says "Class names must use CamelCase"; it's a convention (PEP 8), which the next sentence says.

Stage 3
- Four Code Explanation boxes use the `hint` class, so they display as hints.

Stage 7
- Class diagram adds `get_num_of_enemy`, see above.

Stage 8
- Title "Useability" → "Usability".
- Code comment "converstation".
- Final Make says "There are a few logic mistakes in the code" — these are deliberate and will be kept.

Character LLM
- "downoad", "chartacters", stray `:` option line in a code block, "we will add always call".
- Page ends at "Up to you" without wiring `chat()` into the main loop.

Flavour text to confirm (possibly deliberate): "unknownable contraptions", "Well youngan", "golden bead in woven through his beard".

Teacher page and repo
- Portable `_build/html` note is out of date after Zensical.
- "The intention is to add both flowchart and pseudocode" — pseudocode is now added.
- Leftovers to remove later (Confirm first): `%GIT%python-oop-with-deepest-dungeon/`, `_build/`, `_static/`, `_templates/`, `conf.py`, `Makefile`, `make.bat`, `admonitions.md`, `notes.md`, `todo.md`, root `.md` pages, `python_files/`, `.claude/`, `cover.psd` (3.3 MB), `logo.psd` (6.1 MB), `youtube_cover.png`, `oop_logo.png`/`_static/opp_logo.png` duplicates. Keep `working_files/*.drawio`.

## Pedagogical observations

- Each stage repeats the whole of `main.py` at every step (up to six times per page). Snippet files with `hl_lines` keep this but remove the copy-paste drift risk.
- Current Code Explanation boxes quote the code instead of line numbers. The house style needs `**line N** →`, explaining only the new/changed (highlighted) lines, since earlier lines were explained on earlier steps.
- PRIMM is introduced inside a hint in Stage 1; it moves to page text, then the standard `primm` callout after every example.
- Stage Make tasks are open design tasks, which suit Year 9/10.

## Colour theme

Banner candidates (current theme is orange `#FF9100`, which only gives 2.3:1 with white text): A burnt orange `#A84300` (6.06), B torch rust `#8A3B12` (7.73), C dungeon stone brown `#5D4037` (9.32), D blood red `#9B1C1C` (8.15). Final mapping to be confirmed before building.

## Open questions

- Fix `get_num_of_enemy` (as `@staticmethod` and use it in the main loop) or leave it?
- Finish the Character LLM page (wire `chat()` into the talk command) or leave "Up to you" as the open task?
- Fix the flavour-text spellings?

## Build order

1. Branch `zensical` in GitHub Desktop (step by step).
2. Scaffold: `zensical.toml`, `requirements.txt`, `extra.css`, assets, scripts, Home, Start pages.
3. Stages 1–4, preview.
4. Stages 5–8, preview.
5. Extensions, Guides, zip; run checks.
6. `VSCODE_CLAUDE_TASKS.md`: link check, spell-check, cleanup, workflow, README, go-live.
