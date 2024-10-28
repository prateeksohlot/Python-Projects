import json
import os
import sys
from datetime import datetime

FILENAME = 'task_data.json'

class TaskTracker:
    def __init__(self,filename):
        self.filename = filename
        
    def load_task(self):
        # Load JSON data from a file
        if not os.path.isfile('task_data.json'):
            with open('task_data.json', 'w') as json_file:
                json.dump([], json_file, indent=4)
            print(f"JSON file '{FILENAME}' created successfully.")

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

def main():
    tracker = TaskTracker(FILENAME)

    if sys.argv[1].lower() == 'add':
        tracker.add_task(sys.argv[-1])

    if sys.argv[1].lower() == 'update':
            task_id = int(sys.argv[2])
            tracker.update_task(task_id, sys.argv[-1])

    if sys.argv[1].lower() == 'delete':
        task_id = int(sys.argv[-1])
        tracker.update_task(task_id)
    
    if sys.argv[-1].lower() == 'list' and len(sys.argv) == 2:
        tracker.all_tasks()

    if sys.argv[1].lower() == 'list' and len(sys.argv) > 2:
        if sys.argv[-1] == 'done':
            tracker.print_by_task('done')
        if sys.argv[-1] == 'todo':
            tracker.print_by_task('todo')
        if sys.argv[-1] == 'in-progress':
            tracker.print_by_task('in-progress')

    if sys.argv[1].lower() == 'mark-in-progress':
        task_id = int(sys.argv[-1])
        tracker.mark_task(task_id, 'in-progress')

    if sys.argv[1].lower() == 'mark-done':
        task_id = int(sys.argv[-1])
        tracker.mark_task(task_id, 'done')
    
if __name__ == "__main__":
    
    main()
    