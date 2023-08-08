#!/bin/bash

# Exist on error
set -e

# env name
conda_env_name=".venv_ability_$1"

# Activate venv
source $conda_env_name/bin/activate

# Run main with arguments except the first one
main "${@:2}"

# TODO Support for arguments
# TODO Support for multiple commands
