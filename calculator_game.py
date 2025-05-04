import tkinter as tk
import random
from tkinter import messagebox

class CalculatorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Game")
        
        self.score = 0
        self.user_input = ''
        self.current_problem = {}

        self.problem_label = tk.Label(root, text="", font=("Arial", 20))
        self.problem_label.pack(pady=10)

        self.input_label = tk.Label(root, text="", font=("Arial", 18))
        self.input_label.pack(pady=5)

        self.create_buttons()
        
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.generate_problem()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ('7', lambda: self.press('7')),
            ('8', lambda: self.press('8')),
            ('9', lambda: self.press('9')),
            ('C', self.clear_input),
            ('4', lambda: self.press('4')),
            ('5', lambda: self.press('5')),
            ('6', lambda: self.press('6')),
            ('=', self.submit_answer),
            ('1', lambda: self.press('1')),
            ('2', lambda: self.press('2')),
            ('3', lambda: self.press('3')),
            ('0', lambda: self.press('0')),
        ]

        row = 0
        col = 0
        for (text, command) in buttons:
            button = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14), command=command)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def generate_problem(self):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        ops = ['+', '-', '*']
        op = random.choice(ops)
        answer = eval(f"{a}{op}{b}")
        self.current_problem = {'a': a, 'b': b, 'op': op, 'answer': answer}
        self.problem_label.config(text=f"{a} {op} {b} = ?")
        self.user_input = ''
        self.input_label.config(text=self.user_input)

    def press(self, num):
        self.user_input += num
        self.input_label.config(text=self.user_input)

    def clear_input(self):
        self.user_input = ''
        self.input_label.config(text=self.user_input)

    def submit_answer(self):
        try:
            if int(self.user_input) == self.current_problem['answer']:
                self.score += 10
                messagebox.showinfo("Correct!", "Good Job!")
            else:
                messagebox.showerror("Wrong!", f"Correct answer: {self.current_problem['answer']}")
            self.score_label.config(text=f"Score: {self.score}")
            self.generate_problem()
        except ValueError:
            messagebox.showwarning("Invalid", "Please enter a valid number!")

if __name__ == "__main__":
    root = tk.Tk()
    game = CalculatorGame(root)
    root.mainloop()
