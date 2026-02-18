🤖 Computer Guessing Game (Console-Based)

A fun and interactive Number Guessing Game where the computer tries to guess the number you are thinking of!

Instead of the user guessing, the roles are reversed — you think of a number, and the computer guesses it using logic.

📌 Features

🤖 Computer guesses the number

🎯 User gives feedback (High / Low / Correct)

⚡ Efficient guessing using binary search logic

🔁 Continuous guessing until correct answer

🎉 Winning message when guessed correctly

🛠️ Technologies Used

Python 3

Core concepts:

Loops (while)

Conditional statements (if-elif-else)

User input (input())

📂 Project Structure
computer-guessing-game/
│
├── main.py        # Game logic
├── README.md      # Documentation

⚙️ Requirements

Before running this project, make sure you have:

Python 3 installed
👉 https://www.python.org/downloads/

Check installation:

python --version

🚀 How to Run the Game

Clone the repository:

git clone https://github.com/your-username/computer-guessing-game.git


Navigate to the project folder:

cd computer-guessing-game


Run the game:

python main.py

🎮 How to Play

Think of a number within a given range (e.g., 1 to 100)

The computer will try to guess your number

After each guess, provide feedback:

h → Too High  
l → Too Low  
c → Correct  


The computer will adjust its guess based on your feedback

The game continues until the correct number is guessed

💡 Example Gameplay
Think of a number between 1 and 100

Computer guesses: 50
Is it too High (h), too Low (l), or Correct (c)? l

Computer guesses: 75
Is it too High (h), too Low (l), or Correct (c)? h

Computer guesses: 62
Is it too High (h), too Low (l), or Correct (c)? c

🎉 The computer guessed your number!

⚙️ Logic Used

The game uses Binary Search Algorithm:

Start with a range (low = 1, high = 100)

Guess the middle number

Adjust range based on feedback

Repeat until correct

This makes the guessing fast and efficient.

🔄 Future Improvements

Add difficulty levels

Track number of attempts

Add GUI version using Streamlit / Tkinter

Add voice interaction

👩‍💻 Author

Fatimah Noman

Python Learner 🚀

Exploring Agentic AI 🤖

⭐ Support

If you like this project, give it a ⭐ on GitHub!

📜 License

This project is open-source and free to use.
