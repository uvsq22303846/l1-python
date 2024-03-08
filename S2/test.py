import random
import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind")
        self.master.geometry("400x400")

        self.colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
        self.secret_code = [random.choice(self.colors) for _ in range(4)]
        self.current_row = 0
        self.create_widgets()
    
    def create_widgets(self):
        self.color_pickers = []
        for i in range(4):
            color_picker = tk.Button(self.master, bg=self.colors[0], width=3, command=lambda idx=i: self.change_color(idx))
            self.color_pickers.append(color_picker)
            color_picker.grid(row=self.current_row, column=i, padx=5, pady=5)
        
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess)
        self.submit_button.grid(row=self.current_row, column=4, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=self.current_row+1, columnspan=5, padx=5, pady=5)

    def change_color(self, idx):
        current_color_index = self.colors.index(self.color_pickers[idx]['bg'])
        next_color_index = (current_color_index + 1) % len(self.colors)
        self.color_pickers[idx]['bg'] = self.colors[next_color_index]

    def check_guess(self):
        guess = [color['bg'] for color in self.color_pickers]
        correct_color_and_position = sum(1 for i in range(4) if guess[i] == self.secret_code[i])
        correct_color_only = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess))
        
        result_text = f"{correct_color_and_position} correct color and position, {correct_color_only} correct color only."
        self.result_label.config(text=result_text)
        
        self.current_row += 2
        self.create_widgets()

        if correct_color_and_position == 4:
            messagebox.showinfo("Congratulations!", "You guessed the code!")
            self.master.destroy()

def main():
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()