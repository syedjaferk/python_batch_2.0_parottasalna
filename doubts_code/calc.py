task_list = [["task a"], ["task b"]]

print(id(task_list))
print(id(task_list[0]))


new = task_list[0]
print(id(new))