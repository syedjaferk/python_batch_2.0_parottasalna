import time
import os
import platform

# Default durations in minutes
DEFAULT_WORK_DURATION = 25
DEFAULT_SHORT_BREAK = 5
DEFAULT_LONG_BREAK = 15
POMODOROS_BEFORE_LONG_BREAK = 4

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def notify(message):
    print(f"\n🔔 {message}")
    # For Windows, you can use winsound.Beep
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 500)
    else:
        print('\a')  # Beep for Unix-like systems

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {time_format}", end="")
        time.sleep(1)
        total_seconds -= 1
    print()  # Move to the next line after countdown

def pomodoro_timer(work_duration, short_break, long_break, cycles):
    pomodoro_count = 0
    while True:
        clear_console()
        print(f"🍅 Pomodoro Session {pomodoro_count + 1}")
        countdown(work_duration)
        pomodoro_count += 1
        notify("Work session complete!")

        if pomodoro_count % cycles == 0:
            print("🛌 Time for a long break!")
            countdown(long_break)
            notify("Long break over!")
        else:
            print("☕ Time for a short break!")
            countdown(short_break)
            notify("Short break over!")

        user_input = input("Start next Pomodoro? (y/n): ").strip().lower()
        if user_input != 'y':
            print("👋 Session ended. Great job!")
            break

if __name__ == "__main__":
    try:
        work_duration = int(input(f"Enter work duration in minutes (default {DEFAULT_WORK_DURATION}): ") or DEFAULT_WORK_DURATION)
        short_break = int(input(f"Enter short break duration in minutes (default {DEFAULT_SHORT_BREAK}): ") or DEFAULT_SHORT_BREAK)
        long_break = int(input(f"Enter long break duration in minutes (default {DEFAULT_LONG_BREAK}): ") or DEFAULT_LONG_BREAK)
        cycles = int(input(f"Enter number of Pomodoros before a long break (default {POMODOROS_BEFORE_LONG_BREAK}): ") or POMODOROS_BEFORE_LONG_BREAK)
    except ValueError:
        print("Invalid input. Using default settings.")
        work_duration = DEFAULT_WORK_DURATION
        short_break = DEFAULT_SHORT_BREAK
        long_break = DEFAULT_LONG_BREAK
        cycles = POMODOROS_BEFORE_LONG_BREAK

    pomodoro_timer(work_duration, short_break, long_break, cycles)
