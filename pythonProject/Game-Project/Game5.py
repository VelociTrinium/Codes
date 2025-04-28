# 2048

import random
import os
# from collections import defaultdict
import time

# Game constants
SIZE = 4
MOVES = {'W': 'up', 'A': 'left', 'S': 'down', 'D': 'right'}

class Game2048:
    def __init__(self):
        self.board = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.add_new_tile()
        self.add_new_tile()
    
    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.8 else 4
    
    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (SIZE - len(new_row))
        return new_row
    
    def merge(self, row):
        new_row = row.copy()
        for i in range(SIZE - 1):
            if new_row[i] == new_row[i + 1] and new_row[i] != 0:
                new_row[i] *= 2
                self.score += new_row[i]  
                new_row[i + 1] = 0
        return new_row
    
    def move_left(self):
        new_board = []
        moved = False
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)
            new_board.append(new_row)
            if row != new_row:
                moved = True
        self.board = new_board
        return moved
    
    def move_right(self):
        self.board = [row[::-1] for row in self.board]
        moved = self.move_left()
        self.board = [row[::-1] for row in self.board]
        return moved
    
    def move_up(self):
        self.board = [list(col) for col in zip(*self.board)]
        moved = self.move_left()
        self.board = [list(col) for col in zip(*self.board)]
        return moved
    
    def move_down(self):
        self.board = [list(col) for col in zip(*self.board)]
        moved = self.move_right()
        self.board = [list(col) for col in zip(*self.board)]
        return moved
    
    def check_game_over(self):
        if any(0 in row for row in self.board):
            return False
        
        for r in range(SIZE):
            for c in range(SIZE - 1):
                if self.board[r][c] == self.board[r][c + 1]:
                    return False
        
        for r in range(SIZE - 1):
            for c in range(SIZE):
                if self.board[r][c] == self.board[r + 1][c]:
                    return False
        
        return True
    
    def make_move(self, direction):
        if self.game_over:
            return False
        
        moved = False
        if direction == 'up':
            moved = self.move_up()
        elif direction == 'down':
            moved = self.move_down()
        elif direction == 'left':
            moved = self.move_left()
        elif direction == 'right':
            moved = self.move_right()
        
        # if moved:
        self.add_new_tile()
        self.high_score = max(self.score, self.high_score)
        if self.check_game_over():
            self.game_over = True
        
        return moved
    
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score} | High Score: {self.high_score}")
        print("=" * (SIZE * 6))
        
        for row in self.board:
            print(" | ".join(f"{num:^4}" if num != 0 else "    " for num in row))
            print("-" * (SIZE * 6))
        
        if self.game_over:
            print("\nGAME OVER! No more moves left.")

def main():
    game = Game2048()
    
    while True:
        game.display()
        
        move = input("Move (WASD, Q to quit): ").strip().upper()
        
        if move == 'Q':
            print("Thanks for playing!")
            time.sleep(0.4)
            break
        
        if move in MOVES:
            game.make_move(MOVES[move])
        else:
            print("Invalid move! Use W (up), A (left), S (down), D (right) or Q to quit.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()