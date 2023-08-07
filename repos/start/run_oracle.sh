#!/bin/bash

# Exist on error
set -e

# env name
conda_env_name=".venv_oracle_$1"

# Activate venv
source $conda_env_name/bin/activate

# Run
main

# TODO Support for arguments
# TODO Support for multiple commands
