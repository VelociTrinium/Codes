#syntax hangman 

import random
import time
# from tqdm import tqdm       # NEW

hang = [
    "------  ",
    "|    |  ",
    "|    0  ",
    "|   /|\\",
    "|   / \\",
    "|       "
]

def print_hang(x):
    for i in range(x):
        print(hang[i])
        time.sleep(0.075)

def ask_question(question, options, correct_option):
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

def print_score(player_name, score, total):
    print(f"\nGame Over! {player_name}, your final score: {score}/{total}")

def run_quiz(questions_subset, player_name):
    score = 0
    incorrect = 0
    for i, (question, options, correct_option) in enumerate(questions_subset):
        print(f"\nQuestion {i + 1}:")
        if ask_question(question, options, correct_option):
            score += 1
        else:
            incorrect += 1
            if incorrect < 6:
                print_hang(incorrect)
            else:
                break
    print_score(player_name, score, len(questions_subset))
    if incorrect >= 6:
        print_hang(6)
        print(f"{player_name} was Hanged")

def single_player(questions):
    player_name = input("Player 1, input your name: ")
    time.sleep(0.1)
    # print("\n")
    # for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):        # NEW
    #     time.sleep(0.03)
    run_quiz(questions[:10], player_name)
    play_again()

def multiplayer(questions):
    player1 = input("Player 1, input your name: ")
    player2 = input("Player 2, input your name: ")
    score1 = score2 = incorrect1 = incorrect2 = 0

    # for _ in tqdm(range(20), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
    #     time.sleep(0.025)

    for i in range(20):
        player = player1 if i % 2 == 0 else player2
        print(f"\n{player}, it's your turn!")
        question, options, correct_option = questions[i]
        if ask_question(question, options, correct_option):
            if player == player1:
                score1 += 1
            else:
                score2 += 1
        else:
            if player == player1:
                incorrect1 += 1
                print(f"{player1}'s Hangman:")
                print_hang(incorrect1)
                if incorrect1 >= 6:
                    print(f"{player1} was Hanged")
                    break
            else:
                incorrect2 += 1
                print(f"{player2}'s Hangman:")
                print_hang(incorrect2)
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
    play_again()

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            main()
            break
        elif choice == "no":
            print("Thanks for playing!")
            time.sleep(0.4)
            break
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")

def main():
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
            single_player(questions)
            break
        elif mode == "2":
            multiplayer(questions)
            break
        else:
            print("Invalid choice! Please enter '1' or '2'.")

if __name__ == "__main__":
    main()

###################################################
# from tqdm import tqdm
# import random
# import time

# hang = ["------  ",
#         "|    |  ",
#         "|    0  ",
#         "|   /|\\",
#         "|   / \\",
#         "|       "]

# def print_hang(x):
#     for i in range(x):
#         print(hang[i])
#         time.sleep(0.075)

# questions = [
#     ("What will be the output of 'print(3 * 3 ** 2)'?", 
#      ["1. 27", "2. 18", "3. 81", "4. 9"], 1),
    
#     ("Which of the following methods can add an element to a set?", 
#      ["1. add()", "2. append()", "3. insert()", "4. extend()"], 1),
    
#     ("What will be the output of 'print(len({1, 2, 2, 3}))'?", 
#      ["1. 4", "2. 3", "3. 2", "4. Error"], 2),
    
#     ("Which of these is a correct way to create an empty dictionary?", 
#      ["1. {}", "2. dict()", "3. {[]}", "4. Both 1 and 2"], 4),
    
#     ("What is the output of 'print(bool(None))'?", 
#      ["1. True", "2. False", "3. None", "4. Error"], 2),
    
#     ("Which function converts a string to a list of characters?", 
#      ["1. list()", "2. split()", "3. tuple()", "4. str()"], 1),
    
#     ("What is the result of 'print([1, 2, 3] + [4, 5])'?", 
#      ["1. [1, 2, 3, 4, 5]", "2. [5, 7, 8]", "3. Error", "4. None"], 1),
    
#     ("Which operator is used for floor division?", 
#      ["1. /", "2. //", "3. %", "4. **"], 2),
    
#     ("What does 'print(type([]))' return?", 
#      ["1. <class 'list'>", "2. <class 'tuple'>", "3. <class 'dict'>", "4. <class 'set'>"], 1),
    
#     ("How do you access the second element of a list 'x = [10, 20, 30]'?", 
#      ["1. x[2]", "2. x(1)", "3. x[1]", "4. x{1}"], 3),
    
#     ("Which of the following creates a tuple?", 
#      ["1. (1,)", "2. (1)", "3. tuple(1, 2)", "4. {1, 2}"], 1),
    
#     ("What is the output of 'print(10 % 3)'?", 
#      ["1. 3", "2. 1", "3. 10", "4. 0"], 2),
    
