# '''count =0
# while (count <4):

#     count += 1
#     print(f"{count}")
# for i in range(0, 4):
#     print(i)

# '''

# a=int(input(""))
# n=int(input(""))
# if (a>=1 and a<=1000000)and(n>=1 and n<=20):
#     ba=bin(a)
#     print(ba)
#     bal=ba<<n
#     print(bal)
#     # bar=bal>>n
#     # dif=ba-bar
#     # rstr= str(dif)
#     # rin=int(rstr, 2)
#     # print(f"Result:{rin}")

# n=int(input())
# m1=[]
# m2=[]
# for i in range(n):
#     m1.append(int(input()))

# m1.sort()

# for x in m1:
#     m2.append(x)



# # m2=[
# #     0 if i==0 else m1[i]**(2+((i+1)%2)) 
# #     for i in range(n)
# # ]

# print(f"Original List: {m1}")
# print(f"Replaced List: {m2}")



# x=int(input("Enter x: "))
# i=0
# while i<x:
#     print(i,end=' ')
#     i+=1
# else:
#     print("##")


# Python Program to find prime numbers in a range
# import math
# import time
# def is_prime(n):
# 	if n <= 1:
# 		return False
# 	if n % 2 == 0:
# 		return n == 2

# 	max_div = math.floor(math.sqrt(n))
# 	for i in range(3, 1 + max_div, 2):
# 		if n % i == 0:
# 			return False
# 	return True

# # Driver function
# t0 = time.time()
# c = 0 #for counting

# for n in range(1,1000000000):
# 	x = is_prime(n)
# 	c += x
# print("Total prime numbers in range :", c)

# t1 = time.time()
# print("Time required :", t1 - t0)


# c=0
# li=[c for c in range(10)]
# print(li)

# m=[1,2,3]
# print(m*3)

# s="happy Day"
# l=list(s)
# print(l)
# (c1, c2)=map(str, input().split())
# ch1='#'
# ch2='$'
# i1=[]
# i2=[]

# while True:
#     x = l.index(c1)
#     y = l.index(c2)
#     l[x]=ch1
#     l[y]=ch2
#     if(l.count(c1)==0 and l.count(c2)):
#         break

# while True:
#     x = l.index(ch1)
#     y = l.index(ch2)
#     l[x]=c2
#     l[y]=c1
#     if(l.count(ch1)==0 and l.count(ch2)):
#         break

# l=list(x for x in range(10))
# print(l)

# l=[1,2,3,4,5,6,7,8,9]
# print(l)
# l.append(10)
# print(l)
# l.reverse()
# print(l)
# ls=str(l)
# s='-'.join(ls)
# print(s)


# s="python Rocks"
# print(s[1]*s.index("n"))
# print(s.lower())
# print(s[2]+s[5])
# print(s.split())
# print(s.index('a'))


# import time
# import random

# def print_board(board):
#     time.sleep(0.1)
#     print("\n    1   2   3")
#     # print("  -----------")
#     for i, row in enumerate(board):
#         time.sleep(0.1)
#         if i==1:
#             print(f"{i+1}   " + " | ".join(row) + " ")
#         elif i==0:
#             print(f"{i+1} ◤ " + " | ".join(row) + " ◥")
#         elif i==2:
#             print(f"{i+1} ◣ " + " | ".join(row) + " ◢")
#         # else:
#         #     print(f"{i+1} " + " | ".join(row))
#         if i == 0:
#             time.sleep(0.1)
#             print("  |———————————|")
#         elif i == 1:
#             time.sleep(0.1)
#             print("  |———————————|")
#     # print("  -----------")



# def check_winner(board, player):
#     for row in board:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# def get_empty_cells(board):
#     return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def ai_move(board):
#     empty_cells = get_empty_cells(board)
#     return random.choice(empty_cells)

# def tic_tac_toe():
#     time.sleep(0.2)
#     print("Welcome to Tic Tac Toe!")
#     mode = input("Choose mode: 1 for Single Player, 2 for Multiplayer: ").strip()

#     scores = {"Player 1": 0, "Player 2": 0}

#     while True:
#         board = [[" " for _ in range(3)] for _ in range(3)]
#         players = ["✕", "Θ"]
#         turn = 0
#         winner = None

#         while True:
#             print_board(board)
#             current_player = players[turn % 2]
            
#             if mode == "1" and current_player == "Θ": #ϴ0
#                 time.sleep(0.5)
#                 print("\nAI is making a move...")
#                 time.sleep(1)
#                 row, col = ai_move(board)
#             else:
#                 move = input(f"\nPlayer {turn % 2 + 1} ({current_player}), enter row and column (1-3, space-separated): ")
#                 try:
#                     row, col = map(int, move.split())
#                     row, col = row - 1, col - 1  # Convert to 0-based index
#                     if board[row][col] != " ":
#                         time.sleep(0.1)
#                         print("\n!Cell is occupied! Try again.")
#                         continue
#                 except (ValueError, IndexError):
#                     time.sleep(0.1)
#                     print("Invalid input. Enter row and column as two numbers between 1 and 3.")
#                     continue
            
#             board[row][col] = current_player

#             if check_winner(board, current_player):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print(f"\nPlayer {turn % 2 + 1} ({current_player}) wins!")
#                 if mode == "2":
#                     scores[f"Player {turn % 2 + 1}"] += 3  # Award 3 points
#                 winner = current_player
#                 break

#             if not get_empty_cells(board):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print("\nIt's a draw!")
#                 break

#             turn += 1

#         if mode == "2":
#             time.sleep(0.1)
#             print("\nScoreboard:")
#             for player, score in scores.items():
#                 time.sleep(0.1)
#                 print(f"{player}: {score}")

#         again = input("Wana play again? (yes/no): ").strip().lower()
#         if again != "yes":
#             time.sleep(0.1)
#             print("Thanks for playing!")
#             break

# tic_tac_toe()

# text = "*"
# for i in range(1, 10):
#     result = text*i
#     print(result.center(21, " "))

# import numpy as np
# import random
# import time

# def create_board():
#     return np.zeros((6, 7), dtype=int)

# def print_board(board):
#     print(" \n  > 1   2   3   4   5   6   7 <")
#     print("  |———————————————————————————|")
#     arr = np.flip(board, 0)
#     for i, row in enumerate(arr):
#         time.sleep(0.05)
#         row_str = "| " + " | ".join(map(str, row)) + " |" 
#         if i < 6:
#             print(f"{i+1} {row_str}")

# def is_valid_move(board, col):
#     return board[5][col] == 0

# def get_next_open_row(board, col):
#     for r in range(6):
#         if board[r][col] == 0:
#             return r

# def drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def check_win(board, piece):
#     for c in range(4):
#         for r in range(6):
#             if all(board[r, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(7):
#         for r in range(3):
#             if all(board[r + i, c] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3):
#             if all(board[r + i, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3, 6):
#             if all(board[r - i, c + i] == piece for i in range(4)):
#                 return True
#     return False

# def ai_move(board):
#     valid_moves = [c for c in range(7) if is_valid_move(board, c)]
#     return random.choice(valid_moves)

# def play_game():
#     time.sleep(0.1)
#     print("\nWelcome to 4 in a Row!")
#     time.sleep(0.1)
#     mode = input("Enter '1' for single-player or '2' for multiplayer: ")
#     board = create_board()
#     # print(board)
#     game_over = False
#     turn = 0
#     scores = {1: 0, 2: 0} if mode == '2' else None
    
#     while not game_over:
#         print_board(board)
#         if turn % 2 == 0:
#             cx = int(input("\nPlayer 1, choose a column (1-7): "))
#             col = cx - 1
#         else:
#             if mode == '1':
#                 col = ai_move(board)
#                 print("\n")
#                 time.sleep(0.7)
#                 print(f"AI is making a move...")
#                 time.sleep(1.1)
#             else:
#                 cx = int(input("\nPlayer 2, choose a column (1-7): "))
#                 col=cx-1
        
#         if is_valid_move(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
#             if check_win(board, 1 if turn % 2 == 0 else 2):
#                 time.sleep(0.1)
#                 print_board(board)
#                 print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
#                 if mode == '2':
#                     scores[1 if turn % 2 == 0 else 2] += 1
#                 game_over = True
                
#         else:
#             print("\nInvalid move! Try again.")
#             continue
        
#         turn += 1
#         if turn == 42:
#             print("\nIt's a tie!")
#             game_over = True
        
#         if game_over and mode == '1':
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 game_over = False
#                 turn = 0

#         if game_over and mode == '2':
#             print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 game_over = False
#                 turn = 0

# play_game()

# import time
# import random

# def print_board(board):
#     time.sleep(0.1)
#     print("\n    1   2   3")
#     for i, row in enumerate(board):
#         time.sleep(0.1)
#         if i == 1:
#             print(f"{i+1}   " + " | ".join(row) + " ")
#         elif i == 0:
#             print(f"{i+1} ◤ " + " | ".join(row) + " ◥")
#         elif i == 2:
#             print(f"{i+1} ◣ " + " | ".join(row) + " ◢")
#         if i == 0 or i == 1:
#             time.sleep(0.1)
#             print("  |———————————|")

# def check_winner(board, player):
#     for row in board:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# def get_empty_cells(board):
#     return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def ai_move(board):
#     empty_cells = get_empty_cells(board)
    
#     def can_win(player):
#         for r, c in empty_cells:
#             board[r][c] = player
#             if check_winner(board, player):
#                 board[r][c] = " "  # Undo move
#                 return r, c
#             board[r][c] = " "  # Undo move
#         return None

#     # 1. Check if AI can win
#     ai_symbol = "Θ"
#     player_symbol = "✕"
#     best_move = can_win(ai_symbol)
#     if best_move:
#         return best_move

#     # 2. Block the player from winning
#     best_move = can_win(player_symbol)
#     if best_move:
#         return best_move

#     # 3. Take center if available
#     if (1, 1) in empty_cells:
#         return 1, 1

#     # 4. Take a corner if available
#     corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
#     available_corners = [c for c in corners if c in empty_cells]
#     if available_corners:
#         return random.choice(available_corners)

#     # 5. Pick a random move
#     return random.choice(empty_cells)

# def tic_tac_toe():
#     time.sleep(0.2)
#     print("Welcome to Tic Tac Toe!")
#     mode = input("Choose mode: 1 for Single Player, 2 for Multiplayer: ").strip()

#     scores = {"Player 1": 0, "Player 2": 0}

#     while True:
#         board = [[" " for _ in range(3)] for _ in range(3)]
#         players = ["✕", "Θ"]
#         turn = 0

#         while True:
#             print_board(board)
#             current_player = players[turn % 2]
            
#             if mode == "1" and current_player == "Θ": 
#                 time.sleep(0.5)
#                 print("\nAI is making a move...")
#                 time.sleep(1)
#                 row, col = ai_move(board)
#             else:
#                 move = input(f"\nPlayer {turn % 2 + 1} ({current_player}), enter row and column (1-3, space-separated): ")
#                 try:
#                     row, col = map(int, move.split())
#                     row, col = row - 1, col - 1  
#                     if board[row][col] != " ":
#                         time.sleep(0.1)
#                         print("\n!Cell is occupied! Try again.")
#                         continue
#                 except (ValueError, IndexError):
#                     time.sleep(0.1)
#                     print("Invalid input. Enter row and column as two numbers between 1 and 3.")
#                     continue
            
#             board[row][col] = current_player

#             if check_winner(board, current_player):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print(f"\nPlayer {turn % 2 + 1} ({current_player}) wins!")
#                 if mode == "2":
#                     scores[f"Player {turn % 2 + 1}"] += 3  
#                 break

#             if not get_empty_cells(board):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print("\nIt's a draw!")
#                 break

#             turn += 1

#         if mode == "2":
#             time.sleep(0.1)
#             print("\nScoreboard:")
#             for player, score in scores.items():
#                 time.sleep(0.1)
#                 print(f"{player}: {score}")

#         again = input("Wana play again? (yes/no): ").strip().lower()
#         if again != "yes":
#             time.sleep(0.1)
#             print("Thanks for playing!")
#             break

# tic_tac_toe()


# if None==False:
#     print("H") 

# import numpy as np
# import random
# import time

# def create_board():
#     return np.zeros((6, 7), dtype=int)

# def print_board(board):
#     print(" \n  > 1   2   3   4   5   6   7 <")
#     print("  |———————————————————————————|")
#     arr = np.flip(board, 0)
#     for i, row in enumerate(arr):
#         row_str = "| " + " | ".join(map(str, row)) + " |"
#         print(f"{i+1} {row_str}")

# def is_valid_move(board, col):
#     return board[5][col] == 0

# def get_next_open_row(board, col):
#     for r in range(6):
#         if board[r][col] == 0:
#             return r

# def drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def check_win(board, piece):
#     for c in range(4):
#         for r in range(6):
#             if all(board[r, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(7):
#         for r in range(3):
#             if all(board[r + i, c] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3):
#             if all(board[r + i, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3, 6):
#             if all(board[r - i, c + i] == piece for i in range(4)):
#                 return True
#     return False

# def ai_move(board):
#     valid_moves = [c for c in range(7) if is_valid_move(board, c)]
    
#     def can_win(piece):
#         for c in valid_moves:
#             row = get_next_open_row(board, c)
#             if row is not None:
#                 drop_piece(board, row, c, piece)
#                 if check_win(board, piece):
#                     board[row][c] = 0  # Undo the move
#                     return c
#                 board[row][c] = 0  # Undo the move
#         return None
    
#     # AI to win
#     ai_piece = 2
#     player_piece = 1
#     move = can_win(ai_piece)
#     if move is not None:
#         return move
    
#     # Block player from winning
#     move = can_win(player_piece)
#     if move is not None:
#         return move
    
#     # Random move if no immediate win/block
#     return random.choice(valid_moves)

# def get_valid_column():
#     while True:
#         try:
#             cx = int(input("\nPlayer 1, choose a column (1-7): "))
#             if 1 <= cx <= 7:
#                 return cx - 1
#             else:
#                 print("Invalid column! Please choose a number between 1 and 7.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")

# def is_board_full(board):
#     return np.all(board != 0)

# def play_game():
#     time.sleep(0.1)
#     print("\nWelcome to 4 in a Row!")
#     time.sleep(0.1)
#     mode = input("Enter '1' for single-player or '2' for multiplayer: ")
#     board = create_board()
#     game_over = False
#     turn = 0
#     scores = {1: 0, 2: 0} if mode == '2' else None
    
#     while not game_over:
#         print_board(board)
#         if turn % 2 == 0:
#             col = get_valid_column()
#         else:
#             if mode == '1':
#                 col = ai_move(board)
#                 print("\n")
#                 time.sleep(0.6)
#                 print(f"AI is making a move...")
#                 time.sleep(1.1)
#             else:
#                 col = get_valid_column()
        
#         if is_valid_move(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
#             if check_win(board, 1 if turn % 2 == 0 else 2):
#                 time.sleep(0.1)
#                 print_board(board)
#                 print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
#                 if mode == '2':
#                     scores[1 if turn % 2 == 0 else 2] += 1
#                 game_over = True
                
#         else:
#             print("\nInvalid move! Try again.")
#             continue
        
#         turn += 1
#         if is_board_full(board):
#             print("\nIt's a tie!")
#             game_over = True
        
#         if game_over and mode == '1':
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 game_over = False
#                 turn = 0

#         if game_over and mode == '2':
#             print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 scores = {1: 0, 2: 0}  
#                 game_over = False
#                 turn = 0

# play_game()

# import random
# import time

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
#         print("Invalid input! Enter a number between 1-4.")
#         return False

# def single_player():
#     """Single-player mode: Asks 20 questions and calculates the score"""
#     print("\nStarting Quiz...\n")
#     score = 0
#     for i in range(20):
#         question, options, correct_option = questions[i]
#         if ask_question(question, options, correct_option):
#             score += 1
#     print(f"\nGame Over! Your final score: {score}/20")
#     play_again()

# def multiplayer():
#     """Multiplayer mode: Players take turns answering questions"""
#     print("\nStarting Quiz...\n")
#     score1, score2 = 0, 0
#     for i in range(20):
#         player = "Player 1" if i % 2 == 0 else "Player 2"
#         print(f"\n{player}, it's your turn!")
#         question, options, correct_option = questions[i]
#         if ask_question(question, options, correct_option):
#             if player == "Player 1":
#                 score1 += 1
#             else:
#                 score2 += 1

#     print("\nGame Over! Final Scores:")
#     print(f"Player 1: {score1}/10")
#     print(f"Player 2: {score2}/10")
#     if score1 > score2:
#         print("Player 1 Wins!")
#     elif score2 > score1:
#         print("Player 2 Wins!")
#     else:
#         print("It's a tie!")
    
#     play_again()

# def play_again():
#     """Asks the user if they want to play again"""
#     choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
#     if choice == "yes":
#         main()
#     else:
#         print("Thanks for playing! Goodbye.")

# def main():
#     """Main function to start the quiz game"""
#     print("\nWelcome to the Python Quiz Game!")
#     print("The quiz is starting...\n")
#     mode = input("Enter '1' for Single Player or '2' for Multiplayer: ")

#     if mode == "1":
#         single_player()
#     elif mode == "2":
#         multiplayer()
#     else:
#         print("Invalid choice! Please enter '1' or '2'.")
#         main()

# main()

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
#         time.sleep(0.05)

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
#     for i in tqdm(range(100), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
#         time.sleep(0.005)

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
#     print("\nStarting Quiz...\n")
#     score1, score2 = 0, 0
#     incorrect1, incorrect2 = 0, 0
#     Player_1 = input("Player 1 input your name: ")
#     Player_2 = input("Player 2 input your name: ")
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

# import time

# l=["loading",
#    "loading.",
#    "loading..",
#    "loading..."]

# for j in range(50):
#     for i in range(len(l)):
#         print("\n"*8)
#         time.sleep(0.05)
#         print(l[i])

# from tqdm import tqdm
# for i in tqdm(range(100), mininterval=0.0001, ncols=100, desc="Loading "):
#     time.sleep(0.005)

# for i in range(10):
#     # if i == 5:
#     #     break
#     print(i, end=' ')
# else:
#     print("Broken!")

# while True:
#     pass

# print(1)

# def prime(x):
#     for i in range(2,100):
#         if x%i==0:
#             pass
#         else:
#             break
#     print(x)
        
# i=1
# while i<100:
#     prime(i)
#     i+=1

# import math

# def main():
#     count = 3
#     one = 1
#     while one == 1:
#         for x in range(2, int(math.sqrt(count) + 1)):
#             if count % x == 0: 
#                 continue
#             if count % x != 0:
#                 print (count)

#         count += 1

# import time

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_nums_generator():
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1

# # Create the generator object
# primes = prime_nums_generator()

# n=10
# a=time.time()
# for _ in range(n):
#     print(next(primes))
# b=time.time()
# print("\n", b-a)

