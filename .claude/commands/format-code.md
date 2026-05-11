# format-code

Format all chess engine code using Black for consistent, readable style.

## Instructions

When invoked, follow these steps in order:

1. **Check Black installation** — run `pip list | findstr black` (or `pip list | grep black` on Linux/Mac). If Black is not installed, run `pip install black`.

2. **Format the four scripts** — run Black on each file in the project root:
   ```
   black chess_engine.py engine.py main.py piece.py
   ```
   This reformats all four files in-place to follow Black's style conventions.

3. **Verify formatting** — run `git diff` to show what changed. Confirm that only whitespace/formatting has changed — no logic alterations.

4. **Report** — summarize the formatting changes applied (e.g., "Formatted 4 files: adjusted indentation, line length, and spacing").

## Scope

- Format only the four chess engine scripts: `chess_engine.py`, `engine.py`, `main.py`, `piece.py`.
- Use Black with default settings — do not pass custom configuration flags.
- Do not modify any logic, variable names, or comments.
- This is purely a formatting/style step; no bug fixes or new code.

## Example invocations

- `/format-code` — format all four scripts using Black
