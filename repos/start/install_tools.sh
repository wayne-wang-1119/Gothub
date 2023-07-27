#!/bin/bash

# Exist on error
set -e

# Get the current directory
current_dir=$(pwd)

# Loop through each child directory
for dir in "$current_dir"/*/; do
    # Check if the child directory has a pyproject.toml file
    if [ -f "$dir/pyproject.toml" ]; then
        # Change into the child directory
        cd "$dir"

        # # Conda
        # conda_env_name=$(pwd | tr '/' '_')
        # conda create -n $conda_env_name python=3.11 -y
        # conda activate $conda_env_name

        # Run 'install' command
        python -m pip install -e "."

        # Change back to the original directory
        cd "$current_dir"
    fi
done