# num1="12345ABCD2"
# num2="12345abcd2"
# print(num1.isupper() and num2.islower())

# import turtle
# import time
# t=turtle.Turtle()
# for _ in range(4):

#     t.forward(100)
#     t.circle(10)
#     t.degrees(45)
#     t.fillcolor(r=255, b=0, j=0)
# time.sleep(5)

# s="hello"
# # t=s.encode()
# s.format()
# print(s,t)

# import re
# register= "24bbs0033"
# if re.match("^[1-9][0-9][a-zA-Z][a-z]|[A-Z][a-zA-Z][0-9][0-9][0-9][0-9]$",register):
#     print("Matched")
# else:
#     print("Not matched")


# regex=“([A-Z][a-z]+).*(([0][1-9]|[1-9][0-9]|[1][0-9]{2}))”

# s1={1,2,3,4,5}
# print(s1-{1,2,3,4,5})

# #4 in a row

# import numpy as np
# import random
# import time

# def create_board():
#     return np.zeros((6, 7), dtype=int)

# def print_board(board):
#     print(" \n  > 1   2   3   4   5   6   7 <")
#     print("  |———————————————————————————|")
#     arr = np.flip(board, 0)
#     for i, row in enumerate(arr):
#         row_str = "| " + " | ".join(map(str, row)) + " |"
#         time.sleep(0.05)
#         print(f"{i+1} {row_str}")

# def is_valid_move(board, col):
#     return board[5][col] == 0

# def get_next_open_row(board, col):
#     for r in range(6):
#         if board[r][col] == 0:
#             return r

# def drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def check_win(board, piece):
#     for c in range(4):
#         for r in range(6):
#             if all(board[r, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(7):
#         for r in range(3):
#             if all(board[r + i, c] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3):
#             if all(board[r + i, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3, 6):
#             if all(board[r - i, c + i] == piece for i in range(4)):
#                 return True
#     return False

# def ai_move(board):
#     valid_moves = [c for c in range(7) if is_valid_move(board, c)]
    
#     def can_win(piece):
#         for c in valid_moves:
#             row = get_next_open_row(board, c)
#             if row is not None:
#                 drop_piece(board, row, c, piece)
#                 if check_win(board, piece):
#                     board[row][c] = 0
#                     return c
#                 board[row][c] = 0
#         return None
    
#     ai_piece = 2
#     player_piece = 1
#     move = can_win(ai_piece)
#     if move is not None:
#         return move
    
#     move = can_win(player_piece)
#     if move is not None:
#         return move
    
#     return random.choice(valid_moves)

# def get_valid_column():
#     while True:
#         try:
#             cx = int(input("\nPlayer 1, choose a column (1-7): "))
#             if cx == -1:
#                 print("\nThank you for playing\n")
#                 exit()
#             if 1 <= cx <= 7:
#                 return cx - 1
#             else:
#                 print("Invalid column! Please choose a number between 1 and 7.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")

# def is_board_full(board):
#     return np.all(board != 0)

# def play_game():
#     time.sleep(0.1)
#     print("\nWelcome to 4 in a Row!")
#     time.sleep(0.1)
#     mode = input("Enter '1' for single-player or '2' for multiplayer: ")
#     board = create_board()
#     game_over = False
#     turn = 0
#     scores = {1: 0, 2: 0} if mode == '2' else None
    
#     while not game_over:
#         print_board(board)
#         if turn % 2 == 0:
#             col = get_valid_column()
#         else:
#             if mode == '1':
#                 col = ai_move(board)
#                 print("\n")
#                 time.sleep(0.6)
#                 print(f"AI is making a move...")
#                 time.sleep(1.1)
#             else:
#                 col = get_valid_column()
        
#         if is_valid_move(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
#             if check_win(board, 1 if turn % 2 == 0 else 2):
#                 time.sleep(0.1)
#                 print_board(board)
#                 print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
#                 if mode == '2':
#                     scores[1 if turn % 2 == 0 else 2] += 1
#                 game_over = True
                
#         else:
#             print("\nInvalid move! Try again.")
#             continue
        
#         turn += 1
#         if is_board_full(board):
#             print("\nIt's a tie!")
#             game_over = True
        
#         if game_over and mode == '1':
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 game_over = False
#                 turn = 0

#         if game_over and mode == '2':
#             print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = create_board()
#                 scores = {1: 0, 2: 0}  
#                 game_over = False
#                 turn = 0

# play_game()

# Existing list
# Rank_People_Alloc = [
#     ["24BBS0001", 1, "", ""],
#     ["24BBS0002", 2, "", ""],
#     ["24BBS0003", 3, "", ""],
#     ["24BBS0004", 4, "", ""],
#     ["24BBS0005", 5, "", ""],
#     ["24BBS0006", 6, "", ""],
#     ["24BBS0007", 7, "", ""],
#     ["24BBS0008", 8, "", ""],
#     ["24BBS0009", 9, "", ""],
#     ["24BBS0010", 10, "", ""],
#     ["24BBS0011", 11, "", ""],
#     ["24BBS0012", 12, "", ""],
#     ["24BBS0013", 13, "", ""],
#     ["24BBS0014", 14, "", ""],
#     ["24BBS0015", 15, "", ""]
# ]

# # Sort the list by the second element in decreasing 
# Rank_People_Alloc.sort(key=lambda x: x[1], reverse=True)

# # Print the sorted list
# print(Rank_People_Alloc)


# from collections import defaultdict

# Size_people = 15
# LoginIds = [f"24BBS{str(i).zfill(4)}" for i in range(1, 16)]
# Id_rank_dict = {f"24BBS{str(i).zfill(4)}": i for i in range(1, 16)}

# Rank_People_Alloc = [[id, i, "", ""] for id, i in Id_rank_dict.items()]
# Rank_People_Dict = {person[0]: person[2:4] for person in Rank_People_Alloc}

# Block_list = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T"]
# Room_Type_list = [["1_Bed_ac", 2], ["1_Bed_nac", 2], ["2_Bed_ac", 2], ["2_Bed_nac", 2], 
#                   ["3_Bed_ac", 2], ["3_Bed_nac", 2], ["4_Bed_ac", 2], ["4_Bed_nac", 2], 
#                   ["6_Bed_ac", 2], ["6_Bed_nac", 2], ["8_Bed_ac", 2], ["8_Bed_nac", 2]]

# Room_Type_dict = {room_type[0]: room_type[1] for room_type in Room_Type_list}
# Block_Room_Types = {block: {room_type[0]: room_type[1] for room_type in Room_Type_list} for block in Block_list}

# left_people_list = []
# All_preference = []

# # Sample data population
# # (Add your sample data here)

# All_preference.append(["24BBS0001", 1, "S", "3_Bed_ac", ["24BBS0001", "24BBS0002", "24BBS0004"]])
# All_preference.append(["24BBS0001", 2, "T", "4_Bed_ac", ["24BBS0001", "24BBS0002", "24BBS0004", "24BBS0006"]])

# All_preference.append(["24BBS0002", 1, "Q", "2_Bed_nac", ["24BBS0002", "24BBS0003"]])
# All_preference.append(["24BBS0002", 2, "Q", "3_Bed_ac", ["24BBS0002", "24BBS0003", "24BBS0004"]])

# All_preference.append(["24BBS0003", 1, "L", "1_Bed_ac", ["24BBS0003"]])

# All_preference.append(["24BBS0005", 1, "S", "2_Bed_ac", ["24BBS0005", "24BBS0003"]])
# All_preference.append(["24BBS0005", 2, "R", "4_Bed_nac", ["24BBS0005", "24BBS0003", "24BBS0006", "24BBS0007"]])

# All_preference.append(["24BBS0006", 1, "S", "3_Bed_ac", ["24BBS0006", "24BBS0007", "24BBS0010"]])
# All_preference.append(["24BBS0006", 2, "T", "4_Bed_ac", ["24BBS0006", "24BBS0007", "24BBS0009", "24BBS0010"]])

# All_preference.append(["24BBS0007", 1, "Q", "2_Bed_nac", ["24BBS0007", "24BBS0010"]])
# All_preference.append(["24BBS0007", 2, "Q", "3_Bed_ac", ["24BBS0007", "24BBS0008", "24BBS0010"]])

# All_preference.append(["24BBS0008", 1, "L", "1_Bed_ac", ["24BBS0008"]])

# All_preference.append(["24BBS0010", 1, "S", "2_Bed_ac", ["24BBS0010", "24BBS0009"]])
# All_preference.append(["24BBS0010", 2, "R", "4_Bed_nac", ["24BBS0010", "24BBS0006", "24BBS0008", "24BBS0009"]])

# All_preference.append(["24BBS0011", 1, "S", "3_Bed_ac", ["24BBS0011", "24BBS0012", "24BBS0013"]])
# All_preference.append(["24BBS0011", 2, "R", "4_Bed_nac", ["24BBS0011", "24BBS0012", "24BBS0013", "24BBS0014"]])


# allocated_ids = {person[0] for person in Rank_People_Alloc}

# def is_room_available(block, room):
#     return Block_Room_Types[block].get(room, 0) > 0

# def is_Id_allocated(id):
#     return Rank_People_Dict[id][0] != ""

# def MasterFunction():
#     for preference in All_preference:
#         id = preference[0]
        
#         if is_Id_allocated(id):
#             continue

#         block = preference[2]
#         room_type = preference[3]

#         if not is_room_available(block, room_type):
#             continue

#         if any(pref_id in allocated_ids for pref_id in preference[4]):
#             continue

#         for i in preference[4]:
#             Rank_People_Dict[i][0] = block
#             Rank_People_Dict[i][1] = room_type
#         Block_Room_Types[block][room_type] -= 1

# def roomless_id_list():
#     return [i for i in LoginIds if not is_Id_allocated(i)]

# def secondary_allotment():
#     while left_people_list:
#         for block in ["A", "B", "C"]:
#             for room_type in ["8_Bed_nac", "8_Bed_ac", "6_Bed_nac", "6_Bed_ac"]:
#                 if is_room_available(block, room_type):
#                     for person in left_people_list:
#                         Rank_People_Dict[person][0] = block
#                         Rank_People_Dict[person][1] = room_type 
#                     Block_Room_Types[block][room_type] -= len(left_people_list)
#                     left_people_list.clear()
#                     break

# def sort_all_preferences():
#     All_preference.sort(key=lambda x: (Id_rank_dict.get(x[0], float('inf')), x[1]), reverse=False)

# def display():
#     for i in Rank_People_Dict.items():
#         print("ID - ", i[0], " Block - ", i[1][0], " Room Type - ", i[1][1])

# # Execute the functions in the correct order
# sort_all_preferences()
# MasterFunction()
# left_people_list = roomless_id_list()
# secondary_allotment()
# display()

# Size_people = 30

# # to login - loginID shoule be = password
# LoginIds = [f"24BBS{str(i).zfill(4)}" for i in range(1, 31)]

# #format -> ID, Rank
# Id_rank_dict = {f"24BBS{str(i).zfill(4)}": i for i in range(1, 31)}

# #format -> Id, rank, allocated Block, Allocated Room_type
# # Rank_People_Alloc=[]
# # Rank_People_Dict={}
# # Rank_People_Alloc = [["24BBS0001", 1, "", ""],["24BBS0002", 2, "", ""],["24BBS0003", 3, "", ""],["24BBS0004", 4, "", ""],["24BBS0005", 5, "", ""],
# # 			        ["24BBS0006", 6, "", ""],["24BBS0007", 7, "", ""],["24BBS0008", 8, "", ""],["24BBS0009", 9, "", ""],["24BBS0010", 10, "", ""],
# # 				    ["24BBS0011", 11, "", ""],["24BBS0012", 12, "", ""],["24BBS0013", 13, "", ""],["24BBS0014", 14, "", ""],["24BBS0015", 15, "", ""],
# #                     ["24BBS0016", 16, "", ""],["24BBS0017", 17, "", ""],["24BBS0018", 18, "", ""],["24BBS0019", 19, "", ""],["24BBS0020", 20, "", ""],
# #                     ["24BBS0021", 21, "", ""],["24BBS0022", 22, "", ""],["24BBS0023", 23, "", ""],["24BBS0024", 24, "", ""],["24BBS0025", 25, "", ""],
# #                     ["24BBS0026", 26, "", ""],["24BBS0027", 27, "", ""],["24BBS0028", 28, "", ""],["24BBS0029", 29, "", ""],["24BBS0030", 30, "", ""]]

# # def generate_Rank_People_Alloc_list():
# #     for i in range(1, 31):
# #         Rank_People_Alloc.append([f"24BBS{str(i).zfill(4)}", i, "", ""])

# Rank_People_Alloc = [[f"24BBS{str(i).zfill(4)}", i, "", ""] for i in range(1, 31)]

# Rank_People_Dict = {person[0]: person[2:4] for person in Rank_People_Alloc}

# Block_list = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T"]

# #format -> Type, available rooms(default->total rooms)
# Room_Type_list = [
#     ["1_Bed_ac", 2], ["1_Bed_nac", 2], 
#     ["2_Bed_ac", 2], ["2_Bed_nac", 2], 
#     ["3_Bed_ac", 2], ["3_Bed_nac", 2], 
#     ["4_Bed_ac", 2], ["4_Bed_nac", 2], 
#     ["6_Bed_ac", 2], ["6_Bed_nac", 2], 
#     ["8_Bed_ac", 2], ["8_Bed_nac", 2]
# ]   # accomodates max 96 people (for now)

# #format -> room_type : num
# Room_Type_dict = {room_type[0]: room_type[1] for room_type in Room_Type_list}
# #format -> Block : (room_type : num)
# Block_Room_Types = {block: {room_type[0]: room_type[1] for room_type in Room_Type_list} for block in Block_list}

# left_people_list= []
# All_preference = []
#         # Sample data
# #when a user logins and sets a preference - data retreived from frontend -> 
# #format -> Id, pref no., Block, room_type, list of (roommates)

# All_preference.append(["24BBS0001", 1, "S", "3_Bed_ac", ["24BBS0001", "24BBS0002", "24BBS0004"]])
# All_preference.append(["24BBS0001", 2, "T", "4_Bed_ac", ["24BBS0001", "24BBS0002", "24BBS0004", "24BBS0006"]])

# All_preference.append(["24BBS0002", 1, "Q", "2_Bed_nac", ["24BBS0002", "24BBS0003"]])
# All_preference.append(["24BBS0002", 2, "Q", "3_Bed_ac", ["24BBS0002", "24BBS0003", "24BBS0004"]])

# All_preference.append(["24BBS0003", 1, "L", "1_Bed_ac", ["24BBS0003"]])

# All_preference.append(["24BBS0005", 1, "S", "2_Bed_ac", ["24BBS0005", "24BBS0003"]])
# All_preference.append(["24BBS0005", 2, "R", "4_Bed_nac", ["24BBS0005", "24BBS0003", "24BBS0006", "24BBS0007"]])

# All_preference.append(["24BBS0006", 1, "S", "3_Bed_ac", ["24BBS0006", "24BBS0007", "24BBS0010"]])
# All_preference.append(["24BBS0006", 2, "T", "4_Bed_ac", ["24BBS0006", "24BBS0007", "24BBS0009", "24BBS0010"]])

# All_preference.append(["24BBS0007", 1, "Q", "2_Bed_nac", ["24BBS0007", "24BBS0010"]])
# All_preference.append(["24BBS0007", 2, "Q", "3_Bed_ac", ["24BBS0007", "24BBS0008", "24BBS0010"]])

# All_preference.append(["24BBS0008", 1, "L", "1_Bed_ac", ["24BBS0008"]])

# All_preference.append(["24BBS0010", 1, "S", "2_Bed_ac", ["24BBS0010", "24BBS0009"]])
# All_preference.append(["24BBS0010", 2, "R", "4_Bed_nac", ["24BBS0010", "24BBS0006", "24BBS0008", "24BBS0009"]])

# All_preference.append(["24BBS0011", 1, "S", "3_Bed_ac", ["24BBS0011", "24BBS0012", "24BBS0013"]])
# All_preference.append(["24BBS0011", 2, "R", "4_Bed_nac", ["24BBS0011", "24BBS0012", "24BBS0013", "24BBS0014"]])

# All_preference.append(["24BBS0012", 1, "Q", "2_Bed_ac", ["24BBS0012", "24BBS0023"]])
# All_preference.append(["24BBS0012", 2, "S", "3_Bed_ac", ["24BBS0012", "24BBS0023", "24BBS0029"]])

# All_preference.append(["24BBS0013",1,"T","4_Bed_ac",["24BBS0013","24BBS0015","24BBS0016","24BBS0017"]])

# All_preference.append(["24BBS0014",1,"K","1_Bed_nac",["24BBS0014"]])

# All_preference.append(["24BBS0015",1,"T","2_Bed_nac",["24BBS0015","24BBS0020"]])

# All_preference.append(["24BBS0016",1,"S","3_Bed_ac",["24BBS0016","24BBS0002","24BBS0003"]])
# All_preference.append(["24BBS0016",2,"S","4_Bed_ac",["24BBS0016","24BBS0002","24BBS0003","24BBS0005"]])

# All_preference.append(["24BBS0017",1,"T","1_Bed_ac",["24BBS0017"]])
# All_preference.append(["24BBS0017",2,"T","1_Bed_Nac",["24BBS0017"]])

# All_preference.append(["24BBS0018",1,"Q","2_Bed_nac",["24BBS0018","24BBS0023"]])
# All_preference.append(["24BBS0018",2,"Q","4_Bed_ac",["24BBS0018","24BBS0023","24BBS0024","24BBS0028"]])

# All_preference.append(["24BBS0019",1,"T","3_Bed_nac",["24BBS0019","24BBS0020","24BBS0021"]])

# All_preference.append(["24BBS0020",1,"Q","2_Bed_ac",["24BBS0020","24BBS0005"]])

# All_preference.append(["24BBS0021",1,"S","2_Bed_ac",["24BBS0021","24BBS0029"]])
# All_preference.append(["24BBS0021",2,"T","3_Bed_nac",["24BBS0021","24BBS0029","24BBS0030"]])

# All_preference.append(["24BBS0022",1,"Q","1_Bed_ac",["24BBS0022"]])
# All_preference.append(["24BBS0022",2,"Q","2_Bed_nac",["24BBS0022","24BBS0023"]])

# All_preference.append(["24BBS0024",1,"S","4_Bed_ac",["24BBS0024","24BBS0001","24BBS0002","24BBS0003"]])
# All_preference.append(["24BBS0024",2,"S","3_Bed_nac",["24BBS0024","24BBS0001","24BBS0003"]])

# All_preference.append(["24BBS0025",1,"Q","3_Bed_nac",["24BBS0025","24BBS0026","24BBS0030"]])

# All_preference.append(["24BBS0027",1,"S","2_Bed_ac",["24BBS0027","24BBS0023"]])
# All_preference.append(["24BBS0027",2,"S","2_Bed_nac",["24BBS0027","24BBS0023"]])

