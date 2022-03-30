import micropip
import sqlite3
from typing import List
import os

deps = [
    "https://storage.googleapis.com/db-owser/parsedatetime-2.7-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/minimal-snowplow-tracker-0.0.2-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_core-1.0.1.4-py3-none-any.whl",
    "https://storage.googleapis.com/db-owser/dbt_sqlite-1.0.0-py3-none-any.whl",
]
for d in deps:
    await micropip.install(d, True)

import dbt.main

def tdb(cmd: str = None):
    if cmd is None:
        return dbt.main.main([])
    else:
        return dbt.main.main(cmd.split(" "))

def cat(filename: str) -> None:
    f = open(filename)
    for line in f:
        print(line)
    
def ls(root_dir: str) -> None:
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            print(f"{root}/{filename}")

def ls(root_dir: str) -> None:
    for _, _, files in os.walk(root_dir):
        for filename in files:
            print(f"{root}/{filename}")

class DB(object):
    def __init__(self, filename: str) -> None:
        self._con = sqlite3.connect(filename)
    
def select(db: DB, query: str) -> None:
    cur = db._con.cursor()
    for row in cur.execute(query):
        print(row)

def tables(db: DB) -> None:
    return select(db, "select * from sqlite_master")
        
tdb()
tdb("--version")
tdb("init")

os.chdir("../bowser/")
tdb("compile")
tdb("run")

cat("../.dbt/profiles.yml")
cat("./dbt_project.yml")
cat("./models/example/my_second_dbt_model.sql")
cat("./target/compiled/db/models/example/my_second_dbt_model.sql")

db = DB("./dev.db")
tables(db)
select(db, "select * from my_first_dbt_model")
select(db, "select * from my_second_dbt_model")
