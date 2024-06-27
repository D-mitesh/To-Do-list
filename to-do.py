import json
import os
from datetime import datetime

DATA_FILE = 'tasks.json'

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} [Priority: {self.priority}] [Due: {self.due_date}] {self.description}"

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        try:
            self.tasks.pop(index)
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        try:
            self.tasks[index].completed = True
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def save_tasks(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task_data) for task_data in tasks_data]

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ").lower()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(description, priority, due_date)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()