# All_preference.append(["24BBS0028",1,"Q","4_Bed_ac",["24BBS0028","24BBS0001","24BBS0004","24BBS0016"]])

# All_preference.append(["24BBS0029",1,"Q","1_Bed_ac",["24BBS0029"]])
# All_preference.append(["24BBS0029",2,"M","2_Bed_nac",["24BBS0029","24BBS0017"]])

# All_preference.append(["24BBS0030",1,"K","3_Bed_nac",["24BBS0030","24BBS0018","24BBS0022"]])
# All_preference.append(["24BBS0030",2,"L","4_Bed_nac",["24BBS0030","24BBS0018","24BBS0017","24BBS0009"]])


# def rank_of_id(id):   # Not usefull
#     return Id_rank_dict[id]

# def is_room_available(block, room):   #take 2 string input, check from "Block_Room_Types" if avalible, return T/F
#     if Block_Room_Types[block][room] > 0:
#         return True
#     return False

# def is_Id_allocated(id):     #take 1 string input, check is block/room_type is allocated, return T/F
#     if Rank_People_Dict[id][0] == "":
#         return False
#     return True

# def sort_all_preferences():     # first sort by rank, then sort by preference number
#     All_preference.sort(key=lambda x: (Id_rank_dict.get(x[0], float('inf')), x[1]), reverse=False)

# def MasterFunction():   # completes first round of allocations
#     for preference in All_preference:
#         id = preference[0]
        
#         if is_Id_allocated(id):
#             continue

#         block = preference[2]
#         room_type = preference[3]

#         if not is_room_available(block, room_type):
#             continue

#         if any(is_Id_allocated(pref_id) for pref_id in preference[4]):
#             continue

#         for i in preference[4]:
#             Rank_People_Dict[i][0] = block
#             Rank_People_Dict[i][1] = room_type
#         Block_Room_Types[block][room_type] -= 1

# def roomless_id_list(): # makes a list of all IDs without a room
#     for i in LoginIds:
#         if not is_Id_allocated(i):
#             left_people_list.append(i)

# def secondary_allotment():  # allocates rooms to remaining people
#     while len(left_people_list) != 0:
#         for block in ["A", "B", "C"]: 
#             for room_type in ["8_Bed_nac", "8_Bed_ac", "6_Bed_nac", "6_Bed_ac"]:
#                 if is_room_available(block, room_type):
#                     for person in left_people_list:
#                         Rank_People_Dict[person][0] = block
#                         Rank_People_Dict[person][1] = room_type 
#                     Block_Room_Types[block][room_type] -= len(left_people_list)
#                     left_people_list.clear()
#                     break

# def display():
#     for i in Rank_People_Dict.items():
#         print("ID - ", i[0], " Block - ", i[1][0], " Room Type - ", i[1][1])


# # def room_taken_in(id):              # to be compleated
# #     chosen_list = []
# #     pass

# # generate_Rank_People_Alloc_list()   # Firts thing to be ran
# sort_all_preferences() # execute before running masterFunction
# MasterFunction()        # to be ran once all the data has been taken
# roomless_id_list()      #Run fater masterfunction to get list of roomless people
# secondary_allotment()   # run after roomless_id_list to allocate reooms to all remaining ones.
# display()


# Game-Project/Game1.py

# import pygame
# import random
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up display
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("🎮 Guess the Number 🎮")

# # Set up fonts
# font = pygame.font.Font(None, 36)

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# # Game variables
# game_mode = None
# guess_limit = 0
# guess_count = 0
# random_no = 0
# input_box = pygame.Rect(200, 150, 140, 32)
# color_inactive = pygame.Color('lightskyblue3')
# color_active = pygame.Color('dodgerblue2')
# color = color_inactive
# active = False
# text = ''
# hint = ''

# # Function to get hint
# def get_hint(guess, correct_number):
#     difference = abs(guess - correct_number)
#     if difference >= 50:
#         return "💀 Whoa! You missed by a mile!"
#     elif difference >= 30:
#         return "🤦‍♂ Oof! You're still quite far."
#     elif difference >= 20:
#         return "🚀 You're getting warmer!"
#     elif difference >= 10:
#         return "🔥 Hot! You're closing in!"
#     elif difference >= 5:
#         return "⚡ Super close!"
#     else:
#         return "💥 SO CLOSE!"

# # Main game loop
# def main():
#     global active, text, guess_count, random_no, guess_limit, hint

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if input_box.collidepoint(event.pos):
#                     active = not active
#                 else:
#                     active = False
#                 color = color_active if active else color_inactive

#             if event.type == pygame.KEYDOWN:
#                 if active:
#                     if event.key == pygame.K_RETURN:
#                         try:
#                             guess_no = int(text)
#                             guess_count += 1
#                             if guess_no == random_no:
#                                 hint = f"🎉 {guess_no} was the right number! You WON!"
#                             else:
#                                 hint = get_hint(guess_no, random_no)
#                         except ValueError:
#                             hint = "❌ Invalid input! Enter a number."
#                         text = ''
#                     elif event.key == pygame.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode

#         # Clear screen
#         screen.fill(WHITE)

#         # Draw input box
#         txt_surface = font.render(text, True, color)
#         width = max(200, txt_surface.get_width()+10)
#         input_box.w = width
#         screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#         pygame.draw.rect(screen, color, input_box, 2)

#         # Display hint
#         hint_surface = font.render(hint, True, BLACK)
#         screen.blit(hint_surface, (20, 250))

#         # Display instructions
#         instructions = font.render("Enter a number (1-100):", True, BLACK)
#         screen.blit(instructions, (20, 100))

#         # Update display
#         pygame.display.flip()

# # Start the game
# if __name__ == "__main__":
#     # Set up game mode and random number
#     game_mode = int(input("Which game mode would you like to play? (1 for Single Player, 2 for Multiplayer): "))
#     if game_mode == 1:
#         random_no = random.randint(1, 100)
#         guess_limit = int(input("How many attempts would you like? "))
#         guess_count = 0
#         hint = ''
#         main()
#     else:
#         print("Multiplayer mode is not implemented in this version.")

# import pygame
# import sys
# import random

# pygame.init()

# # --- Constants ---
# WIDTH, HEIGHT = 800, 600
# FPS = 60
# FONT = pygame.font.SysFont(None, 36)
# BIG_FONT = pygame.font.SysFont(None, 48)

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (50, 150, 255)
# GRAY = (200, 200, 200)
# RED = (255, 80, 80)
# GREEN = (100, 255, 100)

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("🎮 Guess the Number")

# clock = pygame.time.Clock()

# # --- Input Box Class ---
# class InputBox:
#     def __init__(self, x, y, w, h, text=''):
#         self.rect = pygame.Rect(x, y, w, h)
#         self.color = BLACK
#         self.text = text
#         self.txt_surface = FONT.render(text, True, self.color)
#         self.active = False

#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             self.active = self.rect.collidepoint(event.pos)
#         if event.type == pygame.KEYDOWN:
#             if self.active:
#                 if event.key == pygame.K_RETURN:
#                     return self.text
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#                 self.txt_surface = FONT.render(self.text, True, self.color)
#         return None

#     def draw(self, screen):
#         pygame.draw.rect(screen, GRAY if self.active else BLACK, self.rect, 2)
#         screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

# # --- Button Class ---
# class Button:
#     def __init__(self, text, x, y, w, h, color=BLUE, text_color=WHITE):
#         self.rect = pygame.Rect(x, y, w, h)
#         self.text = text
#         self.color = color
#         self.text_color = text_color
#         self.txt_surface = FONT.render(text, True, text_color)

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect)
#         screen.blit(self.txt_surface, (self.rect.x + (self.rect.w - self.txt_surface.get_width()) // 2,
#                                        self.rect.y + (self.rect.h - self.txt_surface.get_height()) // 2))

#     def is_clicked(self, event):
#         return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# # --- Hint Generator ---
# def get_hint(guess, correct):
#     diff = abs(guess - correct)
#     if diff >= 50:
#         return "💀 Whoa! You missed by a mile!"
#     elif diff >= 30:
#         return "🤦‍♂ Still quite far!"
#     elif diff >= 20:
#         return "🚀 Warmer, but not close."
#     elif diff >= 10:
#         return "🔥 Hot!"
#     elif diff >= 5:
#         return "⚡ Super close!"
#     else:
#         return "💥 Almost there!"

# # --- Game State ---
# game_state = "menu"
# guess_limit = 0
# guess_count = 0
# random_number = 0
# guess_value = 0
# hint_text = ""
# player1 = ""
# player2 = ""
# guess_input = InputBox(300, 300, 200, 40)
# name_input = InputBox(300, 300, 200, 40)
# attempt_input = InputBox(300, 360, 200, 40)
# number_input = InputBox(300, 420, 200, 40)
# mode = ""

# # --- Main Loop ---
# running = True
# while running:
#     screen.fill(WHITE)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if game_state == "menu":
#             if single_btn.is_clicked(event):
#                 game_state = "enter_name"
#                 mode = "single"
#             elif multi_btn.is_clicked(event):
#                 game_state = "enter_name"
#                 mode = "multi"

#         elif game_state == "enter_name":
#             name = name_input.handle_event(event)
#             if name:
#                 if mode == "single":
#                     player1 = name
#                     game_state = "single_setup"
#                 else:
#                     if player1 == "":
#                         player1 = name
#                         name_input.text = ""
#                         name_input.txt_surface = FONT.render("", True, BLACK)
#                     else:
#                         player2 = name
#                         game_state = "multi_setup"

#         elif game_state in ["single_setup", "multi_setup"]:
#             attempt_input.handle_event(event)
#             number_input.handle_event(event)
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
#                 try:
#                     guess_limit = int(attempt_input.text)
#                     if mode == "single":
#                         random_number = random.randint(1, 100)
#                         game_state = "guessing"
#                     else:
#                         guess_value = int(number_input.text)
#                         if 1 <= guess_value <= 100:
#                             game_state = "guessing"
#                         else:
#                             hint_text = "❌ Number must be between 1-100"
#                 except ValueError:
#                     hint_text = "❌ Enter valid number(s)"

#         elif game_state == "guessing":
#             response = guess_input.handle_event(event)
#             if response:
#                 try:
#                     guess = int(response)
#                     guess_count += 1
#                     correct = random_number if mode == "single" else guess_value
#                     if guess == correct:
#                         game_state = "win"
#                     elif guess_count >= guess_limit:
#                         game_state = "lose"
#                     else:
#                         hint_text = get_hint(guess, correct)
#                         guess_input.text = ""
#                         guess_input.txt_surface = FONT.render("", True, BLACK)
#                 except ValueError:
#                     hint_text = "❌ Enter a valid number"

#         elif game_state in ["win", "lose"]:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     # Reset
#                     guess_count = 0
#                     guess_input.text = ""
#                     guess_input.txt_surface = FONT.render("", True, BLACK)
#                     name_input.text = ""
#                     name_input.txt_surface = FONT.render("", True, BLACK)
#                     attempt_input.text = ""
#                     attempt_input.txt_surface = FONT.render("", True, BLACK)
#                     number_input.text = ""
#                     number_input.txt_surface = FONT.render("", True, BLACK)
#                     player1 = player2 = ""
#                     game_state = "menu"

#     # --- Render UI ---
#     if game_state == "menu":
#         title = BIG_FONT.render("🎮 Guess The Number", True, BLACK)
#         screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
#         single_btn = Button("Single Player", 300, 250, 200, 50)
#         multi_btn = Button("Multiplayer", 300, 320, 200, 50)
#         single_btn.draw(screen)
#         multi_btn.draw(screen)

#     elif game_state == "enter_name":
#         prompt = "Enter Player Name:" if mode == "single" or player1 == "" else "Enter Player 2 Name:"
#         label = FONT.render(prompt, True, BLACK)
#         screen.blit(label, (300, 250))
#         name_input.draw(screen)

#     elif game_state in ["single_setup", "multi_setup"]:
#         screen.blit(FONT.render("Enter number of attempts:", True, BLACK), (300, 320))
#         attempt_input.draw(screen)
#         if mode == "multi":
#             screen.blit(FONT.render("Player 1: Enter secret number (1-100):", True, BLACK), (300, 390))
#             number_input.draw(screen)
#         if hint_text:
#             screen.blit(FONT.render(hint_text, True, RED), (300, 480))

#     elif game_state == "guessing":
#         who = player1 if mode == "single" else player2
#         screen.blit(FONT.render(f"{who}, enter your guess:", True, BLACK), (280, 250))
#         screen.blit(FONT.render(f"Attempts left: {guess_limit - guess_count}", True, BLACK), (280, 280))
#         guess_input.draw(screen)
#         if hint_text:
#             screen.blit(FONT.render(hint_text, True, RED), (280, 360))

#     elif game_state == "win":
#         msg = BIG_FONT.render("🎉 You Won! Press R to Restart", True, GREEN)
#         screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

#     elif game_state == "lose":
#         correct = random_number if mode == "single" else guess_value
#         msg = BIG_FONT.render(f"💀 You Lost! Number was {correct}. Press R to Restart", True, RED)
#         screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()
# sys.exit()


# import time
# import random

# # 🎯 Welcome Screen
# def show_menu():
#     print("""
# 🎮 Game - Guess the Number 🎮
# Choose Game Mode:

# 1 : Single Player
# 2 : Multi Player
# """)

# # 💡 Hint Generator
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

# # 🔢 General Number Input with Validation
# def input_number(prompt, min_val=None, max_val=None):
#     while True:
#         try:
#             num = int(input(prompt))
#             if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
#                 print(f"❌ Enter a number between {min_val} and {max_val}.")
#                 continue
#             return num
#         except ValueError:
#             print("❌ Error! Please input a valid number.")

# # 🧠 Game Logic (Single or Multiplayer)
# def play_guessing_game(secret_number, attempts, player_name):
#     guess_count = 0
#     while guess_count < attempts:
#         guess = input_number(f"🔢 {player_name}, enter your guess: ", 1, 100)
#         guess_count += 1

#         if guess == secret_number:
#             print(f"🎉 {guess} was the right number! You WON, {player_name}!")
#             return

#         hint = get_hint(guess, secret_number)
#         attempts_left = attempts - guess_count

#         if attempts_left > 1:
#             print(f"❌ Nope! {hint} Try again! 📉 Attempts left: {attempts_left}")
#         elif attempts_left == 1:
#             print(f"⚠ Last chance! {hint}")
#         else:
#             print(f"💀 The correct number was {secret_number}. Better luck next time, {player_name}!")

# # 🎮 Single Player Mode
# def single_player():
#     player = input("🎩 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)

#     secret_number = random.randint(1, 100)
#     guess_limit = input_number(f"{player}, how many attempts would you like? 🎯 ", 1, 100)

#     print(f"\n🚀 {player}, get ready!")
#     print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")
#     time.sleep(1)

#     play_guessing_game(secret_number, guess_limit, player)

# # 🤝 Multiplayer Mode
# def multiplayer():
#     player1 = input("👑 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)
#     player2 = input("🦸‍♂ Player 2, enter your name: ").strip().title()
#     time.sleep(0.5)

#     print(f"\n🔐 {player1}, enter a secret number while {player2} looks away!")
#     secret_number = input_number(f"{player1}, enter a number between 1 and 100: ", 1, 100)
#     guess_limit = input_number(f"🎯 How many attempts does {player2} get? ", 1, 100)

#     print(f"\n📱 Now, pass the device to {player2}!")
#     time.sleep(1.5)

#     print(f"\n⚔ {player2}, your mission: Guess the secret number!")
#     print(f"🎲 You have {guess_limit} attempts!")
#     time.sleep(1)

#     play_guessing_game(secret_number, guess_limit, player2)

# # 🔁 Replay Prompt
# def replay():
#     response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
#     return response == 'y'

# # 🚀 Main Loop
# def main():
#     while True:
#         show_menu()
#         try:
#             choice = int(input("👉 Choose mode (1 or 2): "))
#         except ValueError:
#             print("❌ Invalid input. Please enter 1 or 2.")
#             continue

#         if choice == 1:
#             single_player()
#         elif choice == 2:
#             multiplayer()
#         else:
#             print("❌ Please enter a valid game mode (1 or 2).")
#             continue

#         if not replay():
#             print("\n👋 Thanks for playing! Goodbye!")
#             break

# # 🏁 Run the game
# if __name__ == "__main__":
#     main()


# STR_MAX_SIZE = 100
# STR_MAX_LENGTH = 100
# MAX_SIZE = 100

# # Integer Stack Implementation
# int_arr = []
# int_top = -1

# def int_push(x):
#     global int_top
#     if int_top == MAX_SIZE - 1:
#         print("\nInteger Stack is Full!")
#     else:
#         int_arr.append(x)
#         int_top += 1

# def int_pop():
#     global int_top
#     if int_top == -1:
#         print("\nInteger Stack is Empty!")
#     else:
#         int_arr.pop()
#         int_top -= 1

# def int_display():
#     if int_top == -1:
#         print("\nInteger Stack is Empty!")
#     else:
#         print(f"\nTop element: {int_arr[int_top]}")

# def int_displayAll():
#     if int_top == -1:
#         print("\nInteger Stack is Empty!")
#     else:
#         print("\nStack elements:", ' '.join(str(x) for x in int_arr))

# def test_int_stack():
#     print("\n\nTesting Integer Stack:")
#     int_push(100)
#     int_push(200)
#     int_push(300)
#     int_push(400)
#     int_push(500)
#     int_push(600)
#     int_displayAll()
#     int_display()
#     int_pop()
#     int_pop()
#     int_displayAll()
#     int_display()
#     int_pop()
#     int_pop()
#     int_displayAll()
#     int_display()
#     int_pop()
#     int_pop()
#     int_displayAll()
#     int_display()
#     int_pop()
#     int_pop()
#     int_displayAll()


# # String Stack Implementation
# str_arr = []
# str_top = -1

# def str_push(x):
#     global str_top
#     if str_top == STR_MAX_SIZE - 1:
#         print("\nString Stack is Full!")
#     else:
#         x = x[:STR_MAX_LENGTH - 1]  # Limit string length
#         str_arr.append(x)
#         str_top += 1

# def str_pop():
#     global str_top
#     if str_top == -1:
#         print("\nString Stack is Empty!")
#     else:
#         str_arr.pop()
#         str_top -= 1

# def str_display():
#     if str_top == -1:
#         print("\nString Stack is Empty!")
#     else:
#         print(f"\nTop element: {str_arr[str_top]}")

# def str_displayAll():
#     if str_top == -1:
#         print("\nString Stack is Empty!")
#     else:
#         print("\nStack elements:", ' '.join(str_arr))

