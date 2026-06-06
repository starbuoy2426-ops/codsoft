import json
import os
from datetime import datetime

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append({
            "id": len(tasks) + 1,
            "task": task,
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        print("✅ Task added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("📭 Your to-do list is empty!")
        return
    print("\n" + "="*60)
    print(f"{'ID':<4} {'Status':<10} {'Task':<35} {'Created':<20}")
    print("="*60)
    for t in tasks:
        status = "✅ Done" if t["completed"] else "⏳ Pending"
        print(f"{t['id']:<4} {status:<10} {t['task']:<35} {t['created']:<20}")
    print("="*60)

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        for t in tasks:
            if t["id"] == task_id:
                t["completed"] = True
                print(f"✅ Task {task_id} marked as completed!")
                return
        print("❌ Task ID not found.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        for i, t in enumerate(tasks):
            if t["id"] == task_id:
                del tasks[i]
                print(f"🗑️ Task {task_id} deleted!")
                # Re-number IDs
                for idx, task in enumerate(tasks):
                    task["id"] = idx + 1
                return
        print("❌ Task ID not found.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("🚀 Welcome to the To-Do List App!")
    print("A useful project that helps users manage and organize their tasks efficiently.")
    
    while True:
        print("\n" + "-"*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Goodbye! Your tasks have been saved.")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        save_tasks(tasks)  # Auto-save after each action

if __name__ == "__main__":
    main()