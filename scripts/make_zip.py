"""Build the student download: the finished code for each stage.

Each page's programs live in docs/examples/<section>/<step>/<file>.py,
where a step folder only holds the files that changed in that step.
For every section, the zip gets the latest version of each file, carried
forward from earlier stages, so every folder is a complete, runnable
checkpoint:

    deepest_dungeon/stage_3/main.py, room.py, character.py

Stage checkpoints carry forward in order (stage_1 … stage_8, then
ext_player and ext_llm, which both start from the end of Stage 8).
Other sections (for example guides/buggy_code) are copied as they are.

Run from the repo root: python scripts/make_zip.py
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
ZIP_PATH = ROOT / "docs" / "downloads" / "deepest_dungeon.zip"
STAGES = [f"stage_{n}" for n in range(1, 9)]
EXTENSIONS = ["ext_player", "ext_llm"]


def latest_files(section, start):
    """Return {file name: path} after applying every step in a section."""
    files = dict(start)
    folder = EXAMPLES / section
    if folder.exists():
        for step in sorted(p for p in folder.iterdir() if p.is_dir()):
            for source in sorted(step.glob("*.py")):
                files[source.name] = source
    return files


def main():
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        files = {}
        for stage in STAGES:
            files = latest_files(stage, files)
            for name, source in sorted(files.items()):
                archive.write(source, f"deepest_dungeon/{stage}/{name}")
                count += 1
        for extension in EXTENSIONS:
            for name, source in sorted(latest_files(extension, files).items()):
                archive.write(source, f"deepest_dungeon/{extension}/{name}")
                count += 1
        guides = EXAMPLES / "guides"
        for source in sorted(guides.rglob("*.py")) if guides.exists() else []:
            archive.write(source, f"deepest_dungeon/guides/{source.parent.name}.py")
            count += 1
    print(f"Wrote {count} file(s) to {ZIP_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