# def test_str_stack():
#     print("\n\nTesting String Stack:")
#     str_push("Hello")
#     str_push("World")
#     str_push("Stack")
#     str_push("Implementation")
#     str_push("In")
#     str_push("C")
#     str_displayAll()
#     str_display()
#     str_pop()
#     str_pop()
#     str_displayAll()
#     str_display()
#     str_pop()
#     str_pop()
#     str_displayAll()
#     str_display()
#     str_pop()
#     str_pop()
#     str_displayAll()
#     str_display()
#     str_pop()
#     str_pop()
#     str_displayAll()


# # Main
# if __name__ == "__main__":
#     test_int_stack()
#     test_str_stack()

# STR_MAX_SIZE = 100
# STR_MAX_LENGTH = 100
# MAX_SIZE = 100

# # Integer Queue Implementation
# int_arr = [None] * MAX_SIZE
# int_f = -1
# int_r = -1

# def int_empty():
#     return int_f == -1 and int_r == -1

# def int_full():
#     return int_r == MAX_SIZE - 1

# def int_enqueue(x):
#     global int_f, int_r
#     if int_full():
#         print("\nInteger Queue is Full!")
#     else:
#         if int_empty():
#             int_f = int_r = 0
#         else:
#             int_r += 1
#         int_arr[int_r] = x

# def int_dequeue():
#     global int_f, int_r
#     if int_empty():
#         print("\nInteger Queue is Empty!")
#     else:
#         if int_f == int_r:
#             int_f = int_r = -1
#         else:
#             int_f += 1

# def int_display():
#     if int_empty():
#         print("\nInteger Queue is Empty!")
#     else:
#         print(f"\nFront={int_arr[int_f]}, Rear={int_arr[int_r]}")

# def int_displayAll():
#     if int_empty():
#         print("\nInteger Queue is Empty!")
#     else:
#         print("\nQueue elements:", ' '.join(str(int_arr[i]) for i in range(int_f, int_r + 1)))

# def test_int_queue():
#     print("\n\nTesting Integer Queue:")
#     int_enqueue(0)
#     int_enqueue(1)
#     int_enqueue(2)
#     int_enqueue(3)
#     int_enqueue(4)
#     int_displayAll()
#     int_display()
#     int_dequeue()
#     int_dequeue()
#     int_displayAll()
#     int_display()
#     int_dequeue()
#     int_dequeue()
#     int_displayAll()
#     int_display()
#     int_dequeue()
#     int_dequeue()
#     int_displayAll()


# # String Queue Implementation
# str_arr = [None] * STR_MAX_SIZE
# str_f = -1
# str_r = -1

# def str_empty():
#     return str_f == -1 and str_r == -1

# def str_full():
#     return str_r == STR_MAX_SIZE - 1

# def str_enqueue(x):
#     global str_f, str_r
#     if str_full():
#         print("\nString Queue is Full!")
#     else:
#         if str_empty():
#             str_f = str_r = 0
#         else:
#             str_r += 1
#         str_arr[str_r] = x[:STR_MAX_LENGTH - 1]

# def str_dequeue():
#     global str_f, str_r
#     if str_empty():
#         print("\nString Queue is Empty!")
#     else:
#         if str_f == str_r:
#             str_f = str_r = -1
#         else:
#             str_f += 1

# def str_display():
#     if str_empty():
#         print("\nString Queue is Empty!")
#     else:
#         print(f"\nFront={str_arr[str_f]}, Rear={str_arr[str_r]}")

# def str_displayAll():
#     if str_empty():
#         print("\nString Queue is Empty!")
#     else:
#         print("\nQueue elements:", ' '.join(str_arr[i] for i in range(str_f, str_r + 1)))

# def test_str_queue():
#     print("\n\nTesting String Queue:")
#     str_enqueue("Hello")
#     str_enqueue("World")
#     str_enqueue("Queue")
#     str_enqueue("Implementation")
#     str_enqueue("In C")
#     str_displayAll()
#     str_display()
#     str_dequeue()
#     str_dequeue()
#     str_displayAll()
#     str_display()
#     str_dequeue()
#     str_dequeue()
#     str_displayAll()
#     str_display()
#     str_dequeue()
#     str_dequeue()
#     str_displayAll()


# # Main
# if __name__ == "__main__":
#     test_int_queue()
#     test_str_queue()


# def quick_sort_integers(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[-1]  # Leftmost element as pivot
#     left = [x for x in arr[1:] if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr[1:] if x > pivot]

#     return quick_sort_integers(left) + middle + quick_sort_integers(right)

# # Example usage:
# int_list = [10, 7, 8, 9, 1, 5]
# sorted_integers = quick_sort_integers(int_list)
# print("Sorted integers:", sorted_integers)


# def quick_sort_integers(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[-1]        # arr[len(arr) // 2]  # Choose middle element as pivot
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort_integers(left) + middle + quick_sort_integers(right)

# # Example usage:
# int_list = [10, 7, 8, 9, 1, 5]
# sorted_integers = quick_sort_integers(int_list)
# print("Sorted integers:", sorted_integers)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def xorder(root):
#     if root:
#         xorder(root.left)
#         print(root.data, end=' ')
#         xorder(root.right)


# # Inorder: Left -> Root -> Right
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=' ')
#         inorder(root.right)

# # Preorder: Root -> Left -> Right
# def preorder(root):
#     if root:
#         print(root.data, end=' ')
#         preorder(root.left)
#         preorder(root.right)

# # Postorder: Left -> Right -> Root
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data, end=' ')

# 🌲 Example Tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# # Print traversals
# print("Inorder traversal:")
# xorder(root)
# # print("\nPreorder traversal:")
# # preorder(root)
# # print("\nPostorder traversal:")
# # postorder(root)


# from collections import deque, defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#         # self.graph[v].append(u)  # Uncomment for undirected graph

#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])

#         print("BFS traversal:")
#         while queue:
#             node = queue.popleft()
#             if node not in visited:
#                 print(node, end=' ')
#                 visited.add(node)
#                 queue.extend(self.graph[node])

#     def dfs(self, start):
#         visited = set()

#         def dfs_helper(v):
#             visited.add(v)
#             print(v, end=' ')
#             for neighbor in self.graph[v]:
#                 if neighbor not in visited:
#                     dfs_helper(neighbor)

#         print("DFS traversal:")
#         dfs_helper(start)

# # 🔗 Example Usage
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 5)
# g.add_edge(2, 6)

# #        0
# #       / \
# #      1   2
# #     / \ / \
# #    3  4 5  6

# g.bfs(0)
# print()
# g.dfs(0)


# class Graph:
#     def __init__(self):
#         self.graph = {}  # simple dictionary for adjacency list

#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.graph[u] = []
#         self.graph[u].append(v)
#         # Uncomment the next lines to make it undirected
#         if v not in self.graph:
#             self.graph[v] = []
#         self.graph[v].append(u)

#     def bfs(self, start):
#         visited = set()
#         queue = [start]

#         print("BFS traversal:")
#         while queue:
#             node = queue.pop(0)  # simulate queue with list
#             if node not in visited:
#                 print(node, end=' ')
#                 visited.add(node)
#                 if node in self.graph:
#                     for neighbor in self.graph[node]:
#                         if neighbor not in visited:
#                             queue.append(neighbor)

#     def dfs(self, start):
#         visited = set()
#         print("DFS traversal:")

#         def dfs_helper(v):
#             visited.add(v)
#             print(v, end=' ')
#             if v in self.graph:
#                 for neighbor in self.graph[v]:
#                     if neighbor not in visited:
#                         dfs_helper(neighbor)

        
#         dfs_helper(start)

# # 🔗 Example Usage
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(2, 1)

# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 5)
# g.add_edge(2, 6)
# g.add_edge(2, 7)

# #       0
# #      / \
# #     1---2---7
# #    / \ / \
# #   3  4 5  6

# g.bfs(0)
# print()
# g.dfs(0)


# class node():
#     def __init__(self, data):
#         self.data=data
#         self.left=None
#         self.right=None
    
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=' ')
#         inorder(root.right)
# def preorder(root):
#     if root:
#         print(root.data, end=' ')
#         preorder(root.left)
#         preorder(root.right)
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data, end=' ')

# root = node("Hello")
# root.left=node(2)
# root.right=node(3)
# root.left.left=node(4)
# root.left.right=node(5)
# root.right.left=node(6)
# root.right.right=node(7)
# root.right.right.right=node(10)

# inorder(root)
# print()
# preorder(root)
# print()
# postorder(root)

# class graph():
#     def __init__(self):
#         self.graph={}
    
#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.graph[u]=[]
#         self.graph[u].append(v)
#         if v not in self.graph:
#             self.graph[v]=[]
#         self.graph[v].append(u)

#     def bfs(self, start):
#         visited=set()
#         queue=[start]
#         print("BFS:")
#         while queue:
#             node=queue.pop(0)
#             if node not in visited:
#                 print(node, end=' ')
#                 visited.add(node)
#                 if node in self.graph:
#                     for neighbour in self.graph[node]:
#                         if neighbour not in visited:
#                             queue.append(neighbour)
#         # print(self.graph)
#     def dfs(self, start):
#         visited=set()

#         def dfs_helper(v):
#             print(v, end=' ')
#             visited.add(v)
#             if v in self.graph:
#                 for neighbour in self.graph[v]:
#                     if neighbour not in visited:
#                         dfs_helper(neighbour)
#         print("DFS:")
#         dfs_helper(start)

# g=graph()
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(0,"hello")
# g.add_edge(1,3)
# g.add_edge(1,4)
# g.add_edge(2,5)
# g.add_edge(2,6)

# g.bfs(0)
# print()
# g.dfs(0)


###################################################################################################################
# import time


# from functools import lru_cache

# @lru_cache(maxsize=None) 
# def fibo(x):
#     if x<=1:
#         return x
#     else:
#         return(fibo(x-1)+fibo(x-2))
    
# n=int(input(">> : "))

# n1 = time.time()
# for i in range(n):
#     print("\n", i, "\n")
#     print(fibo(i), end=' ')

# n2 = time.time()
# print("\n",n2-n1)
# print(fibo.cache_info())


# import random


# import time
# time.sleep(0.1)


# from tqdm import tqdm
# for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
#         time.sleep(0.03)


# import os
# os.system('cls' if os.name == 'nt' else 'clear')


################################

#guess the number

# import time
# import random

# def G1_show_menu():
#     print("""
# 🎮 Game - Guess the Number 🎮
# Choose Game Mode:

# 1 : Single Player
# 2 : Multi Player
# """)

# def G1_get_hint(guess, correct_number):
#     difference = abs(guess - correct_number)

#     if difference >= 50:
#         return "💀 Whoa! You missed by a mile! Try a completely different number!"
#     elif difference >= 30:
#         return "🤦 Oof! You're still quite far, but moving in the right direction."
#     elif difference >= 20:
#         return "🚀 You're getting warmer, but still not quite there!"
#     elif difference >= 10:
#         return "🔥 Hot! You're closing in on the target!"
#     elif difference >= 5:
#         return "⚡ Super close! The number is just around the corner!"
#     else:
#         return "💥 SO CLOSE! Almost there, just tweak your guess a little!"

# def G1_input_number(prompt, min_val=None, max_val=None):
#     while True:
#         try:
#             num = int(input(prompt))
#             if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
#                 print(f"❌ Enter a number between {min_val} and {max_val}.")
#                 continue
#             return num
#         except ValueError:
#             print("❌ Error! Please input a valid number.")

# def G1_play_guessing_game(secret_number, attempts, player_name):
#     guess_count = 0
#     while guess_count < attempts:
#         guess = G1_input_number(f"🔢 {player_name}, enter your guess: ", 1, 100)
#         guess_count += 1

#         if guess == secret_number:
#             print(f"🎉 {guess} was the right number! You WON, {player_name}!")
#             return

#         hint = G1_get_hint(guess, secret_number)
#         attempts_left = attempts - guess_count

#         if attempts_left > 1:
#             print(f"❌ Nope! {hint} Try again! 📉 Attempts left: {attempts_left}")
#         elif attempts_left == 1:
#             print(f"⚠ Last chance! {hint}")
#         else:
#             print(f"💀 The correct number was {secret_number}. Better luck next time, {player_name}!")

# def G1_single_player():
#     time.sleep(0.35)
#     player = input("🎩 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)

#     secret_number = random.randint(1, 100)
#     guess_limit = G1_input_number(f"{player}, how many attempts would you like? 🎯 ", 1, 100)

#     print(f"\n🚀 {player}, get ready!")
#     time.sleep(0.25)
#     print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")
#     time.sleep(1)

#     G1_play_guessing_game(secret_number, guess_limit, player)

# def G1_multiplayer():
#     player1 = input("👑 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)
#     player2 = input("🦸‍♂ Player 2, enter your name: ").strip().title()
#     time.sleep(0.5)

#     print(f"\n🔐 {player1}, enter a secret number while {player2} looks away!")
#     secret_number = G1_input_number(f"{player1}, enter a number between 1 and 100: ", 1, 100)
#     guess_limit = G1_input_number(f"🎯 How many attempts does {player2} get? ", 1, 100)

#     print(f"\n📱 Now, pass the device to {player2}!")
#     time.sleep(1.5)

#     print(f"\n⚔ {player2}, your mission: Guess the secret number!")
#     time.sleep(0.25)
#     print(f"🎲 You have {guess_limit} attempts!")
#     time.sleep(1)

#     G1_play_guessing_game(secret_number, guess_limit, player2)

# def G1_replay():
#     response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
#     return response == 'y'

# def G1_main():
#     G1_show_menu()
#     while True:

#         try:
#             choice = int(input("👉 Choose mode (1 or 2): "))
#         except ValueError:
#             print("❌ Invalid input. Please enter 1 or 2.")
#             continue

#         if choice == 1:
#             G1_single_player()
#         elif choice == 2:
#             G1_multiplayer()
#         else:
#             print("❌ Please enter a valid game mode (1 or 2).")
#             continue

#         if not G1_replay():
#             print("\n👋 Thanks for playing! Goodbye!")
#             time.sleep(0.4)
#             break



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


# hang = [
#     "------  ",
#     "|    |  ",
#     "|    0  ",
#     "|   /|\\",
#     "|   / \\",
#     "|       "
# ]

# def G2_print_hang(x):
#     for i in range(x):
#         print(hang[i])
#         time.sleep(0.075)

# def G2_ask_question(question, options, correct_option):
#     print("\n" + question)
#     for option in options:
#         print(option)
#     while True:
#         try:
#             user_choice = int(input("Enter your option (1-4): "))
#             if 1 <= user_choice <= 4:
#                 break
#             else:
#                 print("Please choose a number between 1 and 4.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#     if user_choice == correct_option:
#         print("Correct!")
#         return True
#     else:
#         print(f"Wrong! The correct answer is: {options[correct_option - 1]}")
#         return False

# def G2_print_score(player_name, score, total):
#     print(f"\nGame Over! {player_name}, your final score: {score}/{total}")

# def G2_run_quiz(questions_subset, player_name):
#     score = 0
#     incorrect = 0
#     for i, (question, options, correct_option) in enumerate(questions_subset):
#         print(f"\nQuestion {i + 1}:")
#         if G2_ask_question(question, options, correct_option):
#             score += 1
#         else:
#             incorrect += 1
#             if incorrect < 6:
#                 G2_print_hang(incorrect)
#             else:
#                 break
#     G2_print_score(player_name, score, len(questions_subset))
#     if incorrect >= 6:
#         G2_print_hang(6)
#         print(f"{player_name} was Hanged")

# def G2_single_player(questions):
#     player_name = input("Player 1, input your name: ")
#     time.sleep(0.1)
#     # print("\n")
#     # for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):        # NEW
#     #     time.sleep(0.03)
#     G2_run_quiz(questions[:10], player_name)
#     G2_play_again()

# def G2_multiplayer(questions):
#     player1 = input("Player 1, input your name: ")
#     player2 = input("Player 2, input your name: ")
#     score1 = score2 = incorrect1 = incorrect2 = 0

#     # for _ in tqdm(range(20), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
#     #     time.sleep(0.025)

#     for i in range(20):
#         player = player1 if i % 2 == 0 else player2
#         print(f"\n{player}, it's your turn!")
#         question, options, correct_option = questions[i]
#         if G2_ask_question(question, options, correct_option):
#             if player == player1:
#                 score1 += 1
#             else:
#                 score2 += 1
#         else:
#             if player == player1:
#                 incorrect1 += 1
#                 print(f"{player1}'s Hangman:")
#                 G2_print_hang(incorrect1)
#                 if incorrect1 >= 6:
#                     print(f"{player1} was Hanged")
#                     break
#             else:
#                 incorrect2 += 1
#                 print(f"{player2}'s Hangman:")
#                 G2_print_hang(incorrect2)
#                 if incorrect2 >= 6:
#                     print(f"{player2} was Hanged")
#                     break
#         print(f"\nCurrent Scores: {player1}: {score1}, {player2}: {score2}")

#     print("\nGame Over! Final Scores:")
#     print(f"{player1}: {score1}/10")
#     print(f"{player2}: {score2}/10")
#     if score1 > score2:
#         print(f"{player1} Wins!")
#     elif score2 > score1:
#         print(f"{player2} Wins!")
#     else:
#         print("It's a tie!")
#     G2_play_again()

# def G2_play_again():
#     while True:
#         choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
#         if choice == "yes":
#             main()
#             break
#         elif choice == "no":
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break
#         else:
#             print("Invalid choice! Please enter 'yes' or 'no'.")

