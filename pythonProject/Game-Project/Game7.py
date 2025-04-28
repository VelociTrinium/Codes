# sudoku

import random
import time
import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(str(board[i][j]) if board[i][j] != 0 else ".", end=" ")
        print()

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
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

def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[box + i][box + j] = nums.pop()
    solve_board(board)
    cells_to_remove = min(max(difficulty, 30), 60)
    for _ in range(cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def solve_board(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] = 0
    return False

def input_board():
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

def get_fixed_cells(board):
    return {(i, j) for i in range(9) for j in range(9) if board[i][j] != 0}

def play_move(board, fixed_cells):
    while True:
        move = input("Enter your move (row col num), 'hint' or 'q' to quit: ").lower()
        if move == 'q':
            return False
        if move == 'hint':
            give_hint(board)
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
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            return True
        else:
            print("Invalid move! That number conflicts with existing numbers.")

def give_hint(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        print(f"Try placing in row {i+1}, column {j+1} : {num} ")
                        return
    print("No hints available.")

def check_complete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
            temp = board[i][j]
            board[i][j] = 0
            if not is_valid(board, temp, (i, j)):
                board[i][j] = temp
                return False
            board[i][j] = temp
    return True

def play_sudoku():
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
            board = generate_sudoku(empty_cells)
            break
        elif choice == '2':
            board = input_board()
            solve = input("Would you like to auto-solve your puzzle? (y/n): ").lower()
            if solve == 'y':
                if solve_board(board):
                    print("\nSolved board:")
                    print_board(board)
                else:
                    print("This puzzle has no valid solution.")
                return
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    fixed_cells = get_fixed_cells(board)
    start_time = time.time()

    while True:
        print("\nCurrent board:")
        print_board(board)

        if check_complete(board):
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            print(f"\nCongratulations! You solved the Sudoku in {mins} minutes and {secs} seconds.")
            break

        if not play_move(board, fixed_cells):
            print("\nThanks for playing!")
            time.sleep(0.4)
            break

    print("\nFinal board:")
    print_board(board)

if __name__ == "__main__":
    play_sudoku()