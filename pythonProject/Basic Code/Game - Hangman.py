print("""
Game - Hangman
""")

Player_1 = input("Player 1 input your name: ")
Player_2 = input("Player 2 input your name: ")

word = input(f"{Player_1} enter you word: ")
word = word.lower()
total_attempts = int(input(f"{Player_1} how many attempts do you want to give to {Player_2}: "))
attempts = 0

while attempts < total_attempts:
    print(f"{Player_1} give {Player_2} a hint.")
    left_attempts = total_attempts - attempts
    print(f"{Player_2} you have {left_attempts} attempt left")
    guessed_word = input(f"{Player_2} enter your guess word: ")
    guessed_word = guessed_word.lower()

    if word == guessed_word:
        print(f"{word} is the correct answer")
        break
    elif attempts + 1 == total_attempts:
        print(f"Nope")
    else:
        print(f"Nope, try again")

    attempts += 1

if attempts == total_attempts:
    print(f"{word} was the correct answer, You Lost {Player_2}")
else:
    print(f"You won {Player_2}")