# def G2_main():
#     questions = [
#         ("What will be the output of 'print(3 * 3 ** 2)'?", ["1. 27", "2. 18", "3. 81", "4. 9"], 1),
#         ("Which of the following methods can add an element to a set?", ["1. add()", "2. append()", "3. insert()", "4. extend()"], 1),
#         ("What will be the output of 'print(len({1, 2, 2, 3}))'?", ["1. 4", "2. 3", "3. 2", "4. Error"], 2),
#         ("Which of these is a correct way to create an empty dictionary?", ["1. {}", "2. dict()", "3. {[]}", "4. Both 1 and 2"], 4),
#         ("What is the output of 'print(bool(None))'?", ["1. True", "2. False", "3. None", "4. Error"], 2),
#         ("Which function converts a string to a list of characters?", ["1. list()", "2. split()", "3. tuple()", "4. str()"], 1),
#         ("What is the result of 'print([1, 2, 3] + [4, 5])'?", ["1. [1, 2, 3, 4, 5]", "2. [5, 7, 8]", "3. Error", "4. None"], 1),
#         ("Which operator is used for floor division?", ["1. /", "2. //", "3. %", "4. **"], 2),
#         ("What does 'print(type([]))' return?", ["1. <class 'list'>", "2. <class 'tuple'>", "3. <class 'dict'>", "4. <class 'set'>"], 1),
#         ("How do you access the second element of a list 'x = [10, 20, 30]'?", ["1. x[2]", "2. x(1)", "3. x[1]", "4. x{1}"], 3),
#         ("Which of the following creates a tuple?", ["1. (1,)", "2. (1)", "3. tuple(1, 2)", "4. {1, 2}"], 1),
#         ("What is the output of 'print(10 % 3)'?", ["1. 3", "2. 1", "3. 10", "4. 0"], 2),
#         ("What does 'print(sorted([3, 2, 5, 4]))' return?", ["1. [2, 3, 4, 5]", "2. (2, 3, 4, 5)", "3. {2, 3, 4, 5}", "4. None"], 1),
#         ("Which function returns the total number of elements in a list?", ["1. size()", "2. length()", "3. len()", "4. count()"], 3),
#         ("What does 'range(3)' return?", ["1. [0, 1, 2]", "2. (0, 1, 2)", "3. range object", "4. None"], 3),
#         ("Which keyword is used to define a function in Python?", ["1. function", "2. define", "3. def", "4. fun"], 3),
#         ("What is the output of 'print(type(3.0))'?", ["1. <class 'int'>", "2. <class 'float'>", "3. <class 'complex'>", "4. <class 'str'>"], 2),
#         ("How do you remove an element from a dictionary?", ["1. del dict[key]", "2. dict.remove(key)", "3. dict.pop(key)", "4. Both 1 and 3"], 4),
#         ("Which method is used to remove all elements from a list?", ["1. remove()", "2. clear()", "3. pop()", "4. del()"], 2),
#         ("What will 'print(2 == 2.0)' return?", ["1. True", "2. False", "3. None", "4. Error"], 1),
#         ("Which of the following is a valid variable name in Python?", ["1. 1variable", "2. variable_1", "3. variable-1", "4. variable 1"], 2),
#         ("What is the output of 'print(type({}))'?", ["1. <class 'dict'>", "2. <class 'set'>", "3. <class 'list'>", "4. <class 'tuple'>"], 1),
#         ("Which of the following is used for single-line comments in Python?", ["1. //", "2. <!-- -->", "3. #", "4. /* */"], 3),
#         ("How do you create a list with numbers from 0 to 9 in Python?", ["1. list(range(10))", "2. range(10)", "3. [0:9]", "4. [range(10)]"], 1),
#         ("What is the output of 'print(5 == 5.0)'?", ["1. False", "2. True", "3. Error", "4. None"], 2),
#         ("What is the result of '3 < 4 and 5 > 2'?", ["1. True", "2. False", "3. Error", "4. None"], 1),
#         ("What is the output of 'print(4 ** 0.5)'?", ["1. 2.0", "2. 16", "3. 4", "4. 0"], 1),
#         ("What does 'is' compare in Python?", ["1. Value", "2. Identity", "3. Type", "4. Scope"], 2),
#         ("Which of the following is NOT a valid data type in Python?", ["1. string", "2. list", "3. map", "4. float"], 3),
#         ("What does the 'pass' statement do?", ["1. Skips iteration", "2. Terminates program", "3. Does nothing", "4. Raises an error"], 3),
#         ("Which statement is used to stop a loop in Python?", ["1. stop", "2. break", "3. exit", "4. quit"], 2),
#         ("Which of the following will create a set?", ["1. {1, 2, 3}", "2. [1, 2, 3]", "3. (1, 2, 3)", "4. <1, 2, 3>"], 1),
#         ("What is the keyword to handle exceptions in Python?", ["1. try", "2. check", "3. catch", "4. handle"], 1),
#         ("Which keyword is used to create a class in Python?", ["1. define", "2. function", "3. class", "4. def"], 3),
#         ("What is the result of 'len(\"hello\")'?", ["1. 5", "2. 4", "3. 6", "4. Error"], 1),
#         ("What does 'elif' stand for in Python?", ["1. Else if", "2. Else loop", "3. End if", "4. Else function"], 1),
#         ("How do you write an infinite loop in Python?", ["1. while(True):", "2. for(;;)", "3. while 1", "4. repeat forever"], 1),
#         ("Which of these is used to define a block of code in Python?", ["1. Curly braces", "2. Parentheses", "3. Indentation", "4. Semicolons"], 3),
#         ("Which function gives the Unicode of a character?", ["1. unicode()", "2. char()", "3. ord()", "4. ascii()"], 3),
#         ("What is the output of 'print(\"Hello\"[::-1])'?", ["1. Hello", "2. olleH", "3. Error", "4. hELLO"], 2)
#     ]
    
#     random.shuffle(questions)
#     print("\n🎮 Welcome to the Python Quiz Game! 🎮")
#     time.sleep(0.1)
#     print("The quiz is starting...\n")
#     time.sleep(0.1)
#     while True:
#         mode = input("Enter '1' for Single Player or '2' for Multiplayer: ").strip()
#         if mode == "1":
#             G2_single_player(questions)
#             break
#         elif mode == "2":
#             G2_multiplayer(questions)
#             break
#         else:
#             print("Invalid choice! Please enter '1' or '2'.")

#Rock Paper and Scissors

# def G3_get_move_input(player_name):
#     time.sleep(0.1)
#     move = input(f"{player_name}, enter move (Rock, Paper, Scissor): ").strip().lower()
#     while move not in values:
#         print("Invalid move! Please enter Rock, Paper, or Scissor.")
#         move = input(f"{player_name}, enter move: ").strip().lower()
#     return move

# def G3_decide_winner(p1_move, p2_move):
#     if p1_move == p2_move:
#         return 0
#     elif (p1_move, p2_move) in win_conditions:
#         return 1
#     else:
#         return 2

# def G3_display_score(name1, score1, name2=None, score2=None):
#     if name2:
#         print(f"{name1} has {score1} point(s), {name2} has {score2} point(s)\n")
#     else:
#         print(f"{name1}, you have {score1} point(s)\n")

# def G3_play_single_player():
#     time.sleep(0.2)
#     player_name = input("Player 1, enter your name: ")
#     time.sleep(0.1)
#     rounds = int(input(f"{player_name}, how many rounds would you like to play? "))
#     time.sleep(0.1)
#     print(f"{player_name}, Get ready!\n")
#     time.sleep(0.05)

#     score = 0
#     for round_num in range(1, rounds + 1):
#         print(f"Round {round_num} of {rounds}")
#         time.sleep(0.2)
#         player_move = G3_get_move_input(player_name)
#         computer_move = random.choice(values)
#         time.sleep(0.1)
#         print(f"Computer chose: {computer_move}")

#         result = G3_decide_winner(player_move, computer_move)
#         if result == 0:
#             print("It's a tie!")
#         elif result == 1:
#             print(f"{player_name}, you won this round!")
#             score += 1
#         else:
#             print(f"{player_name}, you lost this round.")

#         G3_display_score(player_name, score)

# def G3_play_multiplayer():
#     player1 = input("Player 1, enter your name: ")
#     player2 = input("Player 2, enter your name: ")
#     rounds = int(input("How many rounds would you like to play? "))
#     print(f"{player1} and {player2}, Get ready!\n")

#     score1 = 0
#     score2 = 0

#     for round_num in range(1, rounds + 1):
#         print(f"Round {round_num} of {rounds}")
#         move1 = G3_get_move_input(player1)
#         move2 = G3_get_move_input(player2)

#         result = G3_decide_winner(move1, move2)
#         if result == 0:
#             print("It's a tie!")
#         elif result == 1:
#             print(f"{player1} won this round!")
#             score1 += 1
#         else:
#             print(f"{player2} won this round!")
#             score2 += 1

#         G3_display_score(player1, score1, player2, score2)

# values = ["rock", "paper", "scissor"]
# win_conditions = {
#     ("rock", "scissor"),
#     ("scissor", "paper"),
#     ("paper", "rock")
# }

# def G3_replay():
#     response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
#     return response == 'y'

# def G3_main():
#     print("""
#         🎮 Game - Rock Paper Scissors 🎮
#         Choose Mode:
#         1 : Single Player
#         2 : Multiplayer
#         """)
#     while True:
#         # mode=0
#         # while mode==0:
#         try:
#             mode = int(input("Enter the mode number: "))
#             if mode == 1:
#                 G3_play_single_player()
#             elif mode == 2:
#                 G3_play_multiplayer()
#             else:
#                 print("Invalid mode selected. Please enter 1 or 2.")
#                 continue
#         except ValueError:
#             print("!Error! Please enter a number, not letters.")
#             continue

#         if not G3_replay():
#             print("\n👋 Thanks for playing! Goodbye!")
#             time.sleep(0.4)
#             break

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

# #tic tac toe //bugtest

# import time
# import random
# import os

# def G4_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("\n    1   2   3")
#     for i, row in enumerate(board):
#         prefix = f"{i+1} "
#         if i == 0:
#             prefix += "◤ "
#         elif i == 2:
#             prefix += "◣ "
#         else:
#             prefix += "  "

#         print(f"{prefix}" + " | ".join(row) + (" ◥" if i == 0 else " ◢" if i == 2 else " "))
#         if i < 2:
#             print("  |———————————|")
#     print()

# def G4_check_winner(board, player):
#     win_patterns = (
#         board,
#         [[board[r][c] for r in range(3)] for c in range(3)],
#         [[board[i][i] for i in range(3)]],
#         [[board[i][2 - i] for i in range(3)]]
#     )
#     return any(all(cell == player for cell in line) for group in win_patterns for line in group)

# def G4_get_empty_cells(board):
#     return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def G4_ai_move(board, ai="Θ", player="✕"):
#     def can_win(symbol):
#         for r, c in G4_get_empty_cells(board):
#             board[r][c] = symbol
#             if G4_check_winner(board, symbol):
#                 board[r][c] = " "
#                 return r, c
#             board[r][c] = " "
#         return None

#     return (
#         can_win(ai) or
#         can_win(player) or
#         (1, 1) if board[1][1] == " " else
#         random.choice([c for c in [(0, 0), (0, 2), (2, 0), (2, 2)] if board[c[0]][c[1]] == " "]) or
#         random.choice(G4_get_empty_cells(board))
#     )

# def G4_get_player_move(board, player_symbol, player_num):
#     while True:
#         move = input(f"Player {player_num} ({player_symbol}), enter row and column (1-3, space-separated): ")
#         try:
#             row, col = map(int, move.split())
#             row -= 1
#             col -= 1
#             if (0 <= row < 3) and (0 <= col < 3) and board[row][col] == " ":
#                 return row, col
#             print("Invalid move. Cell is occupied or out of range.")
#         except (ValueError, IndexError):
#             print("Invalid input. Please enter two numbers between 1 and 3.")

# def G4_main():
#     print("\n🎮 Welcome to Tic Tac Toe! 🎮")
#     mode = int(input("""
#         Choose mode: 
#         1 for Single Player 
#         2 for Multiplayer
#         : """).strip())

#     scores = {"Player 1": 0, "Player 2": 0}
#     players = ["✕", "Θ"]

#     while True:
#         board = [[" "]*3 for _ in range(3)]
#         turn = 0

#         while True:
#             G4_print_board(board)
#             current_player = players[turn % 2]

#             if mode == 1 and current_player == "Θ":
#                 time.sleep(0.3)
#                 print("AI is making a move...")
#                 time.sleep(0.5)
#                 row, col = G4_ai_move(board)
#             else:
#                 row, col = G4_get_player_move(board, current_player, turn % 2 + 1)

#             board[row][col] = current_player

#             if G4_check_winner(board, current_player):
#                 G4_print_board(board)
#                 print(f"Player {turn % 2 + 1} ({current_player}) wins!")
#                 if mode == 2:
#                     scores[f"Player {turn % 2 + 1}"] += 3
#                 break

#             if not G4_get_empty_cells(board):
#                 G4_print_board(board)
#                 print("It's a draw!")
#                 break

#             turn += 1

#         if mode == 2:
#             print("\nScoreboard:")
#             for player, score in scores.items():
#                 print(f"{player}: {score}")
#             print()

#         if input("Wanna play again? (yes/no): ").strip().lower() != "yes":
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break



###################################################
# import time
# import random

# def print_board(board):
#     time.sleep(0.1)
#     print("\n    1   2   3")
#     for i, row in enumerate(board):
#         time.sleep(0.1)
#         if i == 1:
#             print(f"{i+1}   " + " | ".join(row) + " ")
#         elif i == 0:
#             print(f"{i+1} ◤ " + " | ".join(row) + " ◥")
#         elif i == 2:
#             print(f"{i+1} ◣ " + " | ".join(row) + " ◢")
#         if i == 0 or i == 1:
#             time.sleep(0.1)
#             print("  |———————————|")

# def check_winner(board, player):
#     for row in board:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# def get_empty_cells(board):
#     return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def ai_move(board):
#     empty_cells = get_empty_cells(board)
    
#     def can_win(player):
#         for r, c in empty_cells:
#             board[r][c] = player
#             if check_winner(board, player):
#                 board[r][c] = " "
#                 return r, c
#             board[r][c] = " "
#         return None

#     ai_symbol = "Θ"
#     player_symbol = "✕"
#     best_move = can_win(ai_symbol)
#     if best_move:
#         return best_move

#     best_move = can_win(player_symbol)
#     if best_move:
#         return best_move

#     if (1, 1) in empty_cells:
#         return 1, 1

#     corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
#     available_corners = [c for c in corners if c in empty_cells]
#     if available_corners:
#         return random.choice(available_corners)

#     return random.choice(empty_cells)

# def tic_tac_toe():
#     time.sleep(0.2)
#     print("Welcome to Tic Tac Toe!")
#     mode = input("Choose mode: 1 for Single Player, 2 for Multiplayer: ").strip()

#     scores = {"Player 1": 0, "Player 2": 0}

#     while True:
#         board = [[" " for _ in range(3)] for _ in range(3)]
#         players = ["✕", "Θ"]
#         turn = 0

#         while True:
#             print_board(board)
#             current_player = players[turn % 2]
            
#             if mode == "1" and current_player == "Θ": 
#                 time.sleep(0.5)
#                 print("\nAI is making a move...")
#                 time.sleep(1)
#                 row, col = ai_move(board)
#             else:
#                 move = input(f"\nPlayer {turn % 2 + 1} ({current_player}), enter row and column (1-3, space-separated): ")
#                 try:
#                     row, col = map(int, move.split())
#                     row, col = row - 1, col - 1  
#                     if board[row][col] != " ":
#                         time.sleep(0.1)
#                         print("\n!Cell is occupied! Try again.")
#                         continue
#                 except (ValueError, IndexError):
#                     time.sleep(0.1)
#                     print("Invalid input. Enter row and column as two numbers between 1 and 3.")
#                     continue
            
#             board[row][col] = current_player

#             if check_winner(board, current_player):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print(f"\nPlayer {turn % 2 + 1} ({current_player}) wins!")
#                 if mode == "2":
#                     scores[f"Player {turn % 2 + 1}"] += 3  
#                 break

#             if not get_empty_cells(board):
#                 print_board(board)
#                 time.sleep(0.1)
#                 print("\nIt's a draw!")
#                 break

#             turn += 1

#         if mode == "2":
#             time.sleep(0.1)
#             print("\nScoreboard:")
#             for player, score in scores.items():
#                 time.sleep(0.1)
#                 print(f"{player}: {score}")
#             print("\n")

#         again = input("Wana play again? (yes/no): ").strip().lower()
#         if again != "yes":
#             time.sleep(0.1)
#             print("Thanks for playing!")
#             break

# # tic_tac_toe()
# if __name__ == "__main__":
#     tic_tac_toe()

# # 2048

# import random
# import os
# from collections import defaultdict
# import time

# # Game constants
# SIZE = 4
# MOVES = {'W': 'up', 'A': 'left', 'S': 'down', 'D': 'right'}

# class Game2048:
#     def __init__(self):
#         self.board = [[0] * SIZE for _ in range(SIZE)]
#         self.score = 0
#         self.high_score = 0
#         self.game_over = False
#         self.add_new_tile()
#         self.add_new_tile()
    
#     def add_new_tile(self):
#         empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
#         if empty_cells:
#             r, c = random.choice(empty_cells)
#             self.board[r][c] = 2 if random.random() < 0.8 else 4
    
#     def compress(self, row):
#         new_row = [num for num in row if num != 0]
#         new_row += [0] * (SIZE - len(new_row))
#         return new_row
    
#     def merge(self, row):
#         new_row = row.copy()
#         for i in range(SIZE - 1):
#             if new_row[i] == new_row[i + 1] and new_row[i] != 0:
#                 new_row[i] *= 2
#                 self.score += new_row[i]  
#                 new_row[i + 1] = 0
#         return new_row
    
#     def move_left(self):
#         new_board = []
#         moved = False
#         for row in self.board:
#             compressed = self.compress(row)
#             merged = self.merge(compressed)
#             new_row = self.compress(merged)
#             new_board.append(new_row)
#             if row != new_row:
#                 moved = True
#         self.board = new_board
#         return moved
    
#     def move_right(self):
#         self.board = [row[::-1] for row in self.board]
#         moved = self.move_left()
#         self.board = [row[::-1] for row in self.board]
#         return moved
    
#     def move_up(self):
#         self.board = [list(col) for col in zip(*self.board)]
#         moved = self.move_left()
#         self.board = [list(col) for col in zip(*self.board)]
#         return moved
    
#     def move_down(self):
#         self.board = [list(col) for col in zip(*self.board)]
#         moved = self.move_right()
#         self.board = [list(col) for col in zip(*self.board)]
#         return moved
    
#     def check_game_over(self):
#         if any(0 in row for row in self.board):
#             return False
        
#         for r in range(SIZE):
#             for c in range(SIZE - 1):
#                 if self.board[r][c] == self.board[r][c + 1]:
#                     return False
        
#         for r in range(SIZE - 1):
#             for c in range(SIZE):
#                 if self.board[r][c] == self.board[r + 1][c]:
#                     return False
        
#         return True
    
#     def make_move(self, direction):
#         if self.game_over:
#             return False
        
#         moved = False
#         if direction == 'up':
#             moved = self.move_up()
#         elif direction == 'down':
#             moved = self.move_down()
#         elif direction == 'left':
#             moved = self.move_left()
#         elif direction == 'right':
#             moved = self.move_right()
        
#         # if moved:
#         self.add_new_tile()
#         self.high_score = max(self.score, self.high_score)
#         if self.check_game_over():
#             self.game_over = True
        
#         return moved
    
#     def display(self):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print(f"Score: {self.score} | High Score: {self.high_score}")
#         print("=" * (SIZE * 6))
        
#         for row in self.board:
#             print(" | ".join(f"{num:^4}" if num != 0 else "    " for num in row))
#             print("-" * (SIZE * 6))
        
#         if self.game_over:
#             print("\nGAME OVER! No more moves left.")

# def G5_main():
#     game = Game2048()
    
#     while True:
#         game.display()
        
#         move = input("Move (WASD, Q to quit): ").strip().upper()
        
#         if move == 'Q':
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break
        
