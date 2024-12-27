from display import display_countdown_gui
from datetime import datetime, timezone

# Define the next season start date
NEXT_SEASON_START = datetime(2025, 10, 8, tzinfo=timezone.utc)

def main():
    # Calculate the number of days until the next season starts
    days_until_next_season = (NEXT_SEASON_START - datetime.now(timezone.utc)).days
    print(f"Days until next season: {days_until_next_season}")

    # Display the countdown GUI
    display_countdown_gui(days_until_next_season)

if __name__ == "__main__":
    main()