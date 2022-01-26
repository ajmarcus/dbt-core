#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o xtrace

python -m cProfile -s 'cumulative' core/scripts/dbt > scripts/profile_cli.txt
sudo py-spy record -o scripts/profile_cli.svg -- python core/scripts/dbt
sudo chown $USER scripts/profile_cli.svg
# time python core/scripts/dbt >/dev/null 2>/dev/null