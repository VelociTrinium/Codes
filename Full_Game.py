from tqdm import tqdm 
import numpy as np
import traceback
import random
import time
import re
import os


################################################################

#guess the number

def G1_show_menu():
    print("""
🎮 Game - Guess the Number 🎮
Choose Game Mode:

1 : Single Player
2 : Multi Player
""")

def G1_get_hint(guess, correct_number):
    difference = abs(guess - correct_number)

    if difference >= 50:
        return "💀 Whoa! You missed by a mile! Try a completely different number!"
    elif difference >= 30:
        return "🤦 Oof! You're still quite far, but moving in the right direction."
    elif difference >= 20:
        return "🚀 You're getting warmer, but still not quite there!"
    elif difference >= 10:
        return "🔥 Hot! You're closing in on the target!"
    elif difference >= 5:
        return "⚡ Super close! The number is just around the corner!"
    else:
        return "💥 SO CLOSE! Almost there, just tweak your guess a little!"

def G1_input_number(prompt, min_val=None, max_val=None):
    while True:
        try:
            num = int(input(prompt))
            if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
                print(f"❌ Enter a number between {min_val} and {max_val}.")
                continue
            return num
        except ValueError:
            print("❌ Error! Please input a valid number.")

def G1_play_guessing_game(secret_number, attempts, player_name):
    guess_count = 0
    while guess_count < attempts:
        guess = G1_input_number(f"🔢 {player_name}, enter your guess: ", 1, 100)
        guess_count += 1

        if guess == secret_number:
            print(f"🎉 {guess} was the right number! You WON, {player_name}!")
            return

        hint = G1_get_hint(guess, secret_number)
        attempts_left = attempts - guess_count

        if attempts_left > 1:
            print(f"❌ Nope! {hint} Try again! 📉 Attempts left: {attempts_left}")
        elif attempts_left == 1:
            print(f"⚠ Last chance! {hint}")
        else:
            print(f"💀 The correct number was {secret_number}. Better luck next time, {player_name}!")

def G1_single_player():
    time.sleep(0.35)
    player = input("🎩 Player 1, enter your name: ").strip().title()
    time.sleep(0.5)

    secret_number = random.randint(1, 100)
    guess_limit = G1_input_number(f"{player}, how many attempts would you like? 🎯 ", 1, 100)

    print(f"\n🚀 {player}, get ready!")
    time.sleep(0.25)
    print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")
    time.sleep(1)

    G1_play_guessing_game(secret_number, guess_limit, player)

def G1_multiplayer():
    player1 = input("👑 Player 1, enter your name: ").strip().title()
    time.sleep(0.5)
    player2 = input("🦸‍♂ Player 2, enter your name: ").strip().title()
    time.sleep(0.5)

    print(f"\n🔐 {player1}, enter a secret number while {player2} looks away!")
    secret_number = G1_input_number(f"{player1}, enter a number between 1 and 100: ", 1, 100)
    guess_limit = G1_input_number(f"🎯 How many attempts does {player2} get? ", 1, 100)

    print(f"\n📱 Now, pass the device to {player2}!")
    time.sleep(1.5)

    print(f"\n⚔ {player2}, your mission: Guess the secret number!")
    time.sleep(0.25)
    print(f"🎲 You have {guess_limit} attempts!")
    time.sleep(1)

    G1_play_guessing_game(secret_number, guess_limit, player2)

def G1_replay():
    response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    return response == 'y'

def G1_main():
    G1_show_menu()
    while True:

        try:
            choice = int(input("👉 Choose mode (1 or 2): "))
        except ValueError:
            print("❌ Invalid input. Please enter 1 or 2.")
            continue

        if choice == 1:
            G1_single_player()
        elif choice == 2:
            G1_multiplayer()
        else:
            print("❌ Please enter a valid game mode (1 or 2).")
            continue

        if not G1_replay():
            print("\n👋 Thanks for playing! Goodbye!")
            time.sleep(0.4)
            break

################################################################

#syntax hangman 

hang = [
    "------  ",
    "|    |  ",
    "|    0  ",
    "|   /|\\",
    "|   / \\",
    "|       "
]

def G2_print_hang(x):
    for i in range(x):
        print(hang[i])
        time.sleep(0.075)

def G2_ask_question(question, options, correct_option):
    print("\n" + question)
    for option in options:
        print(option)
    while True:
        try:
            user_choice = int(input("Enter your option (1-4): "))
            if 1 <= user_choice <= 4:
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    if user_choice == correct_option:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is: {options[correct_option - 1]}")
        return False

