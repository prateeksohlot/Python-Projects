import json
import os
import sys
from datetime import datetime

FILENAME = 'task_data.json'

def create_json():
    "We create and initialise JSON File"

    tasks = []

    # Write the data to a JSON file
    with open(FILENAME, 'w') as json_file:
        json.dump(tasks, json_file, indent=4)
    print(f"JSON file '{FILENAME}' created successfully.")


class TaskTracker:
    def __init__(self,filename):
        self.filename = filename
        
    def load_task(self):
        # Load JSON data from a file
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    def save_task(self, tasks):
        with open(FILENAME, 'w') as json_file:
            json.dump(tasks, json_file, indent=4)


    def add_task(self, description):
        tasks = self.load_task()
        task_id = len(tasks) + 1
        
        ids = [t['id'] for t in tasks]
        while True:
            if task_id in ids:
                task_id += 1
            else:
                break

        task = {
            'id': task_id,
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updateAt': datetime.now().isoformat()
        }
        tasks.append(task)
        self.save_task(tasks)
        print(f'Task added successfully (ID: {task_id})') 

    def update_task(self, task_id, new_description):
        tasks = self.load_task()

        for task in tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                task['updateAt'] = datetime.now().isoformat()

        self.save_task(tasks)
        print(f'Task updated (ID: {task_id}) to {new_description}') 
    
    def remove_task(self, task_id):
        tasks = self.load_task()

        updated_task = list(filter(lambda task: task.get('id') != task_id, tasks))
        self.save_task(updated_task)
        print(f'Task Deleted successfully (ID: {task_id})') 


    def all_tasks(self):
        tasks = self.load_task()

        for task in tasks:
            print(task['description'])

    def print_by_task(self, status):
        tasks = self.load_task()

        for task in tasks:
            if task['description'] == status:
                print(task['description']) 

    
    def mark_task(self, task_id, status):
        tasks = self.load_task()

        for task in tasks:
            if task['id'] == task_id:
                task['status'] = status
                task['updateAt'] = datetime.now().isoformat()
        self.save_task(tasks)
        print(f'Task (ID: {task_id}) make to {status}') 


if __name__ == "__main__":
    # Resetting Task list every run
    create_json()

    tracker = TaskTracker(FILENAME)

    while True:
        input_text = input()

        if input_text.lower() == "quit":
            print("Program is closing")
            break
        
        if input_text.split()[0].lower() == 'add':
            task = input_text.split('"')[1]
            tracker.add_task(task)

        if input_text.split()[0].lower() == 'update':
            task_id = int(input_text.split()[1])
            task = input_text.split('"')[1]
            tracker.update_task(task_id, task)

        if input_text.split()[0].lower() == 'delete':
            task_id = int(input_text.split()[1])
            tracker.remove_task(task_id)

        if input_text.split()[0].lower() == 'list' and len(input_text.split()[0]) == 1:
            tracker.all_tasks()

        if input_text.split()[0].lower() == 'list' and len(input_text.split()[0]) > 1:
            if input_text.split()[1] == 'done':
                tracker.print_by_task('done')
            if input_text.split()[1] == 'todo':
                tracker.print_by_task('todo')
            if input_text.split()[1] == 'in-progress':
                tracker.print_by_task('in-progress')

        if input_text.split()[0].lower() == 'mark-in-progress':
            task_id = int(input_text.split()[1])
            tracker.mark_task(task_id, 'in-progress')
        
        if input_text.split()[0].lower() == 'mark-done':
            task_id = int(input_text.split()[1])
            tracker.mark_task(task_id, 'done')