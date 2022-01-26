#!/usr/bin/env bash

# Example run:
# git clone 'git@github.com:ajmarcus/dbt-core.git''
# cd into dbt-core, set up virtualenv
# git checkout 'faster-cli-via-lazy-import'
# pip install dev-requirements.txt and editable-requirements.txt
# cd ..
# dbt init
# cd into your project
# ../dbt-core/scripts/profile_cli.sh "dbt" > profile_cli_1.0.1.log
# ../dbt-core/scripts/profile_cli.sh "$HOME/.pyenv/versions/dbt-core/bin/dbt" > profile_cli_lazy.log

set -o xtrace

# Allow user to set custom dbt path for running with virtualenv
if [ -z $1 ]; then
    DBT="python core/scripts/dbt"
else
    DBT=$1
fi

time $DBT
time $DBT docs
time $DBT source
time $DBT clean
time $DBT debug
time $DBT deps
time $DBT list
time $DBT build
time $DBT snapshot
time $DBT run
time $DBT compile
time $DBT parse
time $DBT test
time $DBT seed
time $DBT run-operation macro
sudo time py-spy record -o profile_cli_empty.svg -- $DBT
sudo chown $USER profile_cli_*.svg
