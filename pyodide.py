# pip install build
# python -m build core && mv core/dist/dbt_core-1.0.1-py3-none-any.whl core/dist/dbt_core-1.0.1.4-py3-none-any.whl
# https://pyodide.org/en/stable/console.html
import micropip

deps = [
    "https://storage.googleapis.com/db-owser/parsedatetime-2.7-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/minimal-snowplow-tracker-0.0.2-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_core-1.0.1.9-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_postgres-1.0.1-py3-none-any.whl",
]
for d in deps:
    await micropip.install(d, True)


import dbt.main

dbt.main.main([])
dbt.main.main(["--version"])
dbt.main.main(["init"])

import os

for root, dirs, files in os.walk(".."):
    for filename in files:
        print(f"{root}/{filename}")


def print_file(filename):
    f = open(filename)
    for line in f:
        print(line)


print_file("../logs/dbt.log")

print_file("../.dbt/profiles.yml")
print_file("./dbt_project.yml")
print_file("./models/example/my_second_dbt_model.sql")


dbt.main.main(["parse"])