#     ("What does 'print(sorted([3, 2, 5, 4]))' return?", 
#      ["1. [2, 3, 4, 5]", "2. (2, 3, 4, 5)", "3. {2, 3, 4, 5}", "4. None"], 1),
    
#     ("Which function returns the total number of elements in a list?", 
#      ["1. size()", "2. length()", "3. len()", "4. count()"], 3),
    
#     ("What does 'range(3)' return?", 
#      ["1. [0, 1, 2]", "2. (0, 1, 2)", "3. range object", "4. None"], 3),
    
#     ("Which keyword is used to define a function in Python?", 
#      ["1. function", "2. define", "3. def", "4. fun"], 3),
    
#     ("What is the output of 'print(type(3.0))'?", 
#      ["1. <class 'int'>", "2. <class 'float'>", "3. <class 'complex'>", "4. <class 'str'>"], 2),
    
#     ("How do you remove an element from a dictionary?", 
#      ["1. del dict[key]", "2. dict.remove(key)", "3. dict.pop(key)", "4. Both 1 and 3"], 4),
    
#     ("Which method is used to remove all elements from a list?", 
#      ["1. remove()", "2. clear()", "3. pop()", "4. del()"], 2),
    
#     ("What will 'print(2 == 2.0)' return?", 
#      ["1. True", "2. False", "3. None", "4. Error"], 1),
# ]

# random.shuffle(questions)

# def ask_question(question, options, correct_option):
#     print("\n" + question)
#     for option in options:
#         print(option)
#     try:
#         user_choice = int(input("Enter your option (1-4): "))
#         if user_choice == correct_option:
#             print("Correct!")
#             return True
#         else:
#             print(f"Wrong! The correct answer is: {options[correct_option - 1]}")
#             return False
#     except ValueError:
#         print("\nInvalid input! Enter a number between 1-4.")
#         return False

# def single_player():
#     Player_1 = input("Player 1 input your name: ")
#     time.sleep(0.1)
#     print("\n")
#     for i in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
#         time.sleep(0.03)

#     score = 0
#     incorrect_answers = 0
#     for i in range(10):
#         question, options, correct_option = questions[i]
#         if ask_question(question, options, correct_option):
#             score += 1
#         else:
#             incorrect_answers += 1
#         if incorrect_answers < 6:
#             print_hang(incorrect_answers)
#         else:
#             break
#     print(f"\nGame Over! {Player_1} Your final score: {score}/10")
#     if incorrect_answers == 6:
#         print_hang(6)
#         print(f"{Player_1} was Hanged")
#     play_again()

# def multiplayer():
#     score1, score2 = 0, 0
#     incorrect1, incorrect2 = 0, 0
#     Player_1 = input("Player 1 input your name: ")
#     Player_2 = input("Player 2 input your name: ")
#     # print("\n")
#     for i in tqdm(range(20), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
#         time.sleep(0.025)
#     for i in range(20):
#         player = Player_1 if i % 2 == 0 else Player_2
#         print(f"\n{player}, it's your turn!")
#         question, options, correct_option = questions[i]
#         if ask_question(question, options, correct_option):
#             if player == Player_1:
#                 score1 += 1
#             else:
#                 score2 += 1
#         else:
#             if player == Player_1:
#                 incorrect1 += 1
#             else:
#                 incorrect2 += 1
        
#         print(f"\nCurrent Scores: {Player_1}: {score1}, {Player_2}: {score2}")
#         if player == Player_1 and incorrect1 < 6:
#             print(f"{Player_1}'s Hangman:")
#             print_hang(incorrect1)
#         elif player == Player_2 and incorrect2 < 6:
#             print(f"{Player_2}'s Hangman:")
#             print_hang(incorrect2)
#         else:
#             break

#     print("\nGame Over! Final Scores:")
#     print(f"{Player_1}: {score1}/10")
#     print(f"{Player_2}: {score2}/10")
#     if score1 > score2:
#         print(f"{Player_1} Wins!")
#         print(f"{Player_2} was Hanged")
#     elif score2 > score1:
#         print(f"{Player_2} Wins!")
#         print(f"{Player_1} was Hanged")
#     else:
#         print("It's a tie!")
    
#     play_again()

# def play_again():
#     while True:
#         choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
#         if choice == "yes":
#             main()
#             break
#         elif choice == "no":
#             print("Thanks for playing!")
#             break
#         else:
#             print("Invalid choice! Please enter 'yes' or 'no'.")

# def main():
#     print("\nWelcome to the Python Quiz Game!")
#     time.sleep(0.1)
#     print("The quiz is starting...\n")
#     time.sleep(0.1)
#     while True:
#         mode = input("Enter '1' for Single Player or '2' for Multiplayer: ")
#         time.sleep(0.1)
#         if mode == "1":
#             single_player()
#             break
#         elif mode == "2":
#             multiplayer()
#             break
#         else:
#             print("Invalid choice! Please enter '1' or '2'.")

# main()