def G2_print_score(player_name, score, total):
    print(f"\nGame Over! {player_name}, your final score: {score}/{total}")

def G2_run_quiz(questions_subset, player_name):
    score = 0
    incorrect = 0
    for i, (question, options, correct_option) in enumerate(questions_subset):
        print(f"\nQuestion {i + 1}:")
        if G2_ask_question(question, options, correct_option):
            score += 1
        else:
            incorrect += 1
            if incorrect < 6:
                G2_print_hang(incorrect)
            else:
                break
    G2_print_score(player_name, score, len(questions_subset))
    if incorrect >= 6:
        G2_print_hang(6)
        print(f"{player_name} was Hanged")

def G2_single_player(questions):
    player_name = input("Player 1, input your name: ")
    time.sleep(0.1)
    G2_run_quiz(questions[:10], player_name)
    G2_play_again()

def G2_multiplayer(questions):
    player1 = input("Player 1, input your name: ")
    player2 = input("Player 2, input your name: ")
    score1 = score2 = incorrect1 = incorrect2 = 0

    for i in range(20):
        player = player1 if i % 2 == 0 else player2
        print(f"\n{player}, it's your turn!")
        question, options, correct_option = questions[i]
        if G2_ask_question(question, options, correct_option):
            if player == player1:
                score1 += 1
            else:
                score2 += 1
        else:
            if player == player1:
                incorrect1 += 1
                print(f"{player1}'s Hangman:")
                G2_print_hang(incorrect1)
                if incorrect1 >= 6:
                    print(f"{player1} was Hanged")
                    break
            else:
                incorrect2 += 1
                print(f"{player2}'s Hangman:")
                G2_print_hang(incorrect2)
                if incorrect2 >= 6:
                    print(f"{player2} was Hanged")
                    break
        print(f"\nCurrent Scores: {player1}: {score1}, {player2}: {score2}")

    print("\nGame Over! Final Scores:")
    print(f"{player1}: {score1}/10")
    print(f"{player2}: {score2}/10")
    if score1 > score2:
        print(f"{player1} Wins!")
    elif score2 > score1:
        print(f"{player2} Wins!")
    else:
        print("It's a tie!")
    G2_play_again()

def G2_play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            G2_main()
            break
        elif choice == "no":
            print("Thanks for playing!")
            time.sleep(0.4)
            break
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")

