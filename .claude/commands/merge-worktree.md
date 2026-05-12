# merge-worktree

Merge a `claude/*` worktree branch into `main`: selectively commit the worktree's local edits, merge into main, then remove the worktree and delete the branch.

## Instructions

When invoked with a worktree branch name (e.g. `/merge-worktree claude/crazy-einstein-d04c6b`), follow these steps in order. If no branch is named, list the existing worktrees with `git worktree list` and ask which one to merge.

1. **Survey state (parallel)** — in a single tool block, run:
   - `git worktree list` — locate the worktree's filesystem path.
   - `git -C <worktree-path> status` — see modified/untracked files inside the worktree.
   - `git log --oneline --graph --all -20` — confirm where the branch sits relative to `main`.
   - `git merge-base --is-ancestor <branch> main && echo MERGED || echo UNMERGED` — detect whether the branch tip is already in main's history.

2. **Inventory the worktree's local edits** — read `git -C <worktree-path> status` and classify every modified or untracked entry into two buckets:
   - **Keep**: source files, notebooks, project config the user authored (e.g. `*.py`, `*.ipynb`, `.claude/commands/*.md`, `requirements.txt`).
   - **Exclude**: ephemeral or machine-local state. Never commit any of these:
     - `.claude/.last-seen-files`
     - `.claude/settings.local.json`
     - `pre-log.json`, `post-log.json`, other `*-log.json`
     - `.env`, `.env.*` (excluded by `.gitignore`, but double-check)
     - `.idea/`, `.vscode/` machine-local files unless already tracked
   
   Present the keep/exclude split to the user and confirm before staging. If unsure about a file, ask rather than commit.

3. **Stage the keep list explicitly** — from inside the worktree, run `git add <file1> <file2> ...` with each path quoted. Never use `git add -A`, `git add .`, or `git add -u` here — accidental inclusion of secrets/logs is exactly what step 2 is designed to prevent. Then run `git status` and verify only the intended files are staged.

4. **Commit on the worktree branch** — write a concise message (under 72 chars) describing what was added. Use the HEREDOC form:
   ```
   git commit -m "$(cat <<'EOF'
   <message>

   Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
   EOF
   )"
   ```

5. **Merge into main with `--no-ff`** — from the main checkout (use `-C <main-path>` to avoid cd-ing):
   ```
   git -C <main-path> merge --no-ff <branch> -m "Merge branch '<branch>'"
   ```
   `--no-ff` is required so the branch history is preserved as a visible merge commit, even when fast-forward is possible. If the merge reports conflicts, stop and report the conflicting paths to the user — do not attempt resolution as part of this skill.

6. **Verify the merge landed** — run `git -C <main-path> log -1 --stat` and confirm the expected files appear in the merge. If a file the user wanted is missing, stop and report.

7. **Remove the worktree** — from outside the worktree directory (always use `-C <main-path>`, never `cd` into the worktree you are about to delete):
   ```
   git -C <main-path> worktree remove <worktree-path>
   ```
   If the worktree has unrelated untracked files that would be lost, `git worktree remove` refuses by default. Report the files and ask the user before adding `--force`.

8. **Delete the branch** — only after step 7 succeeds:
   ```
   git -C <main-path> branch -d <branch>
   ```
   Use `-d` (safe delete), not `-D`. If git refuses because the branch isn't merged, re-check step 5 — do not switch to `-D` without user confirmation.

9. **Report** — tell the user the merge commit hash, the files that landed, and confirm the worktree and branch are gone. Do NOT push to remote — pushing is the user's `/push-to-git` workflow, invoked separately.

## Scope

- Only merges worktree branches into `main`. Does not handle cross-branch merges or rebases.
- Stages files explicitly by path. Never uses `git add -A`, `git add .`, or `git add -u`.
- Never force-deletes a branch (`-D`) or force-removes a worktree (`--force`) without user confirmation.
- Never pushes to remote — that is `/push-to-git`'s job.
- Never amends an existing commit; only creates new commits.
- If pre-existing repository quirks come up (e.g. a worktree directory accidentally tracked as a gitlink in main), report them but do NOT fix as part of this skill — surface them as a follow-up.

## Example invocations

- `/merge-worktree claude/crazy-einstein-d04c6b` — inventory the worktree, commit the user-authored files on the branch, merge into main, then clean up the worktree and branch.
- `/merge-worktree` — list available worktrees and ask which to merge.
