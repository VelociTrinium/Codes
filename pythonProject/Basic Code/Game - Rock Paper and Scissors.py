#Rock Paper and Scissors

import time
import random

print("""
Game  - Rock Paper and Scissors
Single Player or Multi Player

1 : Single player
2 : Multi Player
""")

to_perform = 0

try:
    to_perform = int(input("Which game-mode would you like to play => "))
except ValueError:
    print("""!Error! -> Please input number and not letters.
    """)

print("""
Refer to the Words given bellow-
Rock
Paper
Scissor
""")

values = ("rock", "paper", "scissor")
r = "rock"
p = "paper"
s = "scissor"
total_play_cycle = 0
played_cycle = 0
p1_points = 0
p2_points = 0

if float(to_perform) == 1:

    Player_1 = input("Player 1 input your name: ")
    total_play_cycle = int(input(f"{Player_1}, enter the number of times you want to play: "))
    print(f"{Player_1}, Get ready")

    while played_cycle < total_play_cycle:
        played_cycle += 1
        random_move = random.choice(values)
        move = input(f"{Player_1}, enter move: ")
        move = move.lower()
        if move == random_move:
            print(f"{move} = {random_move}")
            print(f"{Player_1}, it is a tie")
            print(f"You have {p1_points} point")

        elif move == r and random_move == p:
            print(f"Rock < Paper")
            print(f"{Player_1}, you lost this round")
            print(f"You have {p1_points} point")

        elif move == p and random_move == s:
            print(f"Paper < Scissor")
            print(f"{Player_1}, you lost this round")
            print(f"You have {p1_points} point")

        elif move == s and random_move == r:
            print(f"Scissor < Rock")
            print(f"{Player_1}, you lost this round")
            print(f"You have {p1_points} point")

        elif move == p and random_move == r:
            p1_points += 1
            print(f"Paper > Rock")
            print(f"{Player_1}, you won this round")
            print(f"You have {p1_points} point")

        elif move == s and random_move == p:
            p1_points += 1
            print(f"Scissor > Ppaer")
            print(f"{Player_1}, you won this round")
            print(f"You have {p1_points} point")

        elif move == r and random_move == s:
            p1_points += 1
            print(f"Rock > Scissor")
            print(f"{Player_1}, you won this round")
            print(f"You have {p1_points} point")

        else:
            print("Please enter Rock, Paper or Scissor")
            played_cycle -= 1
        
        if played_cycle == total_play_cycle - 1:
            print(f"{Player_1} this is the last round")

        else:
            None

elif float(to_perform) == 2:
    Player_1 = input("Player 1 input your name: ")
    Player_2 = input("Player 2 input your name: ")
    total_play_cycle = int(input("Enter the number of times you want to play: "))
    print(f"{Player_1} and {Player_2}, Get ready")

    while played_cycle < total_play_cycle:
        played_cycle += 1

        random_move = random.choice(values)

        p1_move = input(f"{Player_1}, enter move: ")
        p1_move = p1_move.lower()
        p2_move = input(f"{Player_2}, enter move: ")
        p2_move = p2_move.lower()

        if p1_move == p2_move:
            print(f"{p1_move} = {p2_move}")
            print(f"It is a tie")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == r and p2_move == p:
            p2_points += 1
            print(f"Rock < Paper")
            print(f"{Player_2}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == p and p2_move == s:
            p2_points += 1
            print(f"Paper < Scissor")
            print(f"{Player_2}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == s and p2_move == r:
            p2_points += 1
            print(f"Scissor < Rock")
            print(f"{Player_2}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == p and p2_move == r:
            p1_points += 1
            print(f"Paper > Rock")
            print(f"{Player_1}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == s and p2_move == p:
            p1_points += 1
            print(f"Scissor > Ppaer")
            print(f"{Player_1}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        elif p1_move == r and p2_move == s:
            p1_points += 1
            print(f"Rock > Scissor")
            print(f"{Player_1}, you won this round")
            print(f"{Player_1} has {p1_points} point, {Player_2} has {p2_points} point")

        else:
            print("Please enter Rock, Paper or Scissor")
            played_cycle -= 1
        
        if played_cycle == total_play_cycle - 1:
            print(f"This is the last round")

        else:
            None

else:
    print("Please enter the number of the function you want to perform.")
