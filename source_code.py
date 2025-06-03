from tkinter import *
import random

class Game():

    button_style = {
        "padx": 5,
        "pady": 5,
        "width": 8,
        'height':1,
        "borderwidth": 1,
        "highlightthickness": 0,
        "relief": "raised",
        "bg": "#e6bfbf",
        "activebackground": "#f0f0f0",
        "cursor": "hand2",
    }

    def __init__(self, window):
        self.attempts = 10
        self.Guess_number = ''
        self.placeholder = 'Enter your Guess'
        self.window = window
        self.player_score = 0
        self.target_number = random.randint(1, 100)

        self.label = Label(window, text="🎯 Number Guessing Game 🎯", fg="#FF6347", bg="#F5FFFA",
                         font=("Comic Sans MS", 20, "bold"))
        self.label.pack(fill='both')

        self.frame = LabelFrame(self.window, background='#D3D3D3')
        self.frame.pack(fill='both', padx=10, pady=10, expand=True)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.center_frame = Frame(self.frame, background='#D3D3D3')
        self.center_frame.grid(row=0, column=0, sticky="nsew")

        self.entry = Entry(self.center_frame, font=("Arial", 18), fg='gray', width=25)
        self.entry.pack(pady=(40, 10))
        self.entry.insert(0, self.placeholder)

        self.entry.bind("<Key>", self.on_key_press)
        self.entry.bind("<FocusIn>", self.in_focus)
        self.entry.bind("<FocusOut>", self.out_focus)

        self.score = Label(self.frame, text=f'Score: {self.player_score}', font=("Arial", 10), bg='#D3D3D3')
        self.score.grid(row=4, column=0, padx=0, pady=15, sticky="nsew")

        self.lives = Label(self.frame, text=f'Lives: {self.attempts}', font=("Arial", 10), bg='#D3D3D3')
        self.lives.grid(row=1, column=0, padx=0, pady=5, sticky="nsew")

        self.hints = Label(self.frame, text='Number between (1,100)',font=("Arial", 10), bg='#D3D3D3')
        self.hints.grid(row=3, column=0, padx=0, pady=5, sticky="nsew")
        
        self.create_buttons()

    def on_key_press(self, event):
        if event.keysym.isdigit():
            self.entry.config(fg='black')
            self.Guess_number += event.char
        elif event.keysym == 'BackSpace':
            self.Guess_number = self.Guess_number[:-1]

        self.entry.delete(0, END)
        self.entry.insert(0, self.Guess_number)

        if self.Guess_number == '':
            self.set_placeholder()

        return 'break'

    def in_focus(self, event):
        if self.entry.get() == self.placeholder and self.entry.cget("fg") == "gray":
            self.entry.delete(0, END)
            self.entry.config(fg='black')
            self.Guess_number = ''

    def out_focus(self, event):
        if self.entry.get() == '':
            self.set_placeholder()

    def set_placeholder(self):
        self.entry.config(fg='gray')
        self.entry.delete(0, END)
        self.entry.insert(0, self.placeholder)

    def create_buttons(self):
        self.button_frame = Frame(self.center_frame, background='#D3D3D3')
        self.button_frame.pack()

        self.restart_btn = Button(self.button_frame, text='Restart', font=("Arial", 10),
                                  **Game.button_style, command=self.restart)
        self.restart_btn.grid(row=0, column=0, padx=2, pady=0)

        self.submit_btn = Button(self.button_frame, text='Submit', font=("Arial", 10),
                                 **Game.button_style, command=self.submit)
        self.submit_btn.grid(row=0, column=1, padx=2, pady=0)

        self.play_again_btn = Button(self.button_frame, text='Play again', state='disabled',
                                     font=("Arial", 10), **Game.button_style, command=self.restart)
        self.play_again_btn.grid(row=0, column=2, padx=2, pady=0)

        self.quit_btn = Button(self.button_frame, text='Quit', font=("Arial", 10),
                               **Game.button_style, command=self.window.quit)
        self.quit_btn.grid(row=0, column=3, padx=2, pady=0)

    def restart(self):
        self.Guess_number = ''
        self.target_number = random.randint(1, 100)
        print(self.target_number)
        self.attempts = 10
        self.player_score = 0
        self.entry.config(state='normal')
        self.submit_btn.config(state='normal')
        self.play_again_btn.config(state='disabled')
        self.set_placeholder()
        self.lives.config(text=f'lives: {self.attempts}')
        self.score.config(text=f'Score: {self.player_score}')
        self.hints.config(text='Number between (1,100)')

    def submit(self):
        if not self.Guess_number.isdigit():
            return 

        guess = int(self.Guess_number)
        absolute_dif = abs(self.target_number - guess)

        if absolute_dif == 0:
            self.player_score += 100
            self.entry.delete(0, END)
            self.entry.insert(0, "🎉 Correct!")
            self.entry.config(state='disabled')
            self.submit_btn.config(state='disabled')
            self.play_again_btn.config(state='normal')
            self.hints.config(text='🎉 You Done it')

        elif self.attempts > 1:
            if absolute_dif <= 10 :
                self.player_score += 20
            elif absolute_dif <= 30:
                self.player_score += 15
            elif absolute_dif <= 60:
                self.player_score += 10
            elif absolute_dif <= 80:
                self.player_score += 5
            else:
                self.player_score += 2

            self.attempts -= 1
            self.set_placeholder()

        else:
            self.attempts = 0
            self.entry.delete(0, END)
            self.entry.insert(0, f'💥 Game Over! Number was {self.target_number}')
            self.entry.config(state='disabled')
            self.submit_btn.config(state='disabled')
            self.play_again_btn.config(state='normal')
        if self.attempts==0 or absolute_dif==0:
            self.player_score += self.attempts*20
        self.lives.config(text=f'Lives: {self.attempts}')
        self.score.config(text=f'Score: {self.player_score}')
        self.Guess_number = ''
        if guess >self.target_number:
            self.hints.config(text='Try Low Guess')
        elif guess<self.target_number:
            self.hints.config(text='Try big Guess')



if __name__ == "__main__":
    window = Tk()
    window.title("Guess Game")
    window.geometry('400x300')
    window.configure(bg='#D3D3D3')
    window.resizable(False, False)

    player = Game(window)
    window.mainloop()
