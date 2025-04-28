#Python syntax checker

import traceback
import random
import re

task_bank = [
    ("Create a list and append three numbers to it.",
     lambda lv: isinstance(lv.get('my_list'), list) and len(lv['my_list']) >= 3),

    ("Create a tuple and access an element from it.",
     lambda lv: isinstance(lv.get('my_tuple'), tuple)),

    ("Create a dictionary and retrieve a value using a key.",
     lambda lv: isinstance(lv.get('my_dict'), dict) and bool(lv['my_dict'])),

    ("Import the math module and use the sqrt function.",
     lambda lv: 'math' in lv and callable(lv['math'].sqrt)),

    ("Create a set and add/remove elements.",
     lambda lv: isinstance(lv.get('my_set'), set)),

    ("Define a function that returns the square of a number.",
     lambda lv: callable(lv.get('square')) and lv  == 4),

    ("Create a list of strings and loop through it.",
     lambda lv: isinstance(lv.get('str_list'), list) and all(isinstance(x, str) for x in lv['str_list'])),

    ("Use a tuple to store coordinates and print them.",
     lambda lv: isinstance(lv.get('coords'), tuple) and len(lv['coords']) == 2),

    ("Create a dictionary of student names and grades using a for loop.",
     lambda lv: isinstance(lv.get('grades'), dict)),

    ("Use a set to store unique numbers and display them.",
     lambda lv: isinstance(lv.get('unique_numbers'), set)),

    ("Import the random module and generate a random number.",
     lambda lv: 'random' in lv),

    ("Define a function to check if a number is even.",
     lambda lv: callable(lv.get('is_even')) and lv  is True),

    ("Create a nested list and access an inner element.",
     lambda lv: isinstance(lv.get('nested_list'), list)),

    ("Create a dictionary of fruits and their prices, then print the most expensive fruit.",
     lambda lv: isinstance(lv.get('fruits'), dict)),

    ("Create a list and use pop() to remove an element.",
     lambda lv: isinstance(lv.get('popped_list'), list)),

    ("Define a function to return the length of a string.",
     lambda lv: callable(lv.get('strlen')) and lv['strlen']("abc") == 3),

    ("Make a dictionary and iterate through its keys.",
     lambda lv: isinstance(lv.get('my_dict'), dict)),

    ("Use a tuple to store and print 3 values.",
     lambda lv: isinstance(lv.get('vals'), tuple) and len(lv['vals']) == 3),

    ("Create a set and check for membership.",
     lambda lv: isinstance(lv.get('my_set'), set)),

    ("Check if a substring exists in a string using 'in'.",
     lambda lv: isinstance(lv.get('text'), str) and 'a' in lv['text']),

    ("Replace characters in a string using replace().",
     lambda lv: isinstance(lv.get('text'), str) and 'x' not in lv['text']),

    ("Use regex to find digits in a string.",
     lambda lv: 're' in lv and lv.get('digits') is not None and isinstance(lv['digits'], list)),
]

def check_line_syntax(code_line):
    try:
        compile(code_line, "<line>", "exec")
        return True
    except SyntaxError:
        return False

def play_game():
    print("🎮 Welcome to Python Syntax Battle!")
    start_game = input("Do you want to play? Enter y to start: ").strip().lower()
    if start_game != 'y':
        print("👋 Exiting game. Maybe next time!")
        return

    players = ["Player 1", "Player 2"]
    points = {player: 0 for player in players}
    turn = 0

    while True:
        task_description, validator = random.choice(task_bank)
        print(f"\n📝 Task: {task_description}")

        code_lines = []
        sub_turn = 0

        while True:
            active_player = players[(turn + sub_turn) % 2]
            print(f"\n✏ {active_player}'s turn to enter a line of code:")
            code_line = input(">>> ").rstrip()

            if check_line_syntax(code_line):
                print("✅ Line is syntactically correct.")
                code_lines.append(code_line)
                points[active_player] += 1
            else:
                print("❌ Syntax error! Opportunity passes to the other player.")
                other_player = players[(turn + sub_turn + 1) % 2]
                print(f"✏ {other_player}, your chance to correct the line:")
                code_line_alt = input(">>> ").rstrip()
                if check_line_syntax(code_line_alt):
                    print("✅ Corrected line accepted.")
                    code_lines.append(code_line_alt)
                    points[other_player] += 1
                else:
                    print("❌ Still a syntax error! No line added.")

            compile_now = input("⚙ Compile full code and validate task? (y/n): ").lower()
            if compile_now == 'y':
                full_code = "\n".join(code_lines)
                try:
                    compiled_code = compile(full_code, "<game>", "exec")
                    local_vars = {}
                    exec(compiled_code, {"re": re, "random": random}, local_vars)
                    if validator(local_vars):
                        print("✅ Task completed successfully! Moving to next round.")
                    else:
                        print("❌ Code ran, but task not completed correctly.")
                        print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
                    break
                except Exception:
                    print("❌ Compilation or Runtime error!")
                    print(traceback.format_exc())
                    print(f"🏆 {players[(turn + sub_turn + 1) % 2]} wins this round!")
                    break
            sub_turn += 1

        print("\n📊 Current Points:")
        for player, score in points.items():
            print(f"   {player}: {score} points")

        play_again = input("\n🔁 Continue to next round? (y/n): ").lower()
        if play_again != 'y':
            print("\n🎉 Final Scores:")
            for player, score in points.items():
                print(f"   {player}: {score} points")
            print("👋 Thanks for playing!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()