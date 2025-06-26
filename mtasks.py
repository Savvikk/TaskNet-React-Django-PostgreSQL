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

