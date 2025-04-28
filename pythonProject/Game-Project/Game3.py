#Rock Paper and Scissors

import random
import time

def get_move_input(player_name):
    time.sleep(0.1)
    move = input(f"{player_name}, enter move (Rock, Paper, Scissor): ").strip().lower()
    while move not in values:
        print("Invalid move! Please enter Rock, Paper, or Scissor.")
        move = input(f"{player_name}, enter move: ").strip().lower()
    return move

def decide_winner(p1_move, p2_move):
    if p1_move == p2_move:
        return 0
    elif (p1_move, p2_move) in win_conditions:
        return 1
    else:
        return 2

def display_score(name1, score1, name2=None, score2=None):
    if name2:
        print(f"{name1} has {score1} point(s), {name2} has {score2} point(s)\n")
    else:
        print(f"{name1}, you have {score1} point(s)\n")

def play_single_player():
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
        player_move = get_move_input(player_name)
        computer_move = random.choice(values)
        time.sleep(0.1)
        print(f"Computer chose: {computer_move}")

        result = decide_winner(player_move, computer_move)
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{player_name}, you won this round!")
            score += 1
        else:
            print(f"{player_name}, you lost this round.")

        display_score(player_name, score)

def play_multiplayer():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    rounds = int(input("How many rounds would you like to play? "))
    print(f"{player1} and {player2}, Get ready!\n")

    score1 = 0
    score2 = 0

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num} of {rounds}")
        move1 = get_move_input(player1)
        move2 = get_move_input(player2)

        result = decide_winner(move1, move2)
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print(f"{player1} won this round!")
            score1 += 1
        else:
            print(f"{player2} won this round!")
            score2 += 1

        display_score(player1, score1, player2, score2)

values = ["rock", "paper", "scissor"]
win_conditions = {
    ("rock", "scissor"),
    ("scissor", "paper"),
    ("paper", "rock")
}

def replay():
    response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    return response == 'y'

def main():
    print("""
        🎮 Game - Rock Paper Scissors 🎮
        Choose Mode:
        1 : Single Player
        2 : Multiplayer
        """)
    while True:
        # mode=0
        # while mode==0:
        try:
            mode = int(input("Enter the mode number: "))
            if mode == 1:
                play_single_player()
            elif mode == 2:
                play_multiplayer()
            else:
                print("Invalid mode selected. Please enter 1 or 2.")
                continue
        except ValueError:
            print("!Error! Please enter a number, not letters.")
            continue

        if not replay():
            print("\n👋 Thanks for playing! Goodbye!")
            time.sleep(0.4)
            break


if __name__ == "__main__":
    main()

###################################################
# # import time
# import random

# print("""
# Game  - Rock Paper and Scissors
# Single Player or Multi Player

# 1 : Single player
# 2 : Multi Player
# """)

# to_perform = 0

# try:
#     to_perform = int(input("Which game-mode would you like to play => "))
# except ValueError:
#     print("""!Error! -> Please input number and not letters.
#     """)

# print("""
# Refer to the Words given bellow-
# Rock
# Paper
# Scissor
# """)

# values = ("rock", "paper", "scissor")
# r = "rock"
# p = "paper"
# s = "scissor"
# total_play_cycle = 0
# played_cycle = 0
# p1_points = 0
# p2_points = 0

# if float(to_perform) == 1:

#     Player_1 = input("Player 1 input your name: ")
#     total_play_cycle = int(input(f"{Player_1}, enter the number of times you want to play: "))
#     print(f"{Player_1}, Get ready")

#     while played_cycle < total_play_cycle:
#         played_cycle += 1
#         random_move = random.choice(values)
#         move = input(f"{Player_1}, enter move: ")
#         move = move.lower()
#         if move == random_move:
#             print(f"{move} = {random_move}")
#             print(f"{Player_1}, it is a tie")
#             print(f"You have {p1_points} point")

#         elif move == r and random_move == p:
#             print(f"Rock < Paper")
#             print(f"{Player_1}, you lost this round")
#             print(f"You have {p1_points} point")

#         elif move == p and random_move == s:
#             print(f"Paper < Scissor")
#             print(f"{Player_1}, you lost this round")
#             print(f"You have {p1_points} point")

#         elif move == s and random_move == r:
#             print(f"Scissor < Rock")
#             print(f"{Player_1}, you lost this round")
#             print(f"You have {p1_points} point")

#         elif move == p and random_move == r:
#             p1_points += 1
#             print(f"Paper > Rock")
#             print(f"{Player_1}, you won this round")
#             print(f"You have {p1_points} point")

#         elif move == s and random_move == p:
#             p1_points += 1
#             print(f"Scissor > Ppaer")
#             print(f"{Player_1}, you won this round")
#             print(f"You have {p1_points} point")

#         elif move == r and random_move == s:
#             p1_points += 1
#             print(f"Rock > Scissor")
#             print(f"{Player_1}, you won this round")
#             print(f"You have {p1_points} point")

#         else:
#             print("Please enter Rock, Paper or Scissor")
#             played_cycle -= 1
        
#         if played_cycle == total_play_cycle - 1:
#             print(f"{Player_1} this is the last round")

#         else:
#             None

# elif float(to_perform) == 2:
#     Player_1 = input("Player 1 input your name: ")
#     Player_2 = input("Player 2 input your name: ")
#     total_play_cycle = int(input("Enter the number of times you want to play: "))
#     print(f"{Player_1} and {Player_2}, Get ready")

#     while played_cycle < total_play_cycle:
#         played_cycle += 1

#         random_move = random.choice(values)

#         p1_move = input(f"{Player_1}, enter move: ")
#         p1_move = p1_move.lower()
#         p2_move = input(f"{Player_2}, enter move: ")
#         p2_move = p2_move.lower()

#         if p1_move == p2_move:
#             print(f"{p1_move} = {p2_move}")
#             print(f"It is a tie")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == r and p2_move == p:
#             p2_points += 1
#             print(f"Rock < Paper")
#             print(f"{Player_2}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == p and p2_move == s:
#             p2_points += 1
#             print(f"Paper < Scissor")
#             print(f"{Player_2}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == s and p2_move == r:
#             p2_points += 1
#             print(f"Scissor < Rock")
#             print(f"{Player_2}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == p and p2_move == r:
#             p1_points += 1
#             print(f"Paper > Rock")
#             print(f"{Player_1}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == s and p2_move == p:
#             p1_points += 1
#             print(f"Scissor > Ppaer")
#             print(f"{Player_1}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         elif p1_move == r and p2_move == s:
#             p1_points += 1
#             print(f"Rock > Scissor")
#             print(f"{Player_1}, you won this round")
#             print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

#         else:
#             print("Please enter Rock, Paper or Scissor")
#             played_cycle -= 1
        
#         if played_cycle == total_play_cycle - 1:
#             print(f"This is the last round")

#         else:
#             None

# else:
#     print("Please enter the number of the function you want to perform.")