def G2_main():
    questions = [
        ("What will be the output of 'print(3 * 3 ** 2)'?", ["1. 27", "2. 18", "3. 81", "4. 9"], 1),
        ("Which of the following methods can add an element to a set?", ["1. add()", "2. append()", "3. insert()", "4. extend()"], 1),
        ("What will be the output of 'print(len({1, 2, 2, 3}))'?", ["1. 4", "2. 3", "3. 2", "4. Error"], 2),
        ("Which of these is a correct way to create an empty dictionary?", ["1. {}", "2. dict()", "3. {[]}", "4. Both 1 and 2"], 4),
        ("What is the output of 'print(bool(None))'?", ["1. True", "2. False", "3. None", "4. Error"], 2),
        ("Which function converts a string to a list of characters?", ["1. list()", "2. split()", "3. tuple()", "4. str()"], 1),
        ("What is the result of 'print([1, 2, 3] + [4, 5])'?", ["1. [1, 2, 3, 4, 5]", "2. [5, 7, 8]", "3. Error", "4. None"], 1),
        ("Which operator is used for floor division?", ["1. /", "2. //", "3. %", "4. **"], 2),
        ("What does 'print(type([]))' return?", ["1. <class 'list'>", "2. <class 'tuple'>", "3. <class 'dict'>", "4. <class 'set'>"], 1),
        ("How do you access the second element of a list 'x = [10, 20, 30]'?", ["1. x[2]", "2. x(1)", "3. x[1]", "4. x{1}"], 3),
        ("Which of the following creates a tuple?", ["1. (1,)", "2. (1)", "3. tuple(1, 2)", "4. {1, 2}"], 1),
        ("What is the output of 'print(10 % 3)'?", ["1. 3", "2. 1", "3. 10", "4. 0"], 2),
        ("What does 'print(sorted([3, 2, 5, 4]))' return?", ["1. [2, 3, 4, 5]", "2. (2, 3, 4, 5)", "3. {2, 3, 4, 5}", "4. None"], 1),
        ("Which function returns the total number of elements in a list?", ["1. size()", "2. length()", "3. len()", "4. count()"], 3),
        ("What does 'range(3)' return?", ["1. [0, 1, 2]", "2. (0, 1, 2)", "3. range object", "4. None"], 3),
        ("Which keyword is used to define a function in Python?", ["1. function", "2. define", "3. def", "4. fun"], 3),
        ("What is the output of 'print(type(3.0))'?", ["1. <class 'int'>", "2. <class 'float'>", "3. <class 'complex'>", "4. <class 'str'>"], 2),
        ("How do you remove an element from a dictionary?", ["1. del dict[key]", "2. dict.remove(key)", "3. dict.pop(key)", "4. Both 1 and 3"], 4),
        ("Which method is used to remove all elements from a list?", ["1. remove()", "2. clear()", "3. pop()", "4. del()"], 2),
        ("What will 'print(2 == 2.0)' return?", ["1. True", "2. False", "3. None", "4. Error"], 1),
        ("Which of the following is a valid variable name in Python?", ["1. 1variable", "2. variable_1", "3. variable-1", "4. variable 1"], 2),
        ("What is the output of 'print(type({}))'?", ["1. <class 'dict'>", "2. <class 'set'>", "3. <class 'list'>", "4. <class 'tuple'>"], 1),
        ("Which of the following is used for single-line comments in Python?", ["1. //", "2. <!-- -->", "3. #", "4. /* */"], 3),
        ("How do you create a list with numbers from 0 to 9 in Python?", ["1. list(range(10))", "2. range(10)", "3. [0:9]", "4. [range(10)]"], 1),
        ("What is the output of 'print(5 == 5.0)'?", ["1. False", "2. True", "3. Error", "4. None"], 2),
        ("What is the result of '3 < 4 and 5 > 2'?", ["1. True", "2. False", "3. Error", "4. None"], 1),
        ("What is the output of 'print(4 ** 0.5)'?", ["1. 2.0", "2. 16", "3. 4", "4. 0"], 1),
        ("What does 'is' compare in Python?", ["1. Value", "2. Identity", "3. Type", "4. Scope"], 2),
        ("Which of the following is NOT a valid data type in Python?", ["1. string", "2. list", "3. map", "4. float"], 3),
        ("What does the 'pass' statement do?", ["1. Skips iteration", "2. Terminates program", "3. Does nothing", "4. Raises an error"], 3),
        ("Which statement is used to stop a loop in Python?", ["1. stop", "2. break", "3. exit", "4. quit"], 2),
        ("Which of the following will create a set?", ["1. {1, 2, 3}", "2. [1, 2, 3]", "3. (1, 2, 3)", "4. <1, 2, 3>"], 1),
        ("What is the keyword to handle exceptions in Python?", ["1. try", "2. check", "3. catch", "4. handle"], 1),
        ("Which keyword is used to create a class in Python?", ["1. define", "2. function", "3. class", "4. def"], 3),
        ("What is the result of 'len(\"hello\")'?", ["1. 5", "2. 4", "3. 6", "4. Error"], 1),
        ("What does 'elif' stand for in Python?", ["1. Else if", "2. Else loop", "3. End if", "4. Else function"], 1),
        ("How do you write an infinite loop in Python?", ["1. while(True):", "2. for(;;)", "3. while 1", "4. repeat forever"], 1),
        ("Which of these is used to define a block of code in Python?", ["1. Curly braces", "2. Parentheses", "3. Indentation", "4. Semicolons"], 3),
        ("Which function gives the Unicode of a character?", ["1. unicode()", "2. char()", "3. ord()", "4. ascii()"], 3),
        ("What is the output of 'print(\"Hello\"[::-1])'?", ["1. Hello", "2. olleH", "3. Error", "4. hELLO"], 2)
    ]
    
    random.shuffle(questions)
    print("\n🎮 Welcome to the Python Quiz Game! 🎮")
    time.sleep(0.1)
    print("The quiz is starting...\n")
    time.sleep(0.1)
    while True:
        mode = input("Enter '1' for Single Player or '2' for Multiplayer: ").strip()
        if mode == "1":
            G2_single_player(questions)
            break
        elif mode == "2":
            G2_multiplayer(questions)
            break
        else:
            print("Invalid choice! Please enter '1' or '2'.")

################################################################

#Rock Paper and Scissors

def G3_get_move_input(player_name):
    time.sleep(0.1)
    move = input(f"{player_name}, enter move (Rock, Paper, Scissor): ").strip().lower()
    while move not in values:
        print("Invalid move! Please enter Rock, Paper, or Scissor.")
        move = input(f"{player_name}, enter move: ").strip().lower()
    return move

