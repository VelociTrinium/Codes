import Game1
import Game2
import Game3
import Game4
import Game5
import Game6
import Game7
import Game8

from tqdm import tqdm 
import time
import os

def loading_bar():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting...  "):        # NEW        # NEW
        time.sleep(0.03)

def show_menu():
    # loading_bar()
    print("""
🎮 8-Bit Games - Virtual Arcade 🎮
Choose a game to play or 'q' to quit:

1 : Guess the Number
2 : Hangman Quiz
3 : Rock, Paper, Scissors
4 : Tic Tac Toe
5 : 2048
6 : 4 in a Row
7 : Sudoku
8 : Python Syntax Checker
""")



def run():
    while True:
        show_menu()
        choice = input('> ').strip().lower()
        
        if choice == 'q':
            print("Thanks for playing! Goodbye!")
            break
        elif choice == '1':
            loading_bar()
            Game1.main()
        elif choice == '2':
            loading_bar()
            Game2.main()
        elif choice == '3':
            loading_bar()
            Game3.main()
        elif choice == '4':
            loading_bar()
            Game4.tic_tac_toe()
        elif choice == '5':
            loading_bar()
            Game5.main()
        elif choice == '6':
            loading_bar()
            Game6.play_game()
        elif choice == '7':
            loading_bar()
            Game7.play_sudoku()
        elif choice == '8':
            loading_bar()
            Game8.play_game()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run()
