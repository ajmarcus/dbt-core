import micropip
import sqlite3
from typing import List
import os

deps = [
    "https://storage.googleapis.com/db-owser/parsedatetime-2.7-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/minimal-snowplow-tracker-0.0.2-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_core-1.0.1.2-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_sqlite-1.0.0-py3-none-any.whl",
]
for d in deps:
    await micropip.install(d, True)

import dbt.main

def run(cmd: str = None):
    if cmd is None:
        return dbt.main.main([])
    else:
        return dbt.main.main([cmd])

def cat(filename: str) -> List[str]:
    lines = []
    f = open(filename)
    for line in f:
        lines.append(line)
    return lines
    
def ls(root_dir: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            result.append(f"{root}/{filename}")
    return result

def p(i: List) -> None:
    for l in i:
        print(l)

class DB(object):
    def __init__(self, filename: str) -> None:
        self._con = sqlite3.connect(filename)
    
def select(db: DB, query: str) -> List[sqlite3.Row]:
    result = []
    cur = db._con.cursor()
    for row in cur.execute(query):
        result.append(row)
    return result

def tables(db: DB) -> List[sqlite3.Row]:
    return select(db, "select * from sqlite_master")
        
run()
run("--version")
run("init")

os.chdir("../db/")
run("compile")
run("run")

p(cat("../.dbt/profiles.yml"))
p(cat("./dbt_project.yml"))
p(cat("./models/example/my_second_dbt_model.sql"))
p(cat("./target/compiled/db/models/example/my_second_dbt_model.sql"))

db = DB("./dev.db")
p(tables(db))
p(select(db, "select * from my_first_dbt_model"))
p(select(db, "select * from my_second_dbt_model"))
