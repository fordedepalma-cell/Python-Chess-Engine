# push-to-git

Commit all current changes and push them to the remote git repository.

## Instructions

When invoked, follow these steps in order:

1. **Check status (parallel)** — in a single tool block, run `git status` and `git log -3 --oneline` together. The status shows what's changed; the log gives recent commit-message style for reference. If there is nothing to commit (no modified tracked files), report that and stop.

2. **Stage tracked changes only** — run `git add -u` to stage all modified and deleted tracked files. Do NOT stage untracked files (e.g. `.idea/vcs.xml` or other IDE/OS-generated files).

3. **Review the staged diff** — run `git diff --cached` to read exactly what is staged. Use this to write the commit message. This is the only diff call needed — the pre-stage `git diff` is redundant because `git add -u` stages exactly what would appear there.

4. **Write a descriptive commit message** — one concise sentence summarising *what changed and why*, based on the actual diff. Keep it under 72 characters. Do not use generic messages like "update files".

5. **Commit** using this exact format (HEREDOC to preserve formatting):
   ```
   git commit -m "$(cat <<'EOF'
   <your message here>

   Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
   EOF
   )"
   ```

6. **Push** — run `git push origin main`. The repo is already authenticated via Windows Credential Manager, so no token prompt is needed.

7. **Confirm via gh** — run `gh run list --branch main --limit 1 --json status,conclusion,workflowName,headSha`. This confirms the push landed on GitHub and reports whether CI kicked off. Report the commit hash and the CI status (e.g. `queued`, `in_progress`, `completed/success`) to the user. If no workflow exists for the repo, just report the commit hash and that the push succeeded.

## Scope

- Stage only tracked files (`git add -u`). Never use `git add .` or `git add -A`.
- Never force-push (`--force`).
- Never amend a previous commit — always create a new one.
- If the push fails, report the error message verbatim and stop.

## Example invocations

- `/push-to-git` — stage, commit, and push all current changes
- `/push-to-git` after editing `chess_engine.py` — commit with a message describing the specific fix applied
