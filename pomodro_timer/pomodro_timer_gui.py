import time
import threading
import tkinter as tk
from tkinter import messagebox
from plyer import notification
import matplotlib.pyplot as plt

# Constants (in seconds)
WORK_DURATION = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
CYCLES_BEFORE_LONG_BREAK = 4

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("400x300")
        self.timer_running = False
        self.session_count = 0
        self.completed_sessions = []
        self.current_task = tk.StringVar()
        self.focus_mode = False
        self.current_timer_thread = None

        self._build_ui()

    def _build_ui(self):
        # Task Entry
        tk.Label(self.root, text="Current Task:").pack(pady=5)
        self.task_entry = tk.Entry(self.root, textvariable=self.current_task, width=40)
        self.task_entry.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(self.root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=10)

        # Buttons
        tk.Button(self.root, text="▶️ Start", command=self.start_timer).pack(pady=5)
        tk.Button(self.root, text="⏹️ Stop", command=self.stop_timer).pack(pady=5)
        tk.Button(self.root, text="📊 Show Stats", command=self.show_stats).pack(pady=5)
        tk.Button(self.root, text="🧘 Focus Mode", command=self.toggle_focus).pack(pady=5)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.current_timer_thread = threading.Thread(target=self.run_session, daemon=True)
            self.current_timer_thread.start()

    def stop_timer(self):
        self.timer_running = False

    def toggle_focus(self):
        self.focus_mode = not self.focus_mode
        self.root.attributes("-fullscreen", self.focus_mode)
        if not self.focus_mode:
            self.root.geometry("400x300")

    def run_session(self):
        while self.timer_running:
            self.session_count += 1
            self._run_timer(WORK_DURATION, f"Pomodoro {self.session_count}", "Work")
            if not self.timer_running:
                break

            if self.session_count % CYCLES_BEFORE_LONG_BREAK == 0:
                self._run_timer(LONG_BREAK, "Long Break", "Break")
            else:
                self._run_timer(SHORT_BREAK, "Short Break", "Break")

    def _run_timer(self, duration, label, session_type):
        notification.notify(title="Pomodoro Timer", message=f"{label} started!", timeout=3)
        start_time = time.time()

        while self.timer_running and time.time() - start_time < duration:
            remaining = int(duration - (time.time() - start_time))
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)

        if self.timer_running:
            notification.notify(title="Pomodoro Timer", message=f"{label} complete!", timeout=3)
            if session_type == "Work":
                self.completed_sessions.append((self.current_task.get() or "Unnamed Task", time.time()))

    def show_stats(self):
        if not self.completed_sessions:
            messagebox.showinfo("Stats", "No work sessions completed yet.")
            return

        tasks = [task for task, _ in self.completed_sessions]
        task_counts = {t: tasks.count(t) for t in set(tasks)}

        plt.bar(task_counts.keys(), task_counts.values(), color='green')
        plt.title("Pomodoro Task Stats")
        plt.ylabel("Pomodoros Completed")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