def G3_decide_winner(p1_move, p2_move):
    if p1_move == p2_move:
        return 0
    elif (p1_move, p2_move) in win_conditions:
        return 1
    else:
        return 2

def G3_display_score(name1, score1, name2=None, score2=None):
    if name2:
        print(f"{name1} has {score1} point(s), {name2} has {score2} point(s)\n")
    else:
        print(f"{name1}, you have {score1} point(s)\n")

def G3_play_single_player():
    time.sleep(0.2)
    player_name = input("Player 1, enter your name: ")
    time.sleep(0.1)
    rounds = int(input(f"{player_name}, how many rounds would you like to play? "))
    time.sleep(0.1)
    print(f"{player_name}, Get ready!\n")
    time.sleep(0.05)

    score = 0
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num} of {rounds}")
        time.sleep(0.2)
        player_move = G3_get_move_input(player_name)
        computer_move = random.choice(values)
        time.sleep(0.1)
        print(f"Computer chose: {computer_move}")

        result = G3_decide_winner(player_move, computer_move)
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{player_name}, you won this round!")
            score += 1
        else:
            print(f"{player_name}, you lost this round.")

        G3_display_score(player_name, score)

def G3_play_multiplayer():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    rounds = int(input("How many rounds would you like to play? "))
    print(f"{player1} and {player2}, Get ready!\n")

    score1 = 0
    score2 = 0

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num} of {rounds}")
        move1 = G3_get_move_input(player1)
        move2 = G3_get_move_input(player2)

        result = G3_decide_winner(move1, move2)
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{player1} won this round!")
            score1 += 1
        else:
            print(f"{player2} won this round!")
            score2 += 1

        G3_display_score(player1, score1, player2, score2)

values = ["rock", "paper", "scissor"]
win_conditions = {
    ("rock", "scissor"),
    ("scissor", "paper"),
    ("paper", "rock")
}

def G3_replay():
    response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    return response == 'y'

def G3_main():
    print("""
        🎮 Game - Rock Paper Scissors 🎮
        Choose Mode:
        1 : Single Player
        2 : Multiplayer
        """)
    while True:
        try:
            mode = int(input("Enter the mode number: "))
            if mode == 1:
                G3_play_single_player()
            elif mode == 2:
                G3_play_multiplayer()
            else:
                print("Invalid mode selected. Please enter 1 or 2.")
                continue
        except ValueError:
            print("!Error! Please enter a number, not letters.")
            continue

        if not G3_replay():
            print("\n👋 Thanks for playing! Goodbye!")
            time.sleep(0.4)
            break

################################################################

#tic tac toe

def G4_print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n    1   2   3")
    for i, row in enumerate(board):
        prefix = f"{i+1} "
        if i == 0:
            prefix += "◤ "
        elif i == 2:
            prefix += "◣ "
        else:
            prefix += "  "

        print(f"{prefix}" + " | ".join(row) + (" ◥" if i == 0 else " ◢" if i == 2 else " "))
        if i < 2:
            print("  |———————————|")
    print()

def G4_check_winner(board, player):
    win_patterns = (
        board,
        [[board[r][c] for r in range(3)] for c in range(3)],
        [[board[i][i] for i in range(3)]],
        [[board[i][2 - i] for i in range(3)]]
    )
    return any(all(cell == player for cell in line) for group in win_patterns for line in group)

def G4_get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def G4_ai_move(board, ai="Θ", player="✕"):
    def can_win(symbol):
        for r, c in G4_get_empty_cells(board):
            board[r][c] = symbol
            if G4_check_winner(board, symbol):
                board[r][c] = " "
                return r, c
            board[r][c] = " "
        return None

    return (
        can_win(ai) or
        can_win(player) or
        (1, 1) if board[1][1] == " " else
        random.choice([c for c in [(0, 0), (0, 2), (2, 0), (2, 2)] if board[c[0]][c[1]] == " "]) or
        random.choice(G4_get_empty_cells(board))
    )

def G4_get_player_move(board, player_symbol, player_num):
    while True:
        move = input(f"Player {player_num} ({player_symbol}), enter row and column (1-3, space-separated): ")
        try:
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            if (0 <= row < 3) and (0 <= col < 3) and board[row][col] == " ":
                return row, col
            print("Invalid move. Cell is occupied or out of range.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 1 and 3.")

