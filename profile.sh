python -m cProfile -s 'cumulative' core/dbt/main.py > profile.txt
sudo py-spy record -o profile.svg -- python core/dbt/main.py
time python core/dbt/main.py