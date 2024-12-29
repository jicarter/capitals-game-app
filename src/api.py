import requests
import json
from datetime import datetime, timezone, timedelta
import threading
import time

API_URL = "https://api-web.nhle.com/v1/club-schedule-season/wsh/20242025"
CHECK_INTERVAL = 60 * 60  # Check every hour

def fetch_schedule():
    print("Fetching schedule...")
    response = requests.get(API_URL)
    print(f"API Response Status: {response.status_code}")
    if response.status_code == 200:
        print("API call successful.")
        # Save the raw JSON for inspection
        with open("schedule.json", "w") as file:
            json.dump(response.json(), file, indent=4)
        return response.json().get("games", [])
    else:
        print(f"API call failed: {response.status_code}")
        return []

def fetch_next_game():
    print("Fetching the next game...")
    schedule = fetch_schedule()
    now = datetime.now(timezone.utc)

    for game in schedule:
        # Parse start time
        game_start_time = datetime.fromisoformat(game["startTimeUTC"].replace("Z", "+00:00"))

        # Adjust time for venue offset
        venue_offset_str = game.get("venueUTCOffset", "+00:00")
        hours_offset = int(venue_offset_str.split(":")[0])
        minutes_offset = int(venue_offset_str.split(":")[1])
        offset = timedelta(hours=hours_offset, minutes=minutes_offset)
        local_start_time = game_start_time + offset

        # Convert to Central Time (subtract 1 hour from Eastern Time)
        central_time = local_start_time - timedelta(hours=1)

        formatted_time = central_time.strftime("%Y-%m-%d %H:%M:%S")

        home_team_name = game["homeTeam"]["commonName"]["default"]
        away_team_name = game["awayTeam"]["commonName"]["default"]
        home_team_logo = game["homeTeam"]["logo"]
        away_team_logo = game["awayTeam"]["logo"]

        # Check if the game is today and hasn't ended yet
        if now.date() == game_start_time.date() and now < game_start_time + timedelta(hours=5):
            return {
                "date": formatted_time,
                "home_team": home_team_name,
                "home_logo": home_team_logo,
                "away_team": away_team_name,
                "away_logo": away_team_logo,
            }

        # Check for future games
        if game_start_time > now:
            return {
                "date": formatted_time,
                "home_team": home_team_name,
                "home_logo": home_team_logo,
                "away_team": away_team_name,
                "away_logo": away_team_logo,
            }

    return None

def update_loop():
    while True:
        next_game = fetch_next_game()
        if next_game:
            print(f"Next game: {next_game}")
            # Call the display function here if needed
            # display_game_gui(next_game)
        else:
            print("No upcoming games found.")
        time.sleep(CHECK_INTERVAL)

def main():
    update_thread = threading.Thread(target=update_loop)
    update_thread.daemon = True
    update_thread.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()