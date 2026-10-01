# Todo

Remaining tasks now that the Zensical rework is live on `main`.

## Clean-up

- [ ] Delete the old `gh-pages` branch: `git push origin --delete gh-pages` (or delete it from the GitHub branches page). Claude's permission system wouldn't allow this one even after confirming — needs doing manually.

## From Damien's list in VSCODE_CLAUDE_TASKS.md

- [ ] Fix `lesson_1_class_diagram.png` in drawio: it labels the method `link_room(room, direction)`, but the code uses `link_rooms(room_to_link, direction)`. Once fixed, remove the Stage 1 tip that explains the difference.
- [ ] Play through each stage's checkpoint from the zip in Thonny to confirm it runs as the page describes.

## Optional follow-up

- [ ] Run the `ext_llm` checkpoint from the zip with a real `nigel` model to confirm talking to Nigel and Ugine both work end-to-end. Skipped during the review since it needs a ~3GB `gemma3:4b` download.