def G4_main():
    print("\n🎮 Welcome to Tic Tac Toe! 🎮")
    mode = int(input("""
        Choose mode: 
        1 for Single Player 
        2 for Multiplayer
        : """).strip())

    scores = {"Player 1": 0, "Player 2": 0}
    players = ["✕", "Θ"]

    while True:
        board = [[" "]*3 for _ in range(3)]
        turn = 0

        while True:
            G4_print_board(board)
            current_player = players[turn % 2]

            if mode == 1 and current_player == "Θ":
                time.sleep(0.3)
                print("AI is making a move...")
                time.sleep(0.5)
                row, col = G4_ai_move(board)
            else:
                row, col = G4_get_player_move(board, current_player, turn % 2 + 1)

            board[row][col] = current_player

            if G4_check_winner(board, current_player):
                G4_print_board(board)
                print(f"Player {turn % 2 + 1} ({current_player}) wins!")
                if mode == 2:
                    scores[f"Player {turn % 2 + 1}"] += 3
                break

            if not G4_get_empty_cells(board):
                G4_print_board(board)
                print("It's a draw!")
                break

            turn += 1

        if mode == 2:
            print("\nScoreboard:")
            for player, score in scores.items():
                print(f"{player}: {score}")
            print()

        if input("Wanna play again? (yes/no): ").strip().lower() != "yes":
            print("Thanks for playing!")
            time.sleep(0.4)
            break


################################################################

# 2048

# Game constants
SIZE = 4
MOVES = {'W': 'up', 'A': 'left', 'S': 'down', 'D': 'right'}

class Game2048:
    def __init__(self):
        self.board = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.add_new_tile()
        self.add_new_tile()
    
    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.8 else 4
    
    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (SIZE - len(new_row))
        return new_row
    
    def merge(self, row):
        new_row = row.copy()
        for i in range(SIZE - 1):
            if new_row[i] == new_row[i + 1] and new_row[i] != 0:
                new_row[i] *= 2
                self.score += new_row[i]  
                new_row[i + 1] = 0
        return new_row
    
    def move_left(self):
        new_board = []
        moved = False
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)
            new_board.append(new_row)
            if row != new_row:
                moved = True
        self.board = new_board
        return moved
    
    def move_right(self):
        self.board = [row[::-1] for row in self.board]
        moved = self.move_left()
        self.board = [row[::-1] for row in self.board]
        return moved
    
    def move_up(self):
        self.board = [list(col) for col in zip(*self.board)]
        moved = self.move_left()
        self.board = [list(col) for col in zip(*self.board)]
        return moved
    
    def move_down(self):
        self.board = [list(col) for col in zip(*self.board)]
        moved = self.move_right()
        self.board = [list(col) for col in zip(*self.board)]
        return moved
    
    def check_game_over(self):
        if any(0 in row for row in self.board):
            return False
        
        for r in range(SIZE):
            for c in range(SIZE - 1):
                if self.board[r][c] == self.board[r][c + 1]:
                    return False
        
        for r in range(SIZE - 1):
            for c in range(SIZE):
                if self.board[r][c] == self.board[r + 1][c]:
                    return False
        
        return True
    
    def make_move(self, direction):
        if self.game_over:
            return False
        
        moved = False
        if direction == 'up':
            moved = self.move_up()
        elif direction == 'down':
            moved = self.move_down()
        elif direction == 'left':
            moved = self.move_left()
        elif direction == 'right':
            moved = self.move_right()
        
        # if moved:
        self.add_new_tile()
        self.high_score = max(self.score, self.high_score)
        if self.check_game_over():
            self.game_over = True
        
        return moved
    
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score} | High Score: {self.high_score}")
        print("=" * (SIZE * 6))
        
        for row in self.board:
            print(" | ".join(f"{num:^4}" if num != 0 else "    " for num in row))
            print("-" * (SIZE * 6))
        
        if self.game_over:
            print("\nGAME OVER! No more moves left.")

def G5_main():
    game = Game2048()
    
    while True:
        game.display()
        
        move = input("Move (WASD, Q to quit): ").strip().upper()
        
        if move == 'Q':
            print("Thanks for playing!")
            time.sleep(0.4)
            break
        
        if move in MOVES:
            game.make_move(MOVES[move])
        else:
            print("Invalid move! Use W (up), A (left), S (down), D (right) or Q to quit.")
            input("Press Enter to continue...")


################################################################

#4 in a row

def G6_create_board():
    return np.zeros((6, 7), dtype=int)

def G6_print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" \n  > 1   2   3   4   5   6   7 <")
    print("  |———————————————————————————|")
    arr = np.flip(board, 0)
    for i, row in enumerate(arr):
        row_str = "| " + " | ".join(map(str, row)) + " |"
        time.sleep(0.025)
        print(f"{i+1} {row_str}")