#         if move in MOVES:
#             game.make_move(MOVES[move])
#         else:
#             print("Invalid move! Use W (up), A (left), S (down), D (right) or Q to quit.")
#             input("Press Enter to continue...")


# #4 in a row

# import numpy as np
# import random
# import time
# import os

# def G6_create_board():
#     return np.zeros((6, 7), dtype=int)

# def G6_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(" \n  > 1   2   3   4   5   6   7 <")
#     print("  |———————————————————————————|")
#     arr = np.flip(board, 0)
#     for i, row in enumerate(arr):
#         row_str = "| " + " | ".join(map(str, row)) + " |"
#         time.sleep(0.025)
#         print(f"{i+1} {row_str}")

# def G6_is_valid_move(board, col):
#     return board[5][col] == 0

# def G6_get_next_open_row(board, col):
#     for r in range(6):
#         if board[r][col] == 0:
#             return r

# def G6_drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def G6_check_win(board, piece):
#     for c in range(4):
#         for r in range(6):
#             if all(board[r, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(7):
#         for r in range(3):
#             if all(board[r + i, c] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3):
#             if all(board[r + i, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3, 6):
#             if all(board[r - i, c + i] == piece for i in range(4)):
#                 return True
#     return False

# def G6_ai_move(board):
#     valid_moves = [c for c in range(7) if G6_is_valid_move(board, c)]
    
#     def can_win(piece):
#         for c in valid_moves:
#             row = G6_get_next_open_row(board, c)
#             if row is not None:
#                 G6_drop_piece(board, row, c, piece)
#                 if G6_check_win(board, piece):
#                     board[row][c] = 0
#                     return c
#                 board[row][c] = 0
#         return None
    
#     ai_piece = 2
#     player_piece = 1
#     move = can_win(ai_piece)
#     if move is not None:
#         return move
    
#     move = can_win(player_piece)
#     if move is not None:
#         return move
    
#     return random.choice(valid_moves)

# def G6_get_valid_column():
#     while True:
#         try:
#             time.sleep(0.25)
#             cx = int(input("\nPlayer 1, choose a column (1-7): "))
#             if cx == -1:
#                 print("\nThank you for playing\n")
#                 time.sleep(0.4)
#                 exit()
#             if 1 <= cx <= 7:
#                 return cx - 1
#             else:
#                 print("Invalid column! Please choose a number between 1 and 7.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")

# def G6_is_board_full(board):
#     return np.all(board != 0)

# def G6_main():
#     time.sleep(0.1)
#     print("\nWelcome to 4 in a Row!")
#     time.sleep(0.1)
#     mode = input("Enter '1' for single-player or '2' for multiplayer: ")
#     board = G6_create_board()
#     game_over = False
#     turn = 0
#     scores = {1: 0, 2: 0} if mode == '2' else None
    
#     while not game_over:
#         G6_print_board(board)
#         if turn % 2 == 0:
#             col = G6_get_valid_column()
#         else:
#             if mode == '1':
#                 col = G6_ai_move(board)
#                 print("\n")
#                 time.sleep(0.6)
#                 print(f"AI is making a move...")
#                 time.sleep(1.1)
#             else:
#                 col = G6_get_valid_column()
        
#         if G6_is_valid_move(board, col):
#             row = G6_get_next_open_row(board, col)
#             G6_drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
#             if G6_check_win(board, 1 if turn % 2 == 0 else 2):
#                 time.sleep(0.1)
#                 G6_print_board(board)
#                 print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
#                 if mode == '2':
#                     scores[1 if turn % 2 == 0 else 2] += 1
#                 game_over = True
                
#         else:
#             print("\nInvalid move! Try again.")
#             continue
        
#         turn += 1
#         if G6_is_board_full(board):
#             print("\nIt's a tie!")
#             game_over = True
        
#         if game_over and mode == '1':
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = G6_create_board()
#                 game_over = False
#                 turn = 0

#         if game_over and mode == '2':
#             print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = G6_create_board()
#                 scores = {1: 0, 2: 0}  
#                 game_over = False
#                 turn = 0

# # sudoku

# import random
# import time
# import os

# def G7_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("------+-------+------")
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")
#         print()

# def G7_find_empty(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return (i, j)
#     return None

# def G7_is_valid(board, num, pos):
#     row, col = pos
#     for i in range(9):
#         if board[row][i] == num and col != i:
#             return False
#         if board[i][col] == num and row != i:
#             return False
#     box_x = col // 3
#     box_y = row // 3
#     for i in range(box_y * 3, box_y * 3 + 3):
#         for j in range(box_x * 3, box_x * 3 + 3):
#             if board[i][j] == num and (i, j) != pos:
#                 return False
#     return True

# def G7_generate_sudoku(difficulty):
#     board = [[0 for _ in range(9)] for _ in range(9)]
#     for box in range(0, 9, 3):
#         nums = list(range(1, 10))
#         random.shuffle(nums)
#         for i in range(3):
#             for j in range(3):
#                 board[box + i][box + j] = nums.pop()
#     G7_solve_board(board)
#     cells_to_remove = min(max(difficulty, 30), 60)
#     for _ in range(cells_to_remove):
#         row, col = random.randint(0, 8), random.randint(0, 8)
#         while board[row][col] == 0:
#             row, col = random.randint(0, 8), random.randint(0, 8)
#         board[row][col] = 0
#     return board

# def G7_solve_board(board):
#     find = G7_find_empty(board)
#     if not find:
#         return True
#     row, col = find
#     for num in range(1, 10):
#         if G7_is_valid(board, num, (row, col)):
#             board[row][col] = num
#             if G7_solve_board(board):
#                 return True
#             board[row][col] = 0
#     return False

# def G7_input_board():
#     print("\nEnter your Sudoku board row by row.")
#     print("Use numbers 1-9 for filled cells and 0 or . for empty cells.")
#     print("Separate numbers with spaces.")
#     board = []
#     for i in range(9):
#         while True:
#             row_input = input(f"Row {i+1}: ").replace('.', '0')
#             parts = row_input.split()
#             if len(parts) != 9:
#                 print("Please enter exactly 9 values.")
#                 continue
#             try:
#                 row = [int(x) if x.isdigit() else -1 for x in parts]
#                 if any(num < 0 or num > 9 for num in row):
#                     print("Numbers must be between 0 and 9.")
#                     continue
#                 board.append(row)
#                 break
#             except Exception:
#                 print("Invalid input. Please enter numbers only.")
#     return board

# def G7_get_fixed_cells(board):
#     return {(i, j) for i in range(9) for j in range(9) if board[i][j] != 0}

# def G7_play_move(board, fixed_cells):
#     while True:
#         move = input("Enter your move (row col num), 'hint' or 'q' to quit: ").lower()
#         if move == 'q':
#             return False
#         if move == 'hint':
#             G7_give_hint(board)
#             continue
#         parts = move.split()
#         if len(parts) != 3 or not all(part.isdigit() for part in parts):
#             print("Please enter row, column, and number as integers separated by spaces.")
#             continue
#         row, col, num = map(int, parts)
#         if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
#             print("Row, column, and number must be between 1-9.")
#             continue
#         row -= 1
#         col -= 1
#         if (row, col) in fixed_cells:
#             print("You can't change the original puzzle numbers!")
#             continue
#         if board[row][col] != 0:
#             print("That cell is already filled!")
#             continue
#         if G7_is_valid(board, num, (row, col)):
#             board[row][col] = num
#             return True
#         else:
#             print("Invalid move! That number conflicts with existing numbers.")

# def G7_give_hint(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 for num in range(1, 10):
#                     if G7_is_valid(board, num, (i, j)):
#                         print(f"Try placing in row {i+1}, column {j+1} : {num} ")
#                         return
#     print("No hints available.")

# def G7_check_complete(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return False
#             temp = board[i][j]
#             board[i][j] = 0
#             if not G7_is_valid(board, temp, (i, j)):
#                 board[i][j] = temp
#                 return False
#             board[i][j] = temp
#     return True

# def G7_main():
#     print("Welcome to Sudoku!")
#     print("Enter moves as 'row col number' (e.g., '3 5 7' to put 7 in row 3, column 5)")
#     print("Enter 'hint' for a hint or 'q' to quit at any time\n")

#     while True:
#         choice = input("Choose an option:\n1. Play a random puzzle\n2. Input your own puzzle\n> ").strip()
#         if choice == '1':
#             difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
#             difficulties = {'easy': (30, 40), 'medium': (41, 49), 'hard': (50, 60)}
#             empty_range = difficulties.get(difficulty, (41, 49))
#             empty_cells = random.randint(*empty_range)
#             board = G7_generate_sudoku(empty_cells)
#             break
#         elif choice == '2':
#             board = G7_input_board()
#             solve = input("Would you like to auto-solve your puzzle? (y/n): ").lower()
#             if solve == 'y':
#                 if G7_solve_board(board):
#                     print("\nSolved board:")
#                     G7_print_board(board)
#                 else:
#                     print("This puzzle has no valid solution.")
#                 return
#             break
#         else:
#             print("Invalid choice. Please enter 1 or 2.")

#     fixed_cells = G7_get_fixed_cells(board)
#     start_time = time.time()

#     while True:
#         print("\nCurrent board:")
#         G7_print_board(board)

#         if G7_check_complete(board):
#             elapsed = time.time() - start_time
#             mins, secs = divmod(int(elapsed), 60)
#             print(f"\nCongratulations! You solved the Sudoku in {mins} minutes and {secs} seconds.")
#             break

#         if not G7_play_move(board, fixed_cells):
#             print("\nThanks for playing!")
#             time.sleep(0.4)
#             break

#     print("\nFinal board:")
#     G7_print_board(board)


#Python syntax checker

# import traceback
# import random
# import re

# task_bank = [
#     ("Create a list and append three numbers to it.",
#      lambda lv: isinstance(lv.get('my_list'), list) and len(lv['my_list']) >= 3),

#     ("Create a tuple and access an element from it.",
#      lambda lv: isinstance(lv.get('my_tuple'), tuple)),

#     ("Create a dictionary and retrieve a value using a key.",
#      lambda lv: isinstance(lv.get('my_dict'), dict) and bool(lv['my_dict'])),

#     ("Import the math module and use the sqrt function.",
#      lambda lv: 'math' in lv and callable(lv['math'].sqrt)),

#     ("Create a set and add/remove elements.",
#      lambda lv: isinstance(lv.get('my_set'), set)),

#     ("Define a function that returns the square of a number.",
#      lambda lv: callable(lv.get('square')) and lv  == 4),

#     ("Create a list of strings and loop through it.",
#      lambda lv: isinstance(lv.get('str_list'), list) and all(isinstance(x, str) for x in lv['str_list'])),

#     ("Use a tuple to store coordinates and print them.",
#      lambda lv: isinstance(lv.get('coords'), tuple) and len(lv['coords']) == 2),

#     ("Create a dictionary of student names and grades using a for loop.",
#      lambda lv: isinstance(lv.get('grades'), dict)),

#     ("Use a set to store unique numbers and display them.",
#      lambda lv: isinstance(lv.get('unique_numbers'), set)),

#     ("Import the random module and generate a random number.",
#      lambda lv: 'random' in lv),

#     ("Define a function to check if a number is even.",
#      lambda lv: callable(lv.get('is_even')) and lv  is True),

#     ("Create a nested list and access an inner element.",
#      lambda lv: isinstance(lv.get('nested_list'), list)),

#     ("Create a dictionary of fruits and their prices, then print the most expensive fruit.",
#      lambda lv: isinstance(lv.get('fruits'), dict)),

#     ("Create a list and use pop() to remove an element.",
#      lambda lv: isinstance(lv.get('popped_list'), list)),

#     ("Define a function to return the length of a string.",
#      lambda lv: callable(lv.get('strlen')) and lv['strlen']("abc") == 3),

#     ("Make a dictionary and iterate through its keys.",
#      lambda lv: isinstance(lv.get('my_dict'), dict)),

#     ("Use a tuple to store and print 3 values.",
#      lambda lv: isinstance(lv.get('vals'), tuple) and len(lv['vals']) == 3),

#     ("Create a set and check for membership.",
#      lambda lv: isinstance(lv.get('my_set'), set)),

#     ("Check if a substring exists in a string using 'in'.",
#      lambda lv: isinstance(lv.get('text'), str) and 'a' in lv['text']),

#     ("Replace characters in a string using replace().",
#      lambda lv: isinstance(lv.get('text'), str) and 'x' not in lv['text']),

#     ("Use regex to find digits in a string.",
#      lambda lv: 're' in lv and lv.get('digits') is not None and isinstance(lv['digits'], list)),
# ]

# def G8_check_line_syntax(code_line):
#     try:
#         compile(code_line, "<line>", "exec")
#         return True
#     except SyntaxError:
#         return False

# def G8_main():
#     print("🎮 Welcome to Python Syntax Battle!")
#     start_game = input("Do you want to play? Enter y to start: ").strip().lower()
#     if start_game != 'y':
#         print("👋 Exiting game. Maybe next time!")
#         return

#     players = ["Player 1", "Player 2"]
#     points = {player: 0 for player in players}
#     turn = 0

#     while True:
#         task_description, validator = random.choice(task_bank)
#         print(f"\n📝 Task: {task_description}")

#         code_lines = []
#         sub_turn = 0

#         while True:
#             active_player = players[(turn + sub_turn) % 2]
#             print(f"\n✏ {active_player}'s turn to enter a line of code:")
#             code_line = input(">>> ").rstrip()

#             if G8_check_line_syntax(code_line):
#                 print("✅ Line is syntactically correct.")
#                 code_lines.append(code_line)
#                 points[active_player] += 1
#             else:
#                 print("❌ Syntax error! Opportunity passes to the other player.")
#                 other_player = players[(turn + sub_turn + 1) % 2]
#                 print(f"✏ {other_player}, your chance to correct the line:")
#                 code_line_alt = input(">>> ").rstrip()
#                 if G8_check_line_syntax(code_line_alt):
#                     print("✅ Corrected line accepted.")
#                     code_lines.append(code_line_alt)
#                     points[other_player] += 1
#                 else:
#                     print("❌ Still a syntax error! No line added.")

#             compile_now = input("⚙ Compile full code and validate task? (y/n): ").lower()
#             if compile_now == 'y':
#                 full_code = "\n".join(code_lines)
#                 try:
#                     compiled_code = compile(full_code, "<game>", "exec")
#                     local_vars = {}
#                     exec(compiled_code, {"re": re, "random": random}, local_vars)
#                     if validator(local_vars):
#                         print("✅ Task completed successfully! Moving to next round.")
#                     else:
#                         print("❌ Code ran, but task not completed correctly.")
#                         print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
#                     break
#                 except Exception:
#                     print("❌ Compilation or Runtime error!")
#                     print(traceback.format_exc())
#                     print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
#                     break
#             sub_turn += 1

#         print("\n📊 Current Points:")
#         for player, score in points.items():
#             print(f"   {player}: {score} points")

#         play_again = input("\n🔁 Continue to next round? (y/n): ").lower()
#         if play_again != 'y':
#             print("\n🎉 Final Scores:")
#             for player, score in points.items():
#                 print(f"   {player}: {score} points")
#             print("👋 Thanks for playing!")
#             break

#         turn += 1


# from tqdm import tqdm 
# import numpy as np
# import traceback
# import random
# import time
# import re
# import os


# ################################

# #guess the number

# def G1_show_menu():
#     print("""
# 🎮 Game - Guess the Number 🎮
# Choose Game Mode:

# 1 : Single Player
# 2 : Multi Player
# """)

# def G1_get_hint(guess, correct_number):
#     difference = abs(guess - correct_number)

#     if difference >= 50:
#         return "💀 Whoa! You missed by a mile! Try a completely different number!"
#     elif difference >= 30:
#         return "🤦 Oof! You're still quite far, but moving in the right direction."
#     elif difference >= 20:
#         return "🚀 You're getting warmer, but still not quite there!"
#     elif difference >= 10:
#         return "🔥 Hot! You're closing in on the target!"
#     elif difference >= 5:
#         return "⚡ Super close! The number is just around the corner!"
#     else:
#         return "💥 SO CLOSE! Almost there, just tweak your guess a little!"

# def G1_input_number(prompt, min_val=None, max_val=None):
#     while True:
#         try:
#             num = int(input(prompt))
#             if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
#                 print(f"❌ Enter a number between {min_val} and {max_val}.")
#                 continue
#             return num
#         except ValueError:
#             print("❌ Error! Please input a valid number.")

# def G1_play_guessing_game(secret_number, attempts, player_name):
#     guess_count = 0
#     while guess_count < attempts:
#         guess = G1_input_number(f"🔢 {player_name}, enter your guess: ", 1, 100)
#         guess_count += 1

#         if guess == secret_number:
#             print(f"🎉 {guess} was the right number! You WON, {player_name}!")
#             return

#         hint = G1_get_hint(guess, secret_number)
#         attempts_left = attempts - guess_count

#         if attempts_left > 1:
#             print(f"❌ Nope! {hint} Try again! 📉 Attempts left: {attempts_left}")
#         elif attempts_left == 1:
#             print(f"⚠ Last chance! {hint}")
#         else:
#             print(f"💀 The correct number was {secret_number}. Better luck next time, {player_name}!")

# def G1_single_player():
#     time.sleep(0.35)
#     player = input("🎩 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)

#     secret_number = random.randint(1, 100)
#     guess_limit = G1_input_number(f"{player}, how many attempts would you like? 🎯 ", 1, 100)

#     print(f"\n🚀 {player}, get ready!")
#     time.sleep(0.25)
#     print(f"🎲 You have {guess_limit} attempts to guess the number between 1 and 100!")
#     time.sleep(1)

#     G1_play_guessing_game(secret_number, guess_limit, player)

# def G1_multiplayer():
#     player1 = input("👑 Player 1, enter your name: ").strip().title()
#     time.sleep(0.5)
#     player2 = input("🦸‍♂ Player 2, enter your name: ").strip().title()
#     time.sleep(0.5)

#     print(f"\n🔐 {player1}, enter a secret number while {player2} looks away!")
#     secret_number = G1_input_number(f"{player1}, enter a number between 1 and 100: ", 1, 100)
#     guess_limit = G1_input_number(f"🎯 How many attempts does {player2} get? ", 1, 100)

#     print(f"\n📱 Now, pass the device to {player2}!")
#     time.sleep(1.5)

#     print(f"\n⚔ {player2}, your mission: Guess the secret number!")
#     time.sleep(0.25)
#     print(f"🎲 You have {guess_limit} attempts!")
#     time.sleep(1)

#     G1_play_guessing_game(secret_number, guess_limit, player2)

# def G1_replay():
#     response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
#     return response == 'y'

# def G1_main():
#     G1_show_menu()
#     while True:

#         try:
#             choice = int(input("👉 Choose mode (1 or 2): "))
#         except ValueError:
#             print("❌ Invalid input. Please enter 1 or 2.")
#             continue

