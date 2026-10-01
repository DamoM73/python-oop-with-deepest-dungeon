# Python OOP with Deepest Dungeon

*Deepest Dungeon* is a tutorial site that teaches Year 9/10 students object-oriented programming in Python by building a text adventure game in Thonny, one stage at a time. It's also a resource for the teachers running the course.

Live site: [Deepest Dungeon - Python OOP](https://damom73.github.io/python-oop-with-deepest-dungeon/)

## Previewing the site

The site is built with [Zensical](https://zensical.org/).

```bash
pip install -r requirements.txt
zensical serve
```

To produce the static build (used by the deploy workflow):

```bash
zensical build --clean
```

## Rebuilding the student zip

Each stage's checkpoint files are bundled into a downloadable zip for students:

```bash
python scripts/make_zip.py
```

## Checking code explanations

Every "Code explanation" callout references line numbers in a snippet. This script confirms they still match:

```bash
python scripts/check_explanations.py
```

## Folder layout

- `docs/index.md` - home page
- `docs/start/` - teacher and student introductions, and an OOP primer
- `docs/stages/stage_1.md` to `stage_8.md` - the eight tutorial stages
- `docs/extensions/` - the Player class, Character LLM and extension ideas
- `docs/guides/` - developing a new program, debugging with Thonny, and licencing
- `docs/examples/<section>/stepNN/<file>.py` - snippet files for each step. A step folder holds only the files that changed in that step. Pages include snippets with `--8<-- "examples/..."` (pymdownx.snippets), with `hl_lines` marking new or changed lines
- `docs/downloads/` - the student zip, built by `scripts/make_zip.py`
- `docs/stylesheets/extra.css` - the site's colour scheme
- `scripts/` - `make_zip.py` and `check_explanations.py`
- `zensical.toml` - site configuration

## Licence

Code is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html). Content (the tutorial text and images) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
