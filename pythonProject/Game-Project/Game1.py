#guess the number

import time
import random

def show_menu():
    print("""
🎮 Game - Guess the Number 🎮
Choose Game Mode:

1 : Single Player
2 : Multi Player
""")

def get_hint(guess, correct_number):
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

def input_number(prompt, min_val=None, max_val=None):
    while True:
        try:
            num = int(input(prompt))
            if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
                print(f"❌ Enter a number between {min_val} and {max_val}.")
                continue
            return num
        except ValueError:
            print("❌ Error! Please input a valid number.")

def play_guessing_game(secret_number, attempts, player_name):
    guess_count = 0
    while guess_count < attempts:
        guess = input_number(f"🔢 {player_name}, enter your guess: ", 1, 100)
        guess_count += 1

        if guess == secret_number:
            print(f"🎉 {guess} was the right number! You WON, {player_name}!")
            return

        hint = get_hint(guess, secret_number)
        attempts_left = attempts - guess_count

        if attempts_left > 1:
            print(f"❌ Nope! {hint} Try again! 📉 Attempts left: {attempts_left}")
        elif attempts_left == 1:
            print(f"⚠ Last chance! {hint}")
        else:
            print(f"💀 The correct number was {secret_number}. Better luck next time, {player_name}!")

def single_player():
    time.sleep(0.35)
    player = input("🎩 Player 1, enter your name: ").strip().title()
    time.sleep(0.5)

    secret_number = random.randint(1, 100)
    guess_limit = input_number(f"{player}, how many attempts would you like? 🎯 ", 1, 100)

    print(f"\n🚀 {player}, get ready!")
    time.sleep(0.25)
    print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")
    time.sleep(1)

    play_guessing_game(secret_number, guess_limit, player)

def multiplayer():
    player1 = input("👑 Player 1, enter your name: ").strip().title()
    time.sleep(0.5)
    player2 = input("🦸‍♂ Player 2, enter your name: ").strip().title()
    time.sleep(0.5)

    print(f"\n🔐 {player1}, enter a secret number while {player2} looks away!")
    secret_number = input_number(f"{player1}, enter a number between 1 and 100: ", 1, 100)
    guess_limit = input_number(f"🎯 How many attempts does {player2} get? ", 1, 100)

    print(f"\n📱 Now, pass the device to {player2}!")
    time.sleep(1.5)

    print(f"\n⚔ {player2}, your mission: Guess the secret number!")
    time.sleep(0.25)
    print(f"🎲 You have {guess_limit} attempts!")
    time.sleep(1)

    play_guessing_game(secret_number, guess_limit, player2)

def replay():
    response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    return response == 'y'

def main():
    show_menu()
    while True:

        try:
            choice = int(input("👉 Choose mode (1 or 2): "))
        except ValueError:
            print("❌ Invalid input. Please enter 1 or 2.")
            continue

        if choice == 1:
            single_player()
        elif choice == 2:
            multiplayer()
        else:
            print("❌ Please enter a valid game mode (1 or 2).")
            continue

        if not replay():
            print("\n👋 Thanks for playing! Goodbye!")
            time.sleep(0.4)
            break

if __name__ == "__main__":
    main()


##############################################
# import time
# import random

# print("""
# 🎮 Game - Guess the Number 🎮
# Single Player or Multi Player

# 1 : Single player
# 2 : Multi Player
# """)

# to_perform = 0

# try:
#     to_perform = int(input("Which game mode would you like to play? 👉 "))
# except ValueError:
#     print("❌ Error! Please input a number, not letters.")
#     exit()

# # Fun Hint Generator
# def get_hint(guess, correct_number):
#     difference = abs(guess - correct_number)
    
#     if difference >= 50:
#         return "💀 Whoa! You missed by a mile! Try a completely different number!"
#     elif difference >= 30:
#         return "🤦‍♂ Oof! You're still quite far, but moving in the right direction."
#     elif difference >= 20:
#         return "🚀 You're getting warmer, but still not quite there!"
#     elif difference >= 10:
#         return "🔥 Hot! You're closing in on the target!"
#     elif difference >= 5:
#         return "⚡ Super close! The number is just around the corner!"
#     else:
#         return "💥 SO CLOSE! Almost there, just tweak your guess a little!"

# if to_perform == 1:
#     # 🎯 Single Player Mode
#     Player_1 = input("🎩 Player 1, enter your name: ")
#     time.sleep(0.5)

#     random_no = random.randint(1, 100)

#     try:
#         guess_limit = int(input(f"{Player_1}, how many attempts would you like? 🎯 "))
#     except ValueError:
#         print("❌ Error! Please enter a valid number.")
#         exit()

#     print(f"\n🚀 {Player_1}, get ready!")
#     print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")

#     time.sleep(1.5)

#     guess_count = 0
#     while guess_count < guess_limit:
#         try:
#             guess_no = int(input(f"🔢 {Player_1}, enter a number: "))
#         except ValueError:
#             print("❌ Invalid input! Enter a number, not letters.")
#             continue

#         guess_count += 1

#         if guess_no == random_no:
#             time.sleep(1)
#             print(f"🎉 {guess_no} was the right number! You WON, {Player_1}!")
#             break
#         else:
#             hint = get_hint(guess_no, random_no)

#         if guess_count < guess_limit - 1:
#             time.sleep(1)
#             print(f"❌ Nope! {hint} Try again!")
#         elif guess_count == guess_limit - 1:
#             time.sleep(1)
#             print(f"⚠ Last chance! {hint}")
#         else:
#             time.sleep(1)
#             print(f"💀 The correct number was {random_no}. Better luck next time, {Player_1}!")

# elif to_perform == 2:
#     # 🤝 Multiplayer Mode
#     Player_1 = input("👑 Player 1, enter your name: ")
#     time.sleep(1)
#     Player_2 = input("🦸‍♂ Player 2, enter your name: ")
#     time.sleep(1)

#     try:
#         guess_value = int(input(f"🔐 {Player_1}, enter a secret number between 1 and 100: "))
#         while guess_value < 1 or guess_value > 100:
#             print("❌ Invalid number! Choose a number between 1 and 100.")
#             guess_value = int(input(f"🔐 {Player_1}, enter a number: "))

#         guess_limit = int(input(f"🎯 {Player_1}, how many chances does {Player_2} get? "))
#     except ValueError:
#         print("❌ Error! Please enter valid numbers only.")
#         exit()

#     guess_count = 0
#     print(f"\n📱 Now, pass the device to {Player_2}!")
#     time.sleep(1.5)

#     print(f"\n⚔ {Player_2}, your mission: Guess the secret number!")
#     print(f"🎲 You have {guess_limit} attempts!")

#     time.sleep(1.5)

#     while guess_count < guess_limit:
#         try:
#             guess_no = int(input(f"🔢 {Player_2}, enter a number: "))
#         except ValueError:
#             print("❌ Invalid input! Enter a number, not letters.")
#             continue

#         guess_count += 1

#         if guess_no == guess_value:
#             time.sleep(1)
#             print(f"🎉 {guess_no} was the correct number! You WON, {Player_2}!")
#             break
#         else:
#             hint = get_hint(guess_no, guess_value)

#         if guess_count < guess_limit - 1:
#             time.sleep(1)
#             print(f"❌ Nope! {hint} Try again!")
#         elif guess_count == guess_limit - 1:
#             time.sleep(1)
#             print(f"⚠ Last chance! {hint}")
#         else:
#             time.sleep(1)
#             print(f"💀 The correct number was {guess_value}. Better luck next time, {Player_2}!")

# else:
#     print("❌ Please enter a valid game mode (1 or 2).")