# Tasks for Claude in VS Code

These tasks finish the Zensical rework of *Deepest Dungeon - Python OOP*. They couldn't be done from Cowork, which could only create and overwrite files in this folder. It couldn't delete files, run git, access GitHub or write inside `.github/`.

The Zensical rework has gone live. From now on, all work happens on `main`. Do the tasks in order and check with Damien before each one marked **Confirm first**. Report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.66 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Audience:** Year 9/10 students (and their teachers), using Thonny.
- **Structure:** Home (`docs/index.md`); Start (`docs/start/teachers.md`, `students.md`, `oop_primer.md`); eight stages (`docs/stages/stage_1.md` to `stage_8.md`); Extensions (`docs/extensions/player.md`, `llm.md`, `extension_ideas.md`); Guides (`docs/guides/developing.md`, `debugging.md`, `licencing.md`). The Developing a New Program guide has its own stepped pet shelter example in `docs/examples/guides/pet_shelter/`.
- **Examples:** each stage builds one program across several files. Every version of a file shown on a page is a snippet file at `docs/examples/<section>/stepNN/<file>.py`, where a step folder holds only the files that changed in that step. Pages include them with `--8<-- "examples/..."` (pymdownx.snippets, base path `docs`), with `hl_lines` marking new or changed lines. A few fragments use a line range, for example `--8<-- "examples/stage_4/step06/main.py:65:73"` with `linenums="65"`; `hl_lines` still counts from 1 in those blocks.
- **Student zip:** `python scripts/make_zip.py` builds `docs/downloads/deepest_dungeon.zip`. Each `deepest_dungeon/stage_N/` folder is a complete, runnable checkpoint (the latest version of every file, carried forward from earlier stages). `ext_player/` and `ext_llm/` both start from the end of Stage 8, and `guides/` holds the finished `pet_shelter/` program plus `buggy_code.py` and `debug_names.py` (40 files).
- **Checks:** `python scripts/check_explanations.py` confirms every Code explanation line number matches its snippet. When a code block has `hl_lines`, only the highlighted code lines need explaining; comment lines are never referenced. Expect `0 issue(s) found`.
- **Colour scheme:** burnt orange `#A84300` (header, tabs, links and headings in light mode; 6.06:1 with white text), torch orange `#E07B2E` (primary light, decorative only), peach `#FFDFB4` (active and hovered tab, dark-mode headings and accent), light blue `#8AB4F8` (dark-mode links). Set in `docs/stylesheets/extra.css`. Burnt orange keeps the old site's orange identity and is clearly different from the micro:bit (navy), Lego Spike (magenta) and Turtle (teal) banners.
- **Callouts:** five types, the same on all of Damien's tutorial sites:
    - `!!! learn "In this lesson we will learn"` (stages) or `"On this page we will learn"` (other pages): amber, target icon, directly under the title and above the video
    - `!!! primm "PRIMM"`: green, flask icon, after examples students run
    - `??? note "Code explanation"`: purple, `</>` icon, collapsed, after each snippet or PRIMM callout
    - `!!! tip "Title"`: light blue, light bulb icon, every other aside
    - `!!! warning "Title"`: hot pink, triangle alert icon
- **Code blocks:** grey border on every code block; error messages use ```` ``` { .text .error linenums="1" } ```` (red border and text). Pseudocode uses ```` ```text title="Stage N pseudocode" ````.
- **Writing style:** Australian English, written for Year 9/10, in Damien's inclusive "we" voice. Code explanations are `- **line n** → full sentence ending in a full stop.` Exercises are phrased as questions ("Can you …?"). There are no starter files or solutions: each stage's exercise is an open **make** task on the student's own dungeon.
- **Deliberate bug:** the Stage 8 final ***main.py*** prints `You travel <direction>` even when the move fails. This is the hidden logic mistake the Final make section refers to, and it's explained on the teachers page. Don't fix it.
- **Rework plan:** the full audit and plan are in Damien's Claude project as `python-oop-with-deepest-dungeon_rework_plan.md`.

## 1. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 5), so nothing is lost. Show Damien this list before deleting anything:

