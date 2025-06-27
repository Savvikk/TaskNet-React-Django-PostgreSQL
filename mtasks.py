import json
from taskjson import save_tasks

class Task:
    def __init__(self, id, title, priority=None, due_date=None):
        self.id = id
        self.title = title
        self.done = False
        self.priority = priority
        self.due_date = due_date

    def mark_done(self):
        if not self.done:
            self.done = True



class TaskManager:
    def __init__(self):
        self.tasks = []




    def add_task(self, title, priority=None, due_date=None):
        new_task = {
            "title" : title,
            "priority" : priority,
            "due_date" : due_date,
            "done" : False
        }
        self.tasks.append(new_task)
        save_tasks(self.tasks)


    def load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as s:
                self.tasks = json.load(s)
        except FileNotFoundError:
            self.tasks = []    

    def remove_task(self, title):
        for task in self.tasks:
            if task in self.tasks == title:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True
        return False
    
    def get_tasks(self):
        print(f"{'Zadanie':<15} | {'Waznosc':<10} | {'Termin':<12} | {'Ukonczone'}")
        print("-" * 55)
        for task in self.tasks:
            print(f"{task['title']:<15} | {task['priority']:<10} | {task['due_date']:<12} | {task['done']}")