#         if choice == 1:
#             G1_single_player()
#         elif choice == 2:
#             G1_multiplayer()
#         else:
#             print("❌ Please enter a valid game mode (1 or 2).")
#             continue

#         if not G1_replay():
#             print("\n👋 Thanks for playing! Goodbye!")
#             time.sleep(0.4)
#             break

# ################################

# #syntax hangman 

# hang = [
#     "------  ",
#     "|    |  ",
#     "|    0  ",
#     "|   /|\\",
#     "|   / \\",
#     "|       "
# ]

# def G2_print_hang(x):
#     for i in range(x):
#         print(hang[i])
#         time.sleep(0.075)

# def G2_ask_question(question, options, correct_option):
#     print("\n" + question)
#     for option in options:
#         print(option)
#     while True:
#         try:
#             user_choice = int(input("Enter your option (1-4): "))
#             if 1 <= user_choice <= 4:
#                 break
#             else:
#                 print("Please choose a number between 1 and 4.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#     if user_choice == correct_option:
#         print("Correct!")
#         return True
#     else:
#         print(f"Wrong! The correct answer is: {options[correct_option - 1]}")
#         return False

# def G2_print_score(player_name, score, total):
#     print(f"\nGame Over! {player_name}, your final score: {score}/{total}")

# def G2_run_quiz(questions_subset, player_name):
#     score = 0
#     incorrect = 0
#     for i, (question, options, correct_option) in enumerate(questions_subset):
#         print(f"\nQuestion {i + 1}:")
#         if G2_ask_question(question, options, correct_option):
#             score += 1
#         else:
#             incorrect += 1
#             if incorrect < 6:
#                 G2_print_hang(incorrect)
#             else:
#                 break
#     G2_print_score(player_name, score, len(questions_subset))
#     if incorrect >= 6:
#         G2_print_hang(6)
#         print(f"{player_name} was Hanged")

# def G2_single_player(questions):
#     player_name = input("Player 1, input your name: ")
#     time.sleep(0.1)
#     G2_run_quiz(questions[:10], player_name)
#     G2_play_again()

# def G2_multiplayer(questions):
#     player1 = input("Player 1, input your name: ")
#     player2 = input("Player 2, input your name: ")
#     score1 = score2 = incorrect1 = incorrect2 = 0

#     for i in range(20):
#         player = player1 if i % 2 == 0 else player2
#         print(f"\n{player}, it's your turn!")
#         question, options, correct_option = questions[i]
#         if G2_ask_question(question, options, correct_option):
#             if player == player1:
#                 score1 += 1
#             else:
#                 score2 += 1
#         else:
#             if player == player1:
#                 incorrect1 += 1
#                 print(f"{player1}'s Hangman:")
#                 G2_print_hang(incorrect1)
#                 if incorrect1 >= 6:
#                     print(f"{player1} was Hanged")
#                     break
#             else:
#                 incorrect2 += 1
#                 print(f"{player2}'s Hangman:")
#                 G2_print_hang(incorrect2)
#                 if incorrect2 >= 6:
#                     print(f"{player2} was Hanged")
#                     break
#         print(f"\nCurrent Scores: {player1}: {score1}, {player2}: {score2}")

#     print("\nGame Over! Final Scores:")
#     print(f"{player1}: {score1}/10")
#     print(f"{player2}: {score2}/10")
#     if score1 > score2:
#         print(f"{player1} Wins!")
#     elif score2 > score1:
#         print(f"{player2} Wins!")
#     else:
#         print("It's a tie!")
#     G2_play_again()

# def G2_play_again():
#     while True:
#         choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
#         if choice == "yes":
#             G2_main()
#             break
#         elif choice == "no":
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break
#         else:
#             print("Invalid choice! Please enter 'yes' or 'no'.")

# def G2_main():
#     questions = [
#         ("What will be the output of 'print(3 * 3 ** 2)'?", ["1. 27", "2. 18", "3. 81", "4. 9"], 1),
#         ("Which of the following methods can add an element to a set?", ["1. add()", "2. append()", "3. insert()", "4. extend()"], 1),
#         ("What will be the output of 'print(len({1, 2, 2, 3}))'?", ["1. 4", "2. 3", "3. 2", "4. Error"], 2),
#         ("Which of these is a correct way to create an empty dictionary?", ["1. {}", "2. dict()", "3. {[]}", "4. Both 1 and 2"], 4),
#         ("What is the output of 'print(bool(None))'?", ["1. True", "2. False", "3. None", "4. Error"], 2),
#         ("Which function converts a string to a list of characters?", ["1. list()", "2. split()", "3. tuple()", "4. str()"], 1),
#         ("What is the result of 'print([1, 2, 3] + [4, 5])'?", ["1. [1, 2, 3, 4, 5]", "2. [5, 7, 8]", "3. Error", "4. None"], 1),
#         ("Which operator is used for floor division?", ["1. /", "2. //", "3. %", "4. **"], 2),
#         ("What does 'print(type([]))' return?", ["1. <class 'list'>", "2. <class 'tuple'>", "3. <class 'dict'>", "4. <class 'set'>"], 1),
#         ("How do you access the second element of a list 'x = [10, 20, 30]'?", ["1. x[2]", "2. x(1)", "3. x[1]", "4. x{1}"], 3),
#         ("Which of the following creates a tuple?", ["1. (1,)", "2. (1)", "3. tuple(1, 2)", "4. {1, 2}"], 1),
#         ("What is the output of 'print(10 % 3)'?", ["1. 3", "2. 1", "3. 10", "4. 0"], 2),
#         ("What does 'print(sorted([3, 2, 5, 4]))' return?", ["1. [2, 3, 4, 5]", "2. (2, 3, 4, 5)", "3. {2, 3, 4, 5}", "4. None"], 1),
#         ("Which function returns the total number of elements in a list?", ["1. size()", "2. length()", "3. len()", "4. count()"], 3),
#         ("What does 'range(3)' return?", ["1. [0, 1, 2]", "2. (0, 1, 2)", "3. range object", "4. None"], 3),
#         ("Which keyword is used to define a function in Python?", ["1. function", "2. define", "3. def", "4. fun"], 3),
#         ("What is the output of 'print(type(3.0))'?", ["1. <class 'int'>", "2. <class 'float'>", "3. <class 'complex'>", "4. <class 'str'>"], 2),
#         ("How do you remove an element from a dictionary?", ["1. del dict[key]", "2. dict.remove(key)", "3. dict.pop(key)", "4. Both 1 and 3"], 4),
#         ("Which method is used to remove all elements from a list?", ["1. remove()", "2. clear()", "3. pop()", "4. del()"], 2),
#         ("What will 'print(2 == 2.0)' return?", ["1. True", "2. False", "3. None", "4. Error"], 1),
#         ("Which of the following is a valid variable name in Python?", ["1. 1variable", "2. variable_1", "3. variable-1", "4. variable 1"], 2),
#         ("What is the output of 'print(type({}))'?", ["1. <class 'dict'>", "2. <class 'set'>", "3. <class 'list'>", "4. <class 'tuple'>"], 1),
#         ("Which of the following is used for single-line comments in Python?", ["1. //", "2. <!-- -->", "3. #", "4. /* */"], 3),
#         ("How do you create a list with numbers from 0 to 9 in Python?", ["1. list(range(10))", "2. range(10)", "3. [0:9]", "4. [range(10)]"], 1),
#         ("What is the output of 'print(5 == 5.0)'?", ["1. False", "2. True", "3. Error", "4. None"], 2),
#         ("What is the result of '3 < 4 and 5 > 2'?", ["1. True", "2. False", "3. Error", "4. None"], 1),
#         ("What is the output of 'print(4 ** 0.5)'?", ["1. 2.0", "2. 16", "3. 4", "4. 0"], 1),
#         ("What does 'is' compare in Python?", ["1. Value", "2. Identity", "3. Type", "4. Scope"], 2),
#         ("Which of the following is NOT a valid data type in Python?", ["1. string", "2. list", "3. map", "4. float"], 3),
#         ("What does the 'pass' statement do?", ["1. Skips iteration", "2. Terminates program", "3. Does nothing", "4. Raises an error"], 3),
#         ("Which statement is used to stop a loop in Python?", ["1. stop", "2. break", "3. exit", "4. quit"], 2),
#         ("Which of the following will create a set?", ["1. {1, 2, 3}", "2. [1, 2, 3]", "3. (1, 2, 3)", "4. <1, 2, 3>"], 1),
#         ("What is the keyword to handle exceptions in Python?", ["1. try", "2. check", "3. catch", "4. handle"], 1),
#         ("Which keyword is used to create a class in Python?", ["1. define", "2. function", "3. class", "4. def"], 3),
#         ("What is the result of 'len(\"hello\")'?", ["1. 5", "2. 4", "3. 6", "4. Error"], 1),
#         ("What does 'elif' stand for in Python?", ["1. Else if", "2. Else loop", "3. End if", "4. Else function"], 1),
#         ("How do you write an infinite loop in Python?", ["1. while(True):", "2. for(;;)", "3. while 1", "4. repeat forever"], 1),
#         ("Which of these is used to define a block of code in Python?", ["1. Curly braces", "2. Parentheses", "3. Indentation", "4. Semicolons"], 3),
#         ("Which function gives the Unicode of a character?", ["1. unicode()", "2. char()", "3. ord()", "4. ascii()"], 3),
#         ("What is the output of 'print(\"Hello\"[::-1])'?", ["1. Hello", "2. olleH", "3. Error", "4. hELLO"], 2)
#     ]
    
#     random.shuffle(questions)
#     print("\n🎮 Welcome to the Python Quiz Game! 🎮")
#     time.sleep(0.1)
#     print("The quiz is starting...\n")
#     time.sleep(0.1)
#     while True:
#         mode = input("Enter '1' for Single Player or '2' for Multiplayer: ").strip()
#         if mode == "1":
#             G2_single_player(questions)
#             break
#         elif mode == "2":
#             G2_multiplayer(questions)
#             break
#         else:
#             print("Invalid choice! Please enter '1' or '2'.")

# ################################

# #Rock Paper and Scissors

# def G3_get_move_input(player_name):
#     time.sleep(0.1)
#     move = input(f"{player_name}, enter move (Rock, Paper, Scissor): ").strip().lower()
#     while move not in values:
#         print("Invalid move! Please enter Rock, Paper, or Scissor.")
#         move = input(f"{player_name}, enter move: ").strip().lower()
#     return move

# def G3_decide_winner(p1_move, p2_move):
#     if p1_move == p2_move:
#         return 0
#     elif (p1_move, p2_move) in win_conditions:
#         return 1
#     else:
#         return 2

# def G3_display_score(name1, score1, name2=None, score2=None):
#     if name2:
#         print(f"{name1} has {score1} point(s), {name2} has {score2} point(s)\n")
#     else:
#         print(f"{name1}, you have {score1} point(s)\n")

# def G3_play_single_player():
#     time.sleep(0.2)
#     player_name = input("Player 1, enter your name: ")
#     time.sleep(0.1)
#     rounds = int(input(f"{player_name}, how many rounds would you like to play? "))
#     time.sleep(0.1)
#     print(f"{player_name}, Get ready!\n")
#     time.sleep(0.05)

#     score = 0
#     for round_num in range(1, rounds + 1):
#         print(f"Round {round_num} of {rounds}")
#         time.sleep(0.2)
#         player_move = G3_get_move_input(player_name)
#         computer_move = random.choice(values)
#         time.sleep(0.1)
#         print(f"Computer chose: {computer_move}")

#         result = G3_decide_winner(player_move, computer_move)
#         if result == 0:
#             print("It's a tie!")
#         elif result == 1:
#             print(f"{player_name}, you won this round!")
#             score += 1
#         else:
#             print(f"{player_name}, you lost this round.")

#         G3_display_score(player_name, score)

# def G3_play_multiplayer():
#     player1 = input("Player 1, enter your name: ")
#     player2 = input("Player 2, enter your name: ")
#     rounds = int(input("How many rounds would you like to play? "))
#     print(f"{player1} and {player2}, Get ready!\n")

#     score1 = 0
#     score2 = 0

#     for round_num in range(1, rounds + 1):
#         print(f"Round {round_num} of {rounds}")
#         move1 = G3_get_move_input(player1)
#         move2 = G3_get_move_input(player2)

#         result = G3_decide_winner(move1, move2)
#         if result == 0:
#             print("It's a tie!")
#         elif result == 1:
#             print(f"{player1} won this round!")
#             score1 += 1
#         else:
#             print(f"{player2} won this round!")
#             score2 += 1

#         G3_display_score(player1, score1, player2, score2)

# values = ["rock", "paper", "scissor"]
# win_conditions = {
#     ("rock", "scissor"),
#     ("scissor", "paper"),
#     ("paper", "rock")
# }

# def G3_replay():
#     response = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
#     return response == 'y'

# def G3_main():
#     print("""
#         🎮 Game - Rock Paper Scissors 🎮
#         Choose Mode:
#         1 : Single Player
#         2 : Multiplayer
#         """)
#     while True:
#         try:
#             mode = int(input("Enter the mode number: "))
#             if mode == 1:
#                 G3_play_single_player()
#             elif mode == 2:
#                 G3_play_multiplayer()
#             else:
#                 print("Invalid mode selected. Please enter 1 or 2.")
#                 continue
#         except ValueError:
#             print("!Error! Please enter a number, not letters.")
#             continue

#         if not G3_replay():
#             print("\n👋 Thanks for playing! Goodbye!")
#             time.sleep(0.4)
#             break

# ################################

# #tic tac toe

# def G4_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("\n    1   2   3")
#     for i, row in enumerate(board):
#         prefix = f"{i+1} "
#         if i == 0:
#             prefix += "◤ "
#         elif i == 2:
#             prefix += "◣ "
#         else:
#             prefix += "  "

#         print(f"{prefix}" + " | ".join(row) + (" ◥" if i == 0 else " ◢" if i == 2 else " "))
#         if i < 2:
#             print("  |———————————|")
#     print()

# def G4_check_winner(board, player):
#     win_patterns = (
#         board,
#         [[board[r][c] for r in range(3)] for c in range(3)],
#         [[board[i][i] for i in range(3)]],
#         [[board[i][2 - i] for i in range(3)]]
#     )
#     return any(all(cell == player for cell in line) for group in win_patterns for line in group)

# def G4_get_empty_cells(board):
#     return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def G4_ai_move(board, ai="Θ", player="✕"):
#     def can_win(symbol):
#         for r, c in G4_get_empty_cells(board):
#             board[r][c] = symbol
#             if G4_check_winner(board, symbol):
#                 board[r][c] = " "
#                 return r, c
#             board[r][c] = " "
#         return None

#     return (
#         can_win(ai) or
#         can_win(player) or
#         (1, 1) if board[1][1] == " " else
#         random.choice([c for c in [(0, 0), (0, 2), (2, 0), (2, 2)] if board[c[0]][c[1]] == " "]) or
#         random.choice(G4_get_empty_cells(board))
#     )

# def G4_get_player_move(board, player_symbol, player_num):
#     while True:
#         move = input(f"Player {player_num} ({player_symbol}), enter row and column (1-3, space-separated): ")
#         try:
#             row, col = map(int, move.split())
#             row -= 1
#             col -= 1
#             if (0 <= row < 3) and (0 <= col < 3) and board[row][col] == " ":
#                 return row, col
#             print("Invalid move. Cell is occupied or out of range.")
#         except (ValueError, IndexError):
#             print("Invalid input. Please enter two numbers between 1 and 3.")

# def G4_main():
#     print("\n🎮 Welcome to Tic Tac Toe! 🎮")
#     mode = int(input("""
#         Choose mode: 
#         1 for Single Player 
#         2 for Multiplayer
#         : """).strip())

#     scores = {"Player 1": 0, "Player 2": 0}
#     players = ["✕", "Θ"]

#     while True:
#         board = [[" "]*3 for _ in range(3)]
#         turn = 0

#         while True:
#             G4_print_board(board)
#             current_player = players[turn % 2]

#             if mode == 1 and current_player == "Θ":
#                 time.sleep(0.3)
#                 print("AI is making a move...")
#                 time.sleep(0.5)
#                 row, col = G4_ai_move(board)
#             else:
#                 row, col = G4_get_player_move(board, current_player, turn % 2 + 1)

#             board[row][col] = current_player

#             if G4_check_winner(board, current_player):
#                 G4_print_board(board)
#                 print(f"Player {turn % 2 + 1} ({current_player}) wins!")
#                 if mode == 2:
#                     scores[f"Player {turn % 2 + 1}"] += 3
#                 break

#             if not G4_get_empty_cells(board):
#                 G4_print_board(board)
#                 print("It's a draw!")
#                 break

#             turn += 1

#         if mode == 2:
#             print("\nScoreboard:")
#             for player, score in scores.items():
#                 print(f"{player}: {score}")
#             print()

#         if input("Wanna play again? (yes/no): ").strip().lower() != "yes":
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break


# ################################

# # 2048

# # Game constants
# SIZE = 4
# MOVES = {'W': 'up', 'A': 'left', 'S': 'down', 'D': 'right'}

# class Game2048:
#     def __init__(self):
#         self.board = [[0] * SIZE for _ in range(SIZE)]
#         self.score = 0
#         self.high_score = 0
#         self.game_over = False
#         self.add_new_tile()
#         self.add_new_tile()
    
#     def add_new_tile(self):
#         empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
#         if empty_cells:
#             r, c = random.choice(empty_cells)
#             self.board[r][c] = 2 if random.random() < 0.8 else 4
    
#     def compress(self, row):
#         new_row = [num for num in row if num != 0]
#         new_row += [0] * (SIZE - len(new_row))
#         return new_row
    
#     def merge(self, row):
#         new_row = row.copy()
#         for i in range(SIZE - 1):
#             if new_row[i] == new_row[i + 1] and new_row[i] != 0:
#                 new_row[i] *= 2
#                 self.score += new_row[i]  
#                 new_row[i + 1] = 0
#         return new_row
    
#     def move_left(self):
#         new_board = []
#         moved = False
#         for row in self.board:
#             compressed = self.compress(row)
#             merged = self.merge(compressed)
#             new_row = self.compress(merged)
#             new_board.append(new_row)
#             if row != new_row:
#                 moved = True
#         self.board = new_board
#         return moved
    
#     def move_right(self):
#         self.board = [row[::-1] for row in self.board]
#         moved = self.move_left()
#         self.board = [row[::-1] for row in self.board]
#         return moved
    
#     def move_up(self):
#         self.board = [list(col) for col in zip(*self.board)]
#         moved = self.move_left()
#         self.board = [list(col) for col in zip(*self.board)]
#         return moved
    
#     def move_down(self):
#         self.board = [list(col) for col in zip(*self.board)]
#         moved = self.move_right()
#         self.board = [list(col) for col in zip(*self.board)]
#         return moved
    
