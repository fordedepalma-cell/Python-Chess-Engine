# debug-push

Run the full debug-then-publish workflow: debug the chess engine, then commit and push the fix to git.

## Instructions

When invoked, execute these three skills in order. Do not skip any step.

1. **Run `/debug-chess`** — follow every instruction in `.claude/commands/debug-chess.md` exactly. This includes:
   - Reading all four scripts (`chess_engine.py`, `engine.py`, `main.py`, `piece.py`)
   - Identifying and locating the bug
   - Applying minimal fixes to `chess_engine.py`
   - Mirroring the fix in the corresponding individual script
   - Adding a `# Relevant Documentation` comment if the logic is non-obvious

   If `/debug-chess` was invoked without a specific bug description, scan for one, **report findings to the user, and stop here** — do not proceed speculative changes. The user must confirm before proceeding to step 2.

2. **Run `/format-code`** — only after step 1 has produced concrete code changes. Follow every instruction in `.claude/commands/format-code.md` exactly. This includes:
   - Checking Black installation (install if needed via `pip install black`)
   - Running Black on all four scripts to format them consistently
   - Verifying that only whitespace/style has changed
   - Reporting the formatting summary

3. **Run `/push-to-git`** — only after step 2 has completed. Follow every instruction in `.claude/commands/push-to-git.md` exactly. This includes:
   - Staging only tracked files (`git add -u`)
   - Writing a descriptive commit message that mentions both the bug fix and formatting
   - Committing with the Co-Authored-By tag
   - Pushing to `origin main`

4. **Confirm** — report the bug fix summary, formatting results, and the resulting commit hash to the user.

## Scope

- Pass any user-supplied bug description from the `/debug-push` invocation through to step 1 (`/debug-chess`).
- If step 1 makes no changes (no bug found, or user has not confirmed a speculative finding), stop without running steps 2 and 3 — there is nothing to format or push.
- If step 2 or 3 fails, report the error verbatim and stop. Do not retry or force-push.

## Example invocations

- `/debug-push castling rights are not cleared after the king moves` — fix the bug, format the code, then commit and push
- `/debug-push en passant capture removes the wrong pawn` — fix the bug, format the code, then commit and push
- `/debug-push` — scan for bugs, report findings, and wait for user confirmation before formatting and pushing
