#4 in a row

import numpy as np
import random
import time
import os

def create_board():
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" \n  > 1   2   3   4   5   6   7 <")
    print("  |———————————————————————————|")
    arr = np.flip(board, 0)
    for i, row in enumerate(arr):
        row_str = "| " + " | ".join(map(str, row)) + " |"
        time.sleep(0.025)
        print(f"{i+1} {row_str}")

def is_valid_move(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def check_win(board, piece):
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

def ai_move(board):
    valid_moves = [c for c in range(7) if is_valid_move(board, c)]
    
    def can_win(piece):
        for c in valid_moves:
            row = get_next_open_row(board, c)
            if row is not None:
                drop_piece(board, row, c, piece)
                if check_win(board, piece):
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

def get_valid_column():
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

def is_board_full(board):
    return np.all(board != 0)

def play_game():
    time.sleep(0.1)
    print("\nWelcome to 4 in a Row!")
    time.sleep(0.1)
    mode = input("Enter '1' for single-player or '2' for multiplayer: ")
    board = create_board()
    game_over = False
    turn = 0
    scores = {1: 0, 2: 0} if mode == '2' else None
    
    while not game_over:
        print_board(board)
        if turn % 2 == 0:
            col = get_valid_column()
        else:
            if mode == '1':
                col = ai_move(board)
                print("\n")
                time.sleep(0.6)
                print(f"AI is making a move...")
                time.sleep(1.1)
            else:
                col = get_valid_column()
        
        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1 if turn % 2 == 0 else 2)
            
            if check_win(board, 1 if turn % 2 == 0 else 2):
                time.sleep(0.1)
                print_board(board)
                print(f"\nPlayer {1 if turn % 2 == 0 else 2} wins!")
                if mode == '2':
                    scores[1 if turn % 2 == 0 else 2] += 1
                game_over = True
                
        else:
            print("\nInvalid move! Try again.")
            continue
        
        turn += 1
        if is_board_full(board):
            print("\nIt's a tie!")
            game_over = True
        
        if game_over and mode == '1':
            replay = input("\nPlay again? (yes/no): ")
            if replay.lower() == 'yes':
                board = create_board()
                game_over = False
                turn = 0

        if game_over and mode == '2':
            print(f"\nScoreboard: Player 1 - {scores[1]}, Player 2 - {scores[2]}")
            replay = input("\nPlay again? (yes/no): ")
            if replay.lower() == 'yes':
                board = create_board()
                scores = {1: 0, 2: 0}  
                game_over = False
                turn = 0

# play_game()
if __name__ == "__main__":
    play_game()