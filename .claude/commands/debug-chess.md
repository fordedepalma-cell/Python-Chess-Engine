# debug-chess

Debug bugs in the chess engine project, applying fixes to both the combined script and the corresponding individual scripts.

## Instructions

When invoked, follow these steps:

1. **Read all four scripts** in parallel:
   - `chess_engine.py` (the combined script — source of truth for debugging)
   - `engine.py`
   - `main.py`
   - `piece.py`

2. **Identify the bug** described by the user (or infer it from context). If no specific bug is described, scan `chess_engine.py` for logic errors, incorrect conditions, off-by-one errors, missing guards, or broken control flow.

3. **Locate the exact lines** causing the bug in `chess_engine.py`. Note the function name, line numbers, and the section of code involved.

4. **Apply minimal fixes only** — do not refactor, rename, restructure, or add new functionality. Preserve the functional flow and variable names exactly as they are.

5. **Mirror the fix** in the corresponding individual script (`engine.py`, `main.py`, or `piece.py`) at the equivalent location. Both files must stay in sync.

6. **Formatting rules** (from CLAUDE.md):
   - 4-space indentation
   - Descriptive variable names (do not shorten or rename existing ones)
   - After making changes, add a `# Relevant Documentation` section near the fix if the logic is non-obvious. One short comment max — no multi-line blocks.

7. **Do not** add move generation, new game features, UI elements, or any code beyond what is needed to fix the identified bug.

## Scope

- Only fix bugs — logic errors, crashes, incorrect behavior, broken conditions.
- Do not add error handling for impossible cases.
- Do not clean up surrounding code unless it directly causes the bug.
- Trust internal chess logic unless a specific rule violation is the reported bug.

## Example invocations

- `/debug-chess` — scan for obvious bugs and report findings before fixing
- `/debug-chess castling rights are not cleared after the king moves`
- `/debug-chess en passant capture removes the wrong pawn`