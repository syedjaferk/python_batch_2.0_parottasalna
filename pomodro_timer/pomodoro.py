import time
import os
from plyer import notification
import requests

DEFAULT_POMODORO_TIMER_MINUTES = 25
DEFAULT_SHORT_BREAK_TIME = 5
DEFAULT_LONG_BREAK_TIME = 15
DEFAULT_CYCLES_FOR_LONG_BREAK = 3


def clear_window():
    os.system("clear")

def time_run(minutes):
    total_seconds = minutes * 60
    total_seconds = 10
    while total_seconds:
        min = total_seconds // 60
        seconds = total_seconds % 60
        print(f"\rTime Left {min:02d}:{seconds:02d}", end="")
        time.sleep(1)
        total_seconds -= 1

def notify(msg):
    notification.notify(title="Pomodoro Timer", message=msg, timeout=5)
    requests.post("https://ntfy.sh/py_class_test",data=msg)

def pomodoro_timer(tasks):

    cycles = 1
    task_counter = 0
    while cycles <= len(tasks):
        clear_window()
        print(f"Pomodoro Session for {tasks[task_counter]} Started !!! ")
        time_run(DEFAULT_POMODORO_TIMER_MINUTES)
        if cycles < DEFAULT_CYCLES_FOR_LONG_BREAK:
            notify("Short Break Started !!")
            time_run(DEFAULT_SHORT_BREAK_TIME)
            task_counter += 1
        else:
            notify("Long Break Started !!!")
            time_run(DEFAULT_LONG_BREAK_TIME)
            task_counter += 1
            # break
        cycles += 1

def get_tasks():
    is_task = True
    tasks = []
    while is_task:
        task = input("Enter your Task Name : ")
        tasks.append(task)
        any_more_task = input("Do you have any more tasks ? (y/n) : ")
        if any_more_task.strip().lower() == "n":
            is_task = False
    return tasks

def main():
    tasks = get_tasks()
    pomodoro_timer(tasks)

if __name__=='__main__':
    main()