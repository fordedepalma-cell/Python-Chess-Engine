# generate-requirements

Scan the four chess engine Python scripts for imported packages and write a `requirements.txt` listing the third-party dependencies.

## Instructions

When invoked, follow these steps:

1. **Read all four scripts** in parallel:
   - `chess_engine.py`
   - `engine.py`
   - `main.py`
   - `piece.py`

2. **Extract every import statement** from each script — both `import X` and `from X import Y` forms. For dotted imports (e.g. `import a.b.c`), keep only the top-level package (`a`).

3. **Filter the import list** down to third-party packages by removing:
   - Local modules of this project: `chess_engine`, `engine`, `main`, `piece`
   - Python standard library modules (e.g. `os`, `sys`, `math`, `random`, `re`, `json`, `time`, `collections`, `itertools`, `functools`, `typing`, `pathlib`, `dataclasses`, `enum`, `copy`, `abc`, `argparse`, `logging`, `unittest`, `__future__`, etc.). When unsure whether a name is stdlib, check it against `sys.stdlib_module_names` by running a short `python -c` snippet.
   - Duplicates across scripts.

4. **Map import names to PyPI package names** when they differ (e.g. `cv2` → `opencv-python`, `PIL` → `Pillow`, `yaml` → `PyYAML`). For names that match their PyPI package, use the import name as-is.

5. **Write `requirements.txt`** at the project root:
   - One package per line, sorted alphabetically (case-insensitive).
   - No version pins unless a script enforces a specific version via comment or check — leave versions unpinned by default.
   - If `requirements.txt` already exists, preserve any existing version pins for packages that are still used; drop entries for packages no longer imported; add new ones.
   - If no third-party packages are found, write an empty `requirements.txt` (a single trailing newline) and tell the user the scripts only use the standard library and local modules.

6. **Report** the final package list to the user, noting any import-name → PyPI-name mappings applied and any entries removed from a pre-existing `requirements.txt`.

## Scope

- Only generate or update `requirements.txt`. Do not modify the four Python scripts.
- Do not install packages, do not run `pip freeze`, and do not pin to whatever happens to be installed locally — the file should reflect what the source code actually imports.
- Do not add development-only tools (e.g. `black`, `pytest`) unless they are imported by one of the four scripts.

## Example invocations

- `/generate-requirements` — scan the four scripts and write `requirements.txt`
