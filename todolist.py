import sys
import os

TASK_FILE = "tasks_pradeep.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        lines = f.readlines()
        return [line.strip().split("||") for line in lines if line.strip()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for desc, status in tasks:
            f.write(f"{desc}||{status}\n")

def add_task(task_desc):
    tasks = load_tasks()
    tasks.append([task_desc, "pending"])
    save_tasks(tasks)
    print(f"✅ Added: {task_desc}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Your to-do list is empty.")
        return
    for i, (desc, status) in enumerate(tasks, 1):
        mark = "✔️" if status == "done" else "⏳"
        print(f"{i}. [{mark}] {desc}")

def delete_task(task_num):
    tasks = load_tasks()
    if task_num < 1 or task_num > len(tasks):
        print("❌ Invalid task number.")
        return
    removed = tasks.pop(task_num - 1)
    save_tasks(tasks)
    print(f"🗑️ Deleted: {removed[0]}")

def mark_done(task_num):
    tasks = load_tasks()
    if task_num < 1 or task_num > len(tasks):
        print("❌ Invalid task number.")
        return
    tasks[task_num - 1][1] = "done"
    save_tasks(tasks)
    print(f"🎉 Marked as done: {tasks[task_num - 1][0]}")

def show_help():
    print("\n📝 Command Line To-Do List")
    print("Usage:")
    print("  python todo.py add 'Task description'     → Add a new task")
    print("  python todo.py list                       → Show all tasks")
    print("  python todo.py done <task-number>         → Mark task as done")
    print("  python todo.py delete <task-number>       → Delete a task")
    print("  python todo.py help                       → Show this help\n")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        task_desc = " ".join(sys.argv[2:])
        add_task(task_desc)
    elif command == "list":
        list_tasks()
    elif command == "delete" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        delete_task(int(sys.argv[2]))
    elif command == "done" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        mark_done(int(sys.argv[2]))
    elif command == "help":
        show_help()
    else:
        print("❗ Unknown command or invalid arguments.")
        show_help()

if __name__ == "__main__":
    main()
