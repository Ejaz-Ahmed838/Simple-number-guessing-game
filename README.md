# 🎯 Number Guessing Game (Python + Tkinter)

A fun and interactive number guessing game built using Python and the Tkinter library. Guess the number between 1 and 100 in 10 attempts and try to score as high as possible!

---

## 🧠 Game Rules

- You have **10 attempts** to guess the correct number.
- The number is randomly generated between **1 and 100**.
- After each guess, the game gives you a **hint**:
  - "Try big guess" if your guess is too low.
  - "Try low guess" if your guess is too high.
- Points are awarded based on how close your guess is:
  - Exact guess: 🎉 +100 points
  - Close guess: +20, 15, 10, 5, or 2 points depending on difference
- Final bonus: Remaining attempts × 20 points if the guess is correct.
- Game ends if the correct number is guessed or attempts reach zero.

---

## 🖥️ GUI Features

- Entry field with placeholder text
- Score and Lives display
- Hint messages
- Buttons: **Submit**, **Restart**, **Play Again**, and **Quit**
- GUI design with colors and styles for better UX

---

## 📦 Requirements

- Python 3.x (no external libraries needed)
- Tkinter (comes pre-installed with Python)

---

## 🚀 How to Run

1. Clone or download the repository.
2. Open the `.py` file in your Python IDE.
3. Run the script:

```bash
python guess_game.py
