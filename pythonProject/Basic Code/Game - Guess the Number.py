import time
import random

print("""
Game - Guess the Number
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

if int(to_perform) == 1:
    Player_1 = input("Player 1 input your name: ")
    time.sleep(0.5)

    random_no = random.randint(1, 10)

    guess_limit = int(input(f"{Player_1} how many attempts would you like: "))
    guess_count = 0

    print(f"{Player_1}, get ready")
    print(f"{Player_1} you have {guess_limit} attempts.")
    print(f"{Player_1} choose a number ranging from 1 to 10")

    time.sleep(1.5)

    while guess_count < guess_limit:
        guess_no = float(input(f"{Player_1} enter a number: "))
        guess_count += 1
        if guess_no == random_no:
            time.sleep(1)
            print(f"{guess_no} was the right number, You won! {Player_1}")
            break
        elif guess_count < guess_limit - 1:
            time.sleep(1)
            print("Nope, try again")
        elif guess_count == guess_limit - 1:
            time.sleep(1)
            print("Nope, This is your last try")
        else:
            time.sleep(1)
            print(f"{random_no} was the correct answer, you failed {Player_1}")

elif int(to_perform) == 2:
    Player_1 = input("Player 1 input your name: ")
    time.sleep(1)
    Player_2 = input("Player 2 input your name: ")
    time.sleep(1)

    guess_value = float(input(f"{Player_1}, input a number: "))
    guess_limit = int(input(f"{Player_1}, input the number of chances for {Player_2}: "))
    guess_count = 0
    print(f"Give {Player_2} the Device")

    time.sleep(1.5)

    print(f"{Player_2}, get ready")
    print(f"{Player_2} you have {guess_limit} attempts.")

    time.sleep(1.5)

    while guess_count < guess_limit:
        guess_no = float(input(f"{Player_2} enter a number: "))
        guess_count += 1
        if guess_no == guess_value:
            time.sleep(1)
            print(f"{guess_no} was the right number, You won! {Player_2}")
            break
        elif guess_count < guess_limit - 1:
            time.sleep(1)
            print("Nope, try again")
        elif guess_count == guess_limit - 1:
            time.sleep(1)
            print("Nope, This is your last try")
        else:
            time.sleep(1)
            print(f"{guess_value} was the correct answer, you failed {Player_2}.")

else:
    print("Please enter the number of the function you want to perform.")