#     def check_game_over(self):
#         if any(0 in row for row in self.board):
#             return False
        
#         for r in range(SIZE):
#             for c in range(SIZE - 1):
#                 if self.board[r][c] == self.board[r][c + 1]:
#                     return False
        
#         for r in range(SIZE - 1):
#             for c in range(SIZE):
#                 if self.board[r][c] == self.board[r + 1][c]:
#                     return False
        
#         return True
    
#     def make_move(self, direction):
#         if self.game_over:
#             return False
        
#         moved = False
#         if direction == 'up':
#             moved = self.move_up()
#         elif direction == 'down':
#             moved = self.move_down()
#         elif direction == 'left':
#             moved = self.move_left()
#         elif direction == 'right':
#             moved = self.move_right()
        
#         # if moved:
#         self.add_new_tile()
#         self.high_score = max(self.score, self.high_score)
#         if self.check_game_over():
#             self.game_over = True
        
#         return moved
    
#     def display(self):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print(f"Score: {self.score} | High Score: {self.high_score}")
#         print("=" * (SIZE * 6))
        
#         for row in self.board:
#             print(" | ".join(f"{num:^4}" if num != 0 else "    " for num in row))
#             print("-" * (SIZE * 6))
        
#         if self.game_over:
#             print("\nGAME OVER! No more moves left.")

# def G5_main():
#     game = Game2048()
    
#     while True:
#         game.display()
        
#         move = input("Move (WASD, Q to quit): ").strip().upper()
        
#         if move == 'Q':
#             print("Thanks for playing!")
#             time.sleep(0.4)
#             break
        
#         if move in MOVES:
#             game.make_move(MOVES[move])
#         else:
#             print("Invalid move! Use W (up), A (left), S (down), D (right) or Q to quit.")
#             input("Press Enter to continue...")


# ################################

# #4 in a row

# def G6_create_board():
#     return np.zeros((6, 7), dtype=int)

# def G6_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(" \n  > 1   2   3   4   5   6   7 <")
#     print("  |———————————————————————————|")
#     arr = np.flip(board, 0)
#     for i, row in enumerate(arr):
#         row_str = "| " + " | ".join(map(str, row)) + " |"
#         time.sleep(0.025)
#         print(f"{i+1} {row_str}")

# def G6_is_valid_move(board, col):
#     return board[5][col] == 0

# def G6_get_next_open_row(board, col):
#     for r in range(6):
#         if board[r][col] == 0:
#             return r

# def G6_drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def G6_check_win(board, piece):
#     for c in range(4):
#         for r in range(6):
#             if all(board[r, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(7):
#         for r in range(3):
#             if all(board[r + i, c] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3):
#             if all(board[r + i, c + i] == piece for i in range(4)):
#                 return True
#     for c in range(4):
#         for r in range(3, 6):
#             if all(board[r - i, c + i] == piece for i in range(4)):
#                 return True
#     return False

# def G6_ai_move(board):
#     valid_moves = [c for c in range(7) if G6_is_valid_move(board, c)]
    
#     def can_win(piece):
#         for c in valid_moves:
#             row = G6_get_next_open_row(board, c)
#             if row is not None:
#                 G6_drop_piece(board, row, c, piece)
#                 if G6_check_win(board, piece):
#                     board[row][c] = 0
#                     return c
#                 board[row][c] = 0
#         return None
    
#     ai_piece = 2
#     player_piece = 1
#     move = can_win(ai_piece)
#     if move is not None:
#         return move
    
#     move = can_win(player_piece)
#     if move is not None:
#         return move
    
#     return random.choice(valid_moves)

# def G6_get_valid_column():
#     while True:
#         try:
#             time.sleep(0.25)
#             cx = int(input("\nPlayer 1, choose a column (1-7): "))
#             if cx == -1:
#                 print("\nThank you for playing\n")
#                 time.sleep(0.4)
#                 exit()
#             if 1 <= cx <= 7:
#                 return cx - 1
#             else:
#                 print("Invalid column! Please choose a number between 1 and 7.")
#         except ValueError:
#             print("Invalid input! Please enter a number.")

# def G6_is_board_full(board):
#     return np.all(board != 0)

# def G6_main():
#     time.sleep(0.1)
#     print("\nWelcome to 4 in a Row!")
#     time.sleep(0.1)
#     mode = input("Enter '1' for single-player or '2' for multiplayer: ")
#     board = G6_create_board()
#     game_over = False
#     turn = 0
#     scores = {1: 0, 2: 0} if mode == '2' else None
    
#     while not game_over:
#         G6_print_board(board)
#         if turn % 2 == 0:
#             col = G6_get_valid_column()
#         else:
#             if mode == '1':
#                 col = G6_ai_move(board)
#                 print("\n")
#                 time.sleep(0.6)
#                 print(f"AI is making a move...")
#                 time.sleep(1.1)
#             else:
#                 col = G6_get_valid_column()
        
#         if G6_is_valid_move(board, col):
#             row = G6_get_next_open_row(board, col)
#             G6_drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
#             if G6_check_win(board, 1 if turn % 2 == 0 else 2):
#                 time.sleep(0.1)
#                 G6_print_board(board)
#                 print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
#                 if mode == '2':
#                     scores[1 if turn % 2 == 0 else 2] += 1
#                 game_over = True
                
#         else:
#             print("\nInvalid move! Try again.")
#             continue
        
#         turn += 1
#         if G6_is_board_full(board):
#             print("\nIt's a tie!")
#             game_over = True
        
#         if game_over and mode == '1':
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = G6_create_board()
#                 game_over = False
#                 turn = 0

#         if game_over and mode == '2':
#             print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
#             replay = input("\nPlay again? (yes/no): ")
#             if replay.lower() == 'yes':
#                 board = G6_create_board()
#                 scores = {1: 0, 2: 0}  
#                 game_over = False
#                 turn = 0

# ################################

# # sudoku

# def G7_print_board(board):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("------+-------+------")
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")
#         print()

# def G7_find_empty(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return (i, j)
#     return None

# def G7_is_valid(board, num, pos):
#     row, col = pos
#     for i in range(9):
#         if board[row][i] == num and col != i:
#             return False
#         if board[i][col] == num and row != i:
#             return False
#     box_x = col // 3
#     box_y = row // 3
#     for i in range(box_y * 3, box_y * 3 + 3):
#         for j in range(box_x * 3, box_x * 3 + 3):
#             if board[i][j] == num and (i, j) != pos:
#                 return False
#     return True

# def G7_generate_sudoku(difficulty):
#     board = [[0 for _ in range(9)] for _ in range(9)]
#     for box in range(0, 9, 3):
#         nums = list(range(1, 10))
#         random.shuffle(nums)
#         for i in range(3):
#             for j in range(3):
#                 board[box + i][box + j] = nums.pop()
#     G7_solve_board(board)
#     cells_to_remove = min(max(difficulty, 30), 60)
#     for _ in range(cells_to_remove):
#         row, col = random.randint(0, 8), random.randint(0, 8)
#         while board[row][col] == 0:
#             row, col = random.randint(0, 8), random.randint(0, 8)
#         board[row][col] = 0
#     return board

# def G7_solve_board(board):
#     find = G7_find_empty(board)
#     if not find:
#         return True
#     row, col = find
#     for num in range(1, 10):
#         if G7_is_valid(board, num, (row, col)):
#             board[row][col] = num
#             if G7_solve_board(board):
#                 return True
#             board[row][col] = 0
#     return False

# def G7_input_board():
#     print("\nEnter your Sudoku board row by row.")
#     print("Use numbers 1-9 for filled cells and 0 or . for empty cells.")
#     print("Separate numbers with spaces.")
#     board = []
#     for i in range(9):
#         while True:
#             row_input = input(f"Row {i+1}: ").replace('.', '0')
#             parts = row_input.split()
#             if len(parts) != 9:
#                 print("Please enter exactly 9 values.")
#                 continue
#             try:
#                 row = [int(x) if x.isdigit() else -1 for x in parts]
#                 if any(num < 0 or num > 9 for num in row):
#                     print("Numbers must be between 0 and 9.")
#                     continue
#                 board.append(row)
#                 break
#             except Exception:
#                 print("Invalid input. Please enter numbers only.")
#     return board

# def G7_get_fixed_cells(board):
#     return {(i, j) for i in range(9) for j in range(9) if board[i][j] != 0}

# def G7_play_move(board, fixed_cells):
#     while True:
#         move = input("Enter your move (row col num), 'hint' or 'q' to quit: ").lower()
#         if move == 'q':
#             return False
#         if move == 'hint':
#             G7_give_hint(board)
#             continue
#         parts = move.split()
#         if len(parts) != 3 or not all(part.isdigit() for part in parts):
#             print("Please enter row, column, and number as integers separated by spaces.")
#             continue
#         row, col, num = map(int, parts)
#         if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
#             print("Row, column, and number must be between 1-9.")
#             continue
#         row -= 1
#         col -= 1
#         if (row, col) in fixed_cells:
#             print("You can't change the original puzzle numbers!")
#             continue
#         if board[row][col] != 0:
#             print("That cell is already filled!")
#             continue
#         if G7_is_valid(board, num, (row, col)):
#             board[row][col] = num
#             return True
#         else:
#             print("Invalid move! That number conflicts with existing numbers.")

# def G7_give_hint(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 for num in range(1, 10):
#                     if G7_is_valid(board, num, (i, j)):
#                         print(f"Try placing in row {i+1}, column {j+1} : {num} ")
#                         return
#     print("No hints available.")

# def G7_check_complete(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return False
#             temp = board[i][j]
#             board[i][j] = 0
#             if not G7_is_valid(board, temp, (i, j)):
#                 board[i][j] = temp
#                 return False
#             board[i][j] = temp
#     return True

# def G7_main():
#     print("Welcome to Sudoku!")
#     print("Enter moves as 'row col number' (e.g., '3 5 7' to put 7 in row 3, column 5)")
#     print("Enter 'hint' for a hint or 'q' to quit at any time\n")

#     while True:
#         choice = input("Choose an option:\n1. Play a random puzzle\n2. Input your own puzzle\n> ").strip()
#         if choice == '1':
#             difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
#             difficulties = {'easy': (30, 40), 'medium': (41, 49), 'hard': (50, 60)}
#             empty_range = difficulties.get(difficulty, (41, 49))
#             empty_cells = random.randint(*empty_range)
#             board = G7_generate_sudoku(empty_cells)
#             break
#         elif choice == '2':
#             board = G7_input_board()
#             solve = input("Would you like to auto-solve your puzzle? (y/n): ").lower()
#             if solve == 'y':
#                 if G7_solve_board(board):
#                     print("\nSolved board:")
#                     G7_print_board(board)
#                 else:
#                     print("This puzzle has no valid solution.")
#                 return
#             break
#         else:
#             print("Invalid choice. Please enter 1 or 2.")

#     fixed_cells = G7_get_fixed_cells(board)
#     start_time = time.time()

#     while True:
#         print("\nCurrent board:")
#         G7_print_board(board)

#         if G7_check_complete(board):
#             elapsed = time.time() - start_time
#             mins, secs = divmod(int(elapsed), 60)
#             print(f"\nCongratulations! You solved the Sudoku in {mins} minutes and {secs} seconds.")
#             break

#         if not G7_play_move(board, fixed_cells):
#             print("\nThanks for playing!")
#             time.sleep(0.4)
#             break

#     print("\nFinal board:")
#     G7_print_board(board)


# ################################

# #Python syntax checker

# task_bank = [
#     ("Create a list and append three numbers to it.",
#      lambda lv: isinstance(lv.get('my_list'), list) and len(lv['my_list']) >= 3),

#     ("Create a tuple and access an element from it.",
#      lambda lv: isinstance(lv.get('my_tuple'), tuple)),

#     ("Create a dictionary and retrieve a value using a key.",
#      lambda lv: isinstance(lv.get('my_dict'), dict) and bool(lv['my_dict'])),

#     ("Import the math module and use the sqrt function.",
#      lambda lv: 'math' in lv and callable(lv['math'].sqrt)),

#     ("Create a set and add/remove elements.",
#      lambda lv: isinstance(lv.get('my_set'), set)),

#     ("Define a function that returns the square of a number.",
#      lambda lv: callable(lv.get('square')) and lv  == 4),

#     ("Create a list of strings and loop through it.",
#      lambda lv: isinstance(lv.get('str_list'), list) and all(isinstance(x, str) for x in lv['str_list'])),

#     ("Use a tuple to store coordinates and print them.",
#      lambda lv: isinstance(lv.get('coords'), tuple) and len(lv['coords']) == 2),

#     ("Create a dictionary of student names and grades using a for loop.",
#      lambda lv: isinstance(lv.get('grades'), dict)),

#     ("Use a set to store unique numbers and display them.",
#      lambda lv: isinstance(lv.get('unique_numbers'), set)),

#     ("Import the random module and generate a random number.",
#      lambda lv: 'random' in lv),

#     ("Define a function to check if a number is even.",
#      lambda lv: callable(lv.get('is_even')) and lv  is True),

#     ("Create a nested list and access an inner element.",
#      lambda lv: isinstance(lv.get('nested_list'), list)),

#     ("Create a dictionary of fruits and their prices, then print the most expensive fruit.",
#      lambda lv: isinstance(lv.get('fruits'), dict)),

#     ("Create a list and use pop() to remove an element.",
#      lambda lv: isinstance(lv.get('popped_list'), list)),

#     ("Define a function to return the length of a string.",
#      lambda lv: callable(lv.get('strlen')) and lv['strlen']("abc") == 3),

#     ("Make a dictionary and iterate through its keys.",
#      lambda lv: isinstance(lv.get('my_dict'), dict)),

#     ("Use a tuple to store and print 3 values.",
#      lambda lv: isinstance(lv.get('vals'), tuple) and len(lv['vals']) == 3),

#     ("Create a set and check for membership.",
#      lambda lv: isinstance(lv.get('my_set'), set)),

#     ("Check if a substring exists in a string using 'in'.",
#      lambda lv: isinstance(lv.get('text'), str) and 'a' in lv['text']),

#     ("Replace characters in a string using replace().",
#      lambda lv: isinstance(lv.get('text'), str) and 'x' not in lv['text']),

#     ("Use regex to find digits in a string.",
#      lambda lv: 're' in lv and lv.get('digits') is not None and isinstance(lv['digits'], list)),
# ]

# def G8_check_line_syntax(code_line):
#     try:
#         compile(code_line, "<line>", "exec")
#         return True
#     except SyntaxError:
#         return False

# def G8_main():
#     print("🎮 Welcome to Python Syntax Battle!")
#     start_game = input("Do you want to play? Enter y to start: ").strip().lower()
#     if start_game != 'y':
#         print("👋 Exiting game. Maybe next time!")
#         return

#     players = ["Player 1", "Player 2"]
#     points = {player: 0 for player in players}
#     turn = 0

#     while True:
#         task_description, validator = random.choice(task_bank)
#         print(f"\n📝 Task: {task_description}")

#         code_lines = []
#         sub_turn = 0

#         while True:
#             active_player = players[(turn + sub_turn) % 2]
#             print(f"\n✏ {active_player}'s turn to enter a line of code:")
#             code_line = input(">>> ").rstrip()

#             if G8_check_line_syntax(code_line):
#                 print("✅ Line is syntactically correct.")
#                 code_lines.append(code_line)
#                 points[active_player] += 1
#             else:
#                 print("❌ Syntax error! Opportunity passes to the other player.")
#                 other_player = players[(turn + sub_turn + 1) % 2]
#                 print(f"✏ {other_player}, your chance to correct the line:")
#                 code_line_alt = input(">>> ").rstrip()
#                 if G8_check_line_syntax(code_line_alt):
#                     print("✅ Corrected line accepted.")
#                     code_lines.append(code_line_alt)
#                     points[other_player] += 1
#                 else:
#                     print("❌ Still a syntax error! No line added.")

#             compile_now = input("⚙ Compile full code and validate task? (y/n): ").lower()
#             if compile_now == 'y':
#                 full_code = "\n".join(code_lines)
#                 try:
#                     compiled_code = compile(full_code, "<game>", "exec")
#                     local_vars = {}
#                     exec(compiled_code, {"re": re, "random": random}, local_vars)
#                     if validator(local_vars):
#                         print("✅ Task completed successfully! Moving to next round.")
#                     else:
#                         print("❌ Code ran, but task not completed correctly.")
#                         print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
#                     break
#                 except Exception:
#                     print("❌ Compilation or Runtime error!")
#                     print(traceback.format_exc())
#                     print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
#                     break
#             sub_turn += 1

#         print("\n📊 Current Points:")
#         for player, score in points.items():
#             print(f"   {player}: {score} points")

#         play_again = input("\n🔁 Continue to next round? (y/n): ").lower()
#         if play_again != 'y':
#             print("\n🎉 Final Scores:")
#             for player, score in points.items():
#                 print(f"   {player}: {score} points")
#             print("👋 Thanks for playing!")
#             break

#         turn += 1

# ################################

# def loading_bar():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting...  "):        # NEW
#         time.sleep(0.03)

# def show_menu():
#     # loading_bar()
#     print("""
# 🎮 8-Bit Games - Virtual Arcade 🎮
# Choose a game to play or 'q' to quit:

# 1 : Guess the Number
# 2 : Hangman Quiz
# 3 : Rock, Paper, Scissors
# 4 : Tic Tac Toe
# 5 : 2048
# 6 : 4 in a Row
# 7 : Sudoku
# 8 : Python Syntax Checker
# """)



# def run():
#     while True:
#         show_menu()
#         choice = input('> ').strip().lower()
        
#         if choice == 'q':
#             print("Thanks for playing! Goodbye!")
#             break
#         elif choice == '1':
#             loading_bar()
#             G1_main()
#         elif choice == '2':
#             loading_bar()
#             G2_main()
#         elif choice == '3':
#             loading_bar()
#             G3_main()
#         elif choice == '4':
#             loading_bar()
#             G4_main()
#         elif choice == '5':
#             loading_bar()
#             G5_main()
#         elif choice == '6':
#             loading_bar()
#             G6_main()
#         elif choice == '7':
#             loading_bar()
#             G7_main()
#         elif choice == '8':
#             loading_bar()
#             G8_main()
#         else:
#             print("Invalid choice. Please select a valid option.")

# if __name__ == "__main__":
#     run()

# keys = {'Mumbai','Bangalore','Chennai','Coimbatore'}
# dictionary =dict.fromkeys(keys)
# print(dictionary)
# dictionary=dict.fromkeys(keys,'India')
# print(dictionary)

# a=( 2* 3 /4 +4/4 +8-2+5/8)

s="aeiou"

# # print(s.index("b"))

# my_strings = ['a', 'b','c', 'd', 'e']
# my_numbers = [1,2, 3, 4]
# # results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
# # print(results)
# res=zip(my_strings, my_numbers)
# print(list(res))
print(s.isdigit())
