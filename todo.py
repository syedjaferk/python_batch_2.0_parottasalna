import sys
task_list = []

def save_tasks():
    task_file = open("tasks.txt", "w")
    for task_name, task_description, task_status in task_list:
        content = f"{task_name}||{task_description}||{task_status}\n"
        task_file.write(content)
    task_file.close()

def add_task(task_name, task_description):
    task_list.append([task_name, task_description, "PENDING"])
    print(f"Task {task_name} is successfully added.")
    save_tasks()

def list_tasks():
    for index, task in enumerate(task_list):
        print(f"{index} {'-'.join(task)}")

def load_tasks():
    task_file = open("tasks.txt", "r")
    tasks = task_file.readlines()
    for task in tasks:
        task = task.strip().split("||")
        task_list.append(task)

def update_task(task_index, task_status):
    task = task_list[task_index]
    task[2] = task_status
    save_tasks()


load_tasks()

if sys.argv[1] == "add" and len(sys.argv) == 4:
    task_name, task_description = sys.argv[2], sys.argv[3]
    add_task(task_name, task_description)
elif sys.argv[1] == "list":
    list_tasks()
elif sys.argv[1] == "update" and len(sys.argv) == 4:
    task_index, task_status = int(sys.argv[2]), sys.argv[3]
    update_task(task_index, task_status)