- root pages: `index.md`, `introduction.md`, `student_intro.md`, `oop_introduction.md`, `stage_1.md` to `stage_8.md`, `ext_player.md`, `ext_llm.md`, `extention.md`, `debugging.md`, `licencing.md`
- Sphinx files: `conf.py`, `Makefile`, `make.bat`, `_build/`, `_static/`, `_templates/`
- old content folders: `assets/` (copied to `docs/assets/`), `python_files/` (out of date: it uses `room.inhabitant`, while every page uses `room.character`)
- stray notes: `notes.md`, `todo.md`, `admonitions.md`
- root image copies: `logo.ico`, `logo_square.png`, `oop_logo.png`, `cover.jpg`, `youtube_cover.png` (the site uses `docs/assets/logo.png`, `logo_header.png` and `favicon.ico`)
- `%GIT%python-oop-with-deepest-dungeon/` (a stray chat history folder)
- `working_files/.$deepest_dungeon_diagrams.drawio.bkp` (a drawio backup file)

Ask Damien about these before touching them:

- `cover.psd` (3.3 MB) and `logo.psd` (6.1 MB): move out of the repo or keep?
- `.claude/`: local Claude Code settings; keep or add to `.gitignore`?
- `Claude outputs/`: check what it holds.
- `working_files/deepest_dungeon_diagrams.drawio`: keep.

Keep `LICENSE` (if present), `README.md`, `.gitignore`, `.gitattributes`, `requirements.txt`, `zensical.toml`, `VSCODE_CLAUDE_TASKS.md`, `docs/`, `scripts/`, `working_files/` (drawio file only) and `.github/`.

Before deleting, search the repo to confirm nothing in `docs/`, `scripts/` or `zensical.toml` references these files. Then add `.cache/` and `site/` to `.gitignore` (the current `.gitignore` only has `.venv`) and run `zensical build --clean`.

## 2. Replace the deploy workflow

Delete `.github/workflows/write_to_gh_pages.yml` and create `.github/workflows/deploy.yml` with the workflow below. It builds with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 3. Update `README.md`

Replace the Sphinx-era README with:

- what the site is and who it is for (Year 9/10 students learning object-oriented Python by building a text adventure in Thonny, and their teachers)
- how to preview it (`pip install -r requirements.txt`, then `zensical serve`)
- how to rebuild the student zip (`python scripts/make_zip.py`)
- how to check explanations (`python scripts/check_explanations.py`)
- the folder layout from the Context section above, including the `stepNN` snippet convention
- the licences: GPLv3 for code, CC BY-NC-SA 4.0 for content

## 4. Verify the Character LLM page

`docs/extensions/llm.md` was finished in Cowork without a running Ollama. Check these assumptions against the current Ollama app and `ollama` Python library, and report any that are wrong:

1. The Ollama desktop app lets us choose `gemma3:4b` from a model list in its chat box, and sending a message downloads the model.
2. Thonny's **Tools** → **Open system shell…** opens a terminal in the current file's folder.
3. `ollama create nigel -f nigel.txt` builds a model from a Modelfile, and the new model appears in the app's model list.
4. The Modelfile link `https://docs.ollama.com/modelfile` works.
5. `ollama.generate(model=..., prompt=...)` returns a response that supports `response['response']` (checked against `ollama` 0.6.3).
6. Calling `ollama.generate` with a model that doesn't exist raises `ollama.ResponseError`, and with the server stopped raises `ConnectionError` (checked against the 0.6.3 source).

If Ollama is installed, run `docs/examples/` checkpoint `ext_llm` from the zip with a `nigel` model and confirm talking to Nigel and Ugine both work.

## 5. Final checks

1. Run `python scripts/make_zip.py`. Expected: `Wrote 40 file(s)`.
2. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
3. Run `zensical build --clean`. Expected: `No issues found`.
4. Check every external link in `docs/` returns a working page (YouTube embeds, the Australian Curriculum links on the teachers page, Thonny, Ollama, Rich and Textual). Report broken ones to Damien rather than guessing replacements.
5. Spell-check the pages for Australian English. American spellings inside code (for example `capitalize()`, `color`) and in library names are correct and should stay.
6. Commit to `zensical` and push.

## 6. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: in the repo settings go to **Settings** → **Pages** → **Source**, or run `gh api -X PUT repos/DamoM73/python-oop-with-deepest-dungeon/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that <https://damom73.github.io/python-oop-with-deepest-dungeon/> shows the new site.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**
6. From now on, all work happens on `main`. Update the intro of this file to say so.

## Tasks for Damien (not for Claude)

- Fix `lesson_1_class_diagram.png` in drawio: it labels the method `link_room(room, direction)`, but the code uses `link_rooms(room_to_link, direction)`. Stage 1 currently has a tip explaining the difference; remove it once the image is fixed.
- Play through each stage's checkpoint from the zip in Thonny to confirm it runs as the page describes.
- Decide whether to move `cover.psd` and `logo.psd` out of the repo.
