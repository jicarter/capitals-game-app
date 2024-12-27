print("Debugging: main.py is starting...")
from api import fetch_next_game
from display import display_game_gui
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
print("Debugging: Imports completed successfully")

def main():
    print("main.py loaded")
    print("Starting main function...")
    try:
        print("Fetching next game...")
        next_game = fetch_next_game()
        print(f"Fetched next game: {next_game}")
        
        if next_game:
            print("Displaying the game in GUI...")
            display_game_gui(next_game)
        else:
            print("No upcoming games found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")