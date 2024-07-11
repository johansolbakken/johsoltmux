#!/bin/bash

# Get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

# Check if the directory is a git repository
if [ -n "$branch" ]; then
    # Count the number of added (staged) files and trim whitespace
    added_files=$(git diff --cached --name-only | wc -l | xargs)
    
    # Count the number of not staged files and trim whitespace
    not_staged_files=$(git diff --name-only | wc -l | xargs)
    
    # Get the number of untracked files and trim whitespace
    untracked_files=$(git ls-files --others --exclude-standard | wc -l | xargs)    # Determine the output based on the file counts

    if [ "$added_files" -eq 0 ] && [ "$not_staged_files" -eq 0 ] && [ "$untracked_files" -eq 0 ]; then
        echo "#[fg=green]✔ #[default]nothing to do"
    else
        echo "#[fg=yellow]✗ #[default][#[fg=green]$added_files staged#[default], #[fg=red]$not_staged_files unstaged#[default], #[fg=gray]$untracked_files untracked#[default]]"
    fi
else
    echo "#[fg=gray]not git repo#[default]"
fi

