# Capitals Game App

A Python application that displays the next Washington Capitals game using the NHL API.

## Features
- Fetches the current season schedule for the Washington Capitals.
- Displays the next upcoming game with details.
- Shows a countdown to the next season if no upcoming games are found.
- Runs in full-screen mode by default and can be toggled with `F11` and exited with `Escape`.

## Requirements
- Python 3.7+
- Libraries: `requests`, `Pillow`, `cairosvg`, `tkinter`

## Project Structure

```
capitals-game-app/
├── src/
│   ├── api.py
│   ├── display.py
│   ├── main.py
│   └── ...
├── assets/
│   └── fonts/
│       └── NHL.ttf
├── data/
│   └── nhl_teams.json
├── venv/
│   └── ...
└── requirements.txt
```

### Files and Directories

- **src/**: Contains the source code for the application.
  - **api.py**: Contains functions to fetch the game schedule and determine the next game.
  - **display.py**: Contains functions to display the game details and countdown using a `tkinter` GUI.
  - **main.py**: The main entry point of the application. It fetches the next game and displays the GUI.
- **assets/**: Contains assets such as fonts.
  - **fonts/**: Contains the custom NHL font used in the application.
- **data/**: Contains data files.
  - **nhl_teams.json**: Contains information about NHL teams, including their logos.
- **venv/**: Contains the virtual environment for the project.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Installation and Running on Raspberry Pi

### Prerequisites

- Raspberry Pi with Raspbian OS installed.
- Internet connection.

### Steps

1. **Update the Package List**

   ```sh
   sudo apt-get update
   ```

2. **Install Required Packages**

   ```sh
   sudo apt-get install python3 python3-venv python3-pil python3-requests python3-tk
   ```

3. **Clone the Repository**

   Clone the project repository to your Raspberry Pi:

   ```sh
   git clone https://github.com/jicarter/capitals-game-app
   cd capitals-game-app
   ```

4. **Create a Virtual Environment**

   Create a virtual environment in your project directory:

   ```sh
   python3 -m venv venv
   ```

5. **Activate the Virtual Environment**

   Activate the virtual environment:

   ```sh
   source venv/bin/activate
   ```

6. **Install Python Dependencies**

   Install the required Python packages using `pip`:

   ```sh
   pip install -r requirements.txt
   ```

7. **Run the Application**

   Run the main script to start the application:

   ```sh
   python3 src/main.py
   ```

### Full-Screen Mode

The application runs in full-screen mode by default. You can toggle full-screen mode by pressing `F11` and exit full-screen mode by pressing `Escape`.

## License

This project is licensed under the MIT License.