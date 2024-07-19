#!/usr/bin/env python3

import subprocess
from typing import Optional

def run_command(command: str) -> str:
    """Runs a shell command and returns the output as a stripped string."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def count_files(command: str) -> int:
    """Runs a shell command that lists files and returns the count of lines in the output."""
    output = run_command(command)
    return int(output) if output else 0

def get_branch_name() -> Optional[str]:
    """Returns the current git branch name, or None if not in a git repository."""
    branch = run_command("git rev-parse --abbrev-ref HEAD 2>/dev/null")
    return branch if branch else None

def get_git_status() -> Tuple[int, int, int]:
    """Returns the count of staged, unstaged, and untracked files in the git repository."""
    added_files = count_files("git diff --cached --name-only | wc -l | xargs")
    not_staged_files = count_files("git diff --name-only | wc -l | xargs")
    untracked_files = count_files("git ls-files --others --exclude-standard | wc -l | xargs")
    return added_files, not_staged_files, untracked_files

def main() -> None:
    branch = get_branch_name()
    if branch:
        added_files, not_staged_files, untracked_files = get_git_status()
        if added_files == 0 and not_staged_files == 0 and untracked_files == 0:
            print(f"#[fg=cyan]({branch}) #[fg=green]✔ #[default]nothing to do")
        else:
            print(f"#[fg=yellow]✗ #[fg=cyan]({branch}) #[default][#[fg=green]{added_files} staged#[default], "
                  f"#[fg=red]{not_staged_files} unstaged#[default], #[fg=gray]{untracked_files} untracked#[default]]")
    else:
        print("#[fg=gray]not git repo#[default]")

if __name__ == "__main__":
    main()