def G6_is_valid_move(board, col):
    return board[5][col] == 0

def G6_get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def G6_drop_piece(board, row, col, piece):
    board[row][col] = piece

def G6_check_win(board, piece):
    for c in range(4):
        for r in range(6):
            if all(board[r, c + i] == piece for i in range(4)):
                return True
    for c in range(7):
        for r in range(3):
            if all(board[r + i, c] == piece for i in range(4)):
                return True
    for c in range(4):
        for r in range(3):
            if all(board[r + i, c + i] == piece for i in range(4)):
                return True
    for c in range(4):
        for r in range(3, 6):
            if all(board[r - i, c + i] == piece for i in range(4)):
                return True
    return False

def G6_ai_move(board):
    valid_moves = [c for c in range(7) if G6_is_valid_move(board, c)]
    
    def can_win(piece):
        for c in valid_moves:
            row = G6_get_next_open_row(board, c)
            if row is not None:
                G6_drop_piece(board, row, c, piece)
                if G6_check_win(board, piece):
                    board[row][c] = 0
                    return c
                board[row][c] = 0
        return None
    
    ai_piece = 2
    player_piece = 1
    move = can_win(ai_piece)
    if move is not None:
        return move
    
    move = can_win(player_piece)
    if move is not None:
        return move
    
    return random.choice(valid_moves)

