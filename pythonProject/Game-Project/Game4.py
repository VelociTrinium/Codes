#tic tac toe //bugtest

import time
import random
import os

def print_board(board):
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

def check_winner(board, player):
    win_patterns = (
        board,
        [[board[r][c] for r in range(3)] for c in range(3)],
        [[board[i][i] for i in range(3)]],
        [[board[i][2 - i] for i in range(3)]]
    )
    return any(all(cell == player for cell in line) for group in win_patterns for line in group)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# def ai_move(board, ai="Θ", player="✕"):
#     def can_win(symbol):
#         for r, c in get_empty_cells(board):
#             board[r][c] = symbol
#             if check_winner(board, symbol):
#                 board[r][c] = " "
#                 return r, c
#             board[r][c] = " "
#         return None

#     return (
#         can_win(ai) or
#         can_win(player) or
#         (1, 1) if board[1][1] == " " else
#         random.choice([c for c in [(0, 0), (0, 2), (2, 0), (2, 2)] if board[c[0]][c[1]] == " "]) or random.choice(get_empty_cells(board))
#     )
def ai_move(board):
    empty_cells = get_empty_cells(board)
    
    def can_win(player):
        for r, c in empty_cells:
            board[r][c] = player
            if check_winner(board, player):
                board[r][c] = " "
                return r, c
            board[r][c] = " "
        return None

    ai_symbol = "Θ"
    player_symbol = "✕"
    best_move = can_win(ai_symbol)
    if best_move:
        return best_move

    best_move = can_win(player_symbol)
    if best_move:
        return best_move

    if (1, 1) in empty_cells:
        return 1, 1

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [c for c in corners if c in empty_cells]
    if available_corners:
        return random.choice(available_corners)

    return random.choice(empty_cells)

def get_player_move(board, player_symbol, player_num):
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

def tic_tac_toe():
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
            print_board(board)
            current_player = players[turn % 2]

            if mode == 1 and current_player == "Θ":
                time.sleep(0.3)
                print("AI is making a move...")
                time.sleep(0.5)
                row, col = ai_move(board)
            else:
                row, col = get_player_move(board, current_player, turn % 2 + 1)

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {turn % 2 + 1} ({current_player}) wins!")
                if mode == 2:
                    scores[f"Player {turn % 2 + 1}"] += 3
                break

            if not get_empty_cells(board):
                print_board(board)
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

if __name__ == "__main__":
    tic_tac_toe()


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