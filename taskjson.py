import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as s:
            json.dump([], s)
        return []
    with open(FILENAME, "r", encoding="utf-8") as s:
        return json.load(s)
    

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as s:
        json.dump(tasks, s, indent=4, ensure_ascii=False)
