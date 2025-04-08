import pandas as pd
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

tasks = pd.DataFrame(columns=["Employee", "Task", "Start Time", "End Time", "Duration"])

def add_task(employee, task):
    start_time = time.time()
    tasks.loc[len(tasks)] = [employee, task, start_time, None, None]
    print(f"Task '{task}' started for {employee}")

def complete_task(employee):
    end_time = time.time()
    task = tasks[tasks["Employee"] == employee].iloc[-1]
    tasks.at[task.name, "End Time"] = end_time
    tasks.at[task.name, "Duration"] = end_time - task["Start Time"]
    print(f"Task completed for {employee}")

def generate_report():
    tasks["Duration"].plot(kind="bar", x=tasks["Task"], y=tasks["Duration"], title="Task Durations")
    plt.xlabel("Task")
    plt.ylabel("Duration (seconds)")
    plt.show()

def time_management_suggestions():
    avg_duration = tasks["Duration"].mean()
    print(f"Average task duration: {avg_duration:.2f} seconds")

    inefficient_tasks = tasks[tasks["Duration"] > avg_duration]
    if not inefficient_tasks.empty:
        print("Inefficient tasks identified:")
        print(inefficient_tasks)
    else:
        print("No inefficient tasks identified.")

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Task Manager")

        self.employee_label = tk.Label(self.root, text="Employee Name:")
        self.employee_label.grid(row=0, column=0)
        self.employee_entry = tk.Entry(self.root)
        self.employee_entry.grid(row=0, column=1)

        self.task_label = tk.Label(self.root, text="Task Name:")
        self.task_label.grid(row=1, column=0)
        self.task_entry = tk.Entry(self.root)
        self.task_entry.grid(row=1, column=1)

        self.start_button = tk.Button(self.root, text="Start Task", command=self.start_task)
        self.start_button.grid(row=2, column=0)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=1)

        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=3, column=0, columnspan=2)

    def start_task(self):
        employee = self.employee_entry.get()
        task = self.task_entry.get()
        if employee and task:
            add_task(employee, task)
            messagebox.showinfo("Task Started", f"Task '{task}' started for {employee}")
        else:
            messagebox.showerror("Error", "Both fields must be filled.")

    def complete_task(self):
        employee = self.employee_entry.get()
        if employee:
            complete_task(employee)
            messagebox.showinfo("Task Completed", f"Task completed for {employee}")
        else:
            messagebox.showerror("Error", "Employee name must be filled.")

    def generate_report(self):
        generate_report()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
