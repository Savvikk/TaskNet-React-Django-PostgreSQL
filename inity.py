import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
import mtasks

tm = mtasks.TaskManager()

def entry_task():
    task_title = title.get()
    task_priority = priority.get()
    task_due_date = due_date.get()

    if not task_title.strip():
        print("Podaj tytuł zadania")
        return
    
    tm.add_task(task_title, task_priority, task_due_date)
    title.delete(0, ctk.END)
    priority.delete(0, ctk.END)
    due_date.delete(0, ctk.END)



def open_calendar():
    def select_date():
        selected_date = cal.selection_get()
        due_date.delete(0, ctk.END)
        due_date.insert(0, selected_date.strftime("%Y-%m-%d"))
        top.destroy()

    top = tk.Toplevel(app)
    top.title("Wybierz datę końcową")
    cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    select_btn = ctk.CTkButton(top, text="Wybierz", command=select_date)
    select_btn.pack(pady=10)

    select_btn = ctk.CTkButton(top, text="Wybierz", command=select_date)
    select_btn.pack(pady=10)


app = ctk.CTk()
app.geometry("400x300")
app.title("python_todo")


title = ctk.CTkEntry(app, placeholder_text="Zadanie")
title.grid()
priority = ctk.CTkEntry(app, placeholder_text="Ważność")
priority.grid()
due_date = ctk.CTkEntry(app, placeholder_text="Data (YYYY-MM-DD)")
due_date.grid()
calendar_btn = ctk.CTkButton(app, text="Wybierz datę końcową", command=open_calendar)
calendar_btn.grid()

button = ctk.CTkButton(app, text="Dodaj", command=entry_task)
button.grid()


tm.get_tasks()

tasks_display = ctk.CTkTextbox(app, width=380, height=150)
tasks_display.grid()



app.mainloop()