def G6_get_valid_column():
    while True:
        try:
            time.sleep(0.25)
            cx = int(input("\nPlayer 1, choose a column (1-7): "))
            if cx == -1:
                print("\nThank you for playing\n")
                time.sleep(0.4)
                exit()
            if 1 <= cx <= 7:
                return cx - 1
            else:
                print("Invalid column! Please choose a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def G6_is_board_full(board):
    return np.all(board != 0)

def G6_main():
    time.sleep(0.1)
    print("\nWelcome to 4 in a Row!")
    time.sleep(0.1)
    mode = input("Enter '1' for single-player or '2' for multiplayer: ")
    board = G6_create_board()
    game_over = False
    turn = 0
    scores = {1: 0, 2: 0} if mode == '2' else None
    
    while not game_over:
        G6_print_board(board)
        if turn % 2 == 0:
            col = G6_get_valid_column()
        else:
            if mode == '1':
                col = G6_ai_move(board)
                print("\n")
                time.sleep(0.6)
                print(f"AI is making a move...")
                time.sleep(1.1)
            else:
                col = G6_get_valid_column()
        
        if G6_is_valid_move(board, col):
            row = G6_get_next_open_row(board, col)
            G6_drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
            if G6_check_win(board, 1 if turn % 2 == 0 else 2):
                time.sleep(0.1)
                G6_print_board(board)
                print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
                if mode == '2':
                    scores[1 if turn % 2 == 0 else 2] += 1
                game_over = True
                
        else:
            print("\nInvalid move! Try again.")
            continue
        
        turn += 1
        if G6_is_board_full(board):
            print("\nIt's a tie!")
            game_over = True
        
        if game_over and mode == '1':
            replay = input("\nPlay again? (yes/no): ")
            if replay.lower() == 'yes':
                board = G6_create_board()
                game_over = False
                turn = 0

        if game_over and mode == '2':
            print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
            replay = input("\nPlay again? (yes/no): ")
            if replay.lower() == 'yes':
                board = G6_create_board()
                scores = {1: 0, 2: 0}  
                game_over = False
                turn = 0

################################################################

# sudoku

def G7_print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")
        print()

def G7_find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def G7_is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and col != i:
            return False
        if board[i][col] == num and row != i:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def G7_generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[box + i][box + j] = nums.pop()
    G7_solve_board(board)
    cells_to_remove = min(max(difficulty, 30), 60)
    for _ in range(cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def G7_solve_board(board):
    find = G7_find_empty(board)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if G7_is_valid(board, num, (row, col)):
            board[row][col] = num
            if G7_solve_board(board):
                return True
            board[row][col] = 0
    return False

def G7_input_board():
    print("\nEnter your Sudoku board row by row.")
    print("Use numbers 1-9 for filled cells and 0 or . for empty cells.")
    print("Separate numbers with spaces.")
    board = []
    for i in range(9):
        while True:
            row_input = input(f"Row {i+1}: ").replace('.', '0')
            parts = row_input.split()
            if len(parts) != 9:
                print("Please enter exactly 9 values.")
                continue
            try:
                row = [int(x) if x.isdigit() else -1 for x in parts]
                if any(num < 0 or num > 9 for num in row):
                    print("Numbers must be between 0 and 9.")
                    continue
                board.append(row)
                break
            except Exception:
                print("Invalid input. Please enter numbers only.")
    return board

def G7_get_fixed_cells(board):
    return {(i, j) for i in range(9) for j in range(9) if board[i][j] != 0}

def G7_play_move(board, fixed_cells):
    while True:
        move = input("Enter your move (row col num), 'hint' or 'q' to quit: ").lower()
        if move == 'q':
            return False
        if move == 'hint':
            G7_give_hint(board)
            continue
        parts = move.split()
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            print("Please enter row, column, and number as integers separated by spaces.")
            continue
        row, col, num = map(int, parts)
        if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
            print("Row, column, and number must be between 1-9.")
            continue
        row -= 1
        col -= 1
        if (row, col) in fixed_cells:
            print("You can't change the original puzzle numbers!")
            continue
        if board[row][col] != 0:
            print("That cell is already filled!")
            continue
        if G7_is_valid(board, num, (row, col)):
            board[row][col] = num
            return True
        else:
            print("Invalid move! That number conflicts with existing numbers.")

def G7_give_hint(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if G7_is_valid(board, num, (i, j)):
                        print(f"Try placing in row {i+1}, column {j+1} : {num} ")
                        return
    print("No hints available.")

def G7_check_complete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
            temp = board[i][j]
            board[i][j] = 0
            if not G7_is_valid(board, temp, (i, j)):
                board[i][j] = temp
                return False
            board[i][j] = temp
    return True

def G7_main():
    print("Welcome to Sudoku!")
    print("Enter moves as 'row col number' (e.g., '3 5 7' to put 7 in row 3, column 5)")
    print("Enter 'hint' for a hint or 'q' to quit at any time\n")

    while True:
        choice = input("Choose an option:\n1. Play a random puzzle\n2. Input your own puzzle\n> ").strip()
        if choice == '1':
            difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
            difficulties = {'easy': (30, 40), 'medium': (41, 49), 'hard': (50, 60)}
            empty_range = difficulties.get(difficulty, (41, 49))
            empty_cells = random.randint(*empty_range)
            board = G7_generate_sudoku(empty_cells)
            break
        elif choice == '2':
            board = G7_input_board()
            solve = input("Would you like to auto-solve your puzzle? (y/n): ").lower()
            if solve == 'y':
                if G7_solve_board(board):
                    print("\nSolved board:")
                    G7_print_board(board)
                else:
                    print("This puzzle has no valid solution.")
                return
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    fixed_cells = G7_get_fixed_cells(board)
    start_time = time.time()

    while True:
        print("\nCurrent board:")
        G7_print_board(board)

        if G7_check_complete(board):
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            print(f"\nCongratulations! You solved the Sudoku in {mins} minutes and {secs} seconds.")
            break

        if not G7_play_move(board, fixed_cells):
            print("\nThanks for playing!")
            time.sleep(0.4)
            break

    print("\nFinal board:")
    G7_print_board(board)


################################################################

#Python syntax checker

task_bank = [
    ("Create a list and append three numbers to it.",
     lambda lv: isinstance(lv.get('my_list'), list) and len(lv['my_list']) >= 3),

    ("Create a tuple and access an element from it.",
     lambda lv: isinstance(lv.get('my_tuple'), tuple)),

    ("Create a dictionary and retrieve a value using a key.",
     lambda lv: isinstance(lv.get('my_dict'), dict) and bool(lv['my_dict'])),

    ("Import the math module and use the sqrt function.",
     lambda lv: 'math' in lv and callable(lv['math'].sqrt)),

    ("Create a set and add/remove elements.",
     lambda lv: isinstance(lv.get('my_set'), set)),

    ("Define a function that returns the square of a number.",
     lambda lv: callable(lv.get('square')) and lv  == 4),

    ("Create a list of strings and loop through it.",
     lambda lv: isinstance(lv.get('str_list'), list) and all(isinstance(x, str) for x in lv['str_list'])),

    ("Use a tuple to store coordinates and print them.",
     lambda lv: isinstance(lv.get('coords'), tuple) and len(lv['coords']) == 2),

    ("Create a dictionary of student names and grades using a for loop.",
     lambda lv: isinstance(lv.get('grades'), dict)),

    ("Use a set to store unique numbers and display them.",
     lambda lv: isinstance(lv.get('unique_numbers'), set)),

    ("Import the random module and generate a random number.",
     lambda lv: 'random' in lv),

    ("Define a function to check if a number is even.",
     lambda lv: callable(lv.get('is_even')) and lv  is True),

    ("Create a nested list and access an inner element.",
     lambda lv: isinstance(lv.get('nested_list'), list)),

    ("Create a dictionary of fruits and their prices, then print the most expensive fruit.",
     lambda lv: isinstance(lv.get('fruits'), dict)),

    ("Create a list and use pop() to remove an element.",
     lambda lv: isinstance(lv.get('popped_list'), list)),

    ("Define a function to return the length of a string.",
     lambda lv: callable(lv.get('strlen')) and lv['strlen']("abc") == 3),

    ("Make a dictionary and iterate through its keys.",
     lambda lv: isinstance(lv.get('my_dict'), dict)),

    ("Use a tuple to store and print 3 values.",
     lambda lv: isinstance(lv.get('vals'), tuple) and len(lv['vals']) == 3),

    ("Create a set and check for membership.",
     lambda lv: isinstance(lv.get('my_set'), set)),

    ("Check if a substring exists in a string using 'in'.",
     lambda lv: isinstance(lv.get('text'), str) and 'a' in lv['text']),

    ("Replace characters in a string using replace().",
     lambda lv: isinstance(lv.get('text'), str) and 'x' not in lv['text']),

    ("Use regex to find digits in a string.",
     lambda lv: 're' in lv and lv.get('digits') is not None and isinstance(lv['digits'], list)),
]

def G8_check_line_syntax(code_line):
    try:
        compile(code_line, "<line>", "exec")
        return True
    except SyntaxError:
        return False

def G8_main():
    print("🎮 Welcome to Python Syntax Battle!")
    start_game = input("Do you want to play? Enter y to start: ").strip().lower()
    if start_game != 'y':
        print("👋 Exiting game. Maybe next time!")
        return

    players = ["Player 1", "Player 2"]
    points = {player: 0 for player in players}
    turn = 0

    while True:
        task_description, validator = random.choice(task_bank)
        print(f"\n📝 Task: {task_description}")

        code_lines = []
        sub_turn = 0

        while True:
            active_player = players[(turn + sub_turn) % 2]
            print(f"\n✏ {active_player}'s turn to enter a line of code:")
            code_line = input(">>> ").rstrip()

            if G8_check_line_syntax(code_line):
                print("✅ Line is syntactically correct.")
                code_lines.append(code_line)
                points[active_player] += 1
            else:
                print("❌ Syntax error! Opportunity passes to the other player.")
                other_player = players[(turn + sub_turn + 1) % 2]
                print(f"✏ {other_player}, your chance to correct the line:")
                code_line_alt = input(">>> ").rstrip()
                if G8_check_line_syntax(code_line_alt):
                    print("✅ Corrected line accepted.")
                    code_lines.append(code_line_alt)
                    points[other_player] += 1
                else:
                    print("❌ Still a syntax error! No line added.")

            compile_now = input("⚙ Compile full code and validate task? (y/n): ").lower()
            if compile_now == 'y':
                full_code = "\n".join(code_lines)
                try:
                    compiled_code = compile(full_code, "<game>", "exec")
                    local_vars = {}
                    exec(compiled_code, {"re": re, "random": random}, local_vars)
                    if validator(local_vars):
                        print("✅ Task completed successfully! Moving to next round.")
                    else:
                        print("❌ Code ran, but task not completed correctly.")
                        print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
                    break
                except Exception:
                    print("❌ Compilation or Runtime error!")
                    print(traceback.format_exc())
                    print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
                    break
            sub_turn += 1

        print("\n📊 Current Points:")
        for player, score in points.items():
            print(f"   {player}: {score} points")

        play_again = input("\n🔁 Continue to next round? (y/n): ").lower()
        if play_again != 'y':
            print("\n🎉 Final Scores:")
            for player, score in points.items():
                print(f"   {player}: {score} points")
            print("👋 Thanks for playing!")
            break

        turn += 1

################################################################

def loading_bar():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting...  "):        # NEW
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
            G1_main()
        elif choice == '2':
            loading_bar()
            G2_main()
        elif choice == '3':
            loading_bar()
            G3_main()
        elif choice == '4':
            loading_bar()
            G4_main()
        elif choice == '5':
            loading_bar()
            G5_main()
        elif choice == '6':
            loading_bar()
            G6_main()
        elif choice == '7':
            loading_bar()
            G7_main()
        elif choice == '8':
            loading_bar()
            G8_main()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run()
