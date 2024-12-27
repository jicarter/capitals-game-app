from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter as tk
from tkinter import font as tkFont
import requests
from io import BytesIO
from cairosvg import svg2png
import os

def get_logo_image(url, size=(350, 300)):
    """Fetch and process the team logo image."""
    try:
        print(f"Fetching logo from: {url}")
        response = requests.get(url)
        response.raise_for_status()

        if url.endswith(".svg"):
            png_data = svg2png(bytestring=response.content)
            img_data = BytesIO(png_data)
        else:
            img_data = BytesIO(response.content)

        img = Image.open(img_data).convert("RGBA")
        background = Image.new("RGBA", img.size, (0,0,0,0))  # Transparent background
        img = Image.alpha_composite(background, img)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error fetching or processing logo from {url}: {e}")
        return None

def create_text_image(text, font_path, font_size, image_size, color="white", bg="black"):
    """Create an image with custom text using a specific font."""
    text = text.upper()  # Convert text to uppercase
    print(f"Attempting to load font from: {font_path}")
    try:
        print(f"Loading font from: {font_path}")
        font = ImageFont.truetype(font_path, font_size)
        print("Font loaded successfully.")
        img = Image.new("RGBA", image_size, bg)
        draw = ImageDraw.Draw(img)
        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((image_size[0] - w) / 2, (image_size[1] - h) / 2), text, font=font, fill=color)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading custom font, using default: {e}")
        font = ImageFont.load_default()
        img = Image.new("RGBA", image_size, bg)
        draw = ImageDraw.Draw(img)
        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((image_size[0] - w) / 2, (image_size[1] - h) / 2), text, font=font, fill=color)
        return ImageTk.PhotoImage(img)

def toggle_fullscreen(event=None):
    """Toggle full-screen mode."""
    root = event.widget
    is_fullscreen = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not is_fullscreen)

def exit_fullscreen(event=None):
    """Exit full-screen mode."""
    root = event.widget
    root.attributes("-fullscreen", False)

def display_game_gui(game):
    """Display the game details in a GUI optimized for showcasing team logos."""
    root = tk.Tk()
    root.title("Next Capitals Game")
    root.geometry("800x480")  # Set window size to match screen resolution
    root.configure(bg="black")

       # Full-screen mode
    root.attributes("-fullscreen", True)
    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", exit_fullscreen)

    # Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    font_path = os.path.join(project_root, "src", "assets", "fonts", "NHL.ttf")
    abs_font_path = os.path.abspath(font_path)
    print("Resolved font path:", abs_font_path)
    print("Current working directory:", os.getcwd())
    if not os.path.exists(abs_font_path):
        print("Font file not found.")
    else:
        print("Font file found.")

    # Load custom font
    try:
        if 'NHL' not in tkFont.names():
            root.tk.call('font', 'create', 'NHL', '-family', 'NHL', '-size', 14, '-weight', 'bold')
        custom_font = tkFont.Font(name='NHL')
    except Exception as e:
        print(f"Error loading font: {e}")
        custom_font = tkFont.Font(family="Arial", size=14, weight="bold")

    # Grid layout configuration
    root.grid_columnconfigure(0, weight=1)  # Left column
    root.grid_columnconfigure(1, weight=1)  # Center column
    root.grid_columnconfigure(2, weight=1)  # Right column
    root.grid_rowconfigure(0, weight=1)  # Logos
    root.grid_rowconfigure(1, weight=1)  # Team names
    root.grid_rowconfigure(2, weight=1)  # Date and time

    # Fetch and process logos
    home_logo = get_logo_image(game["home_logo"], size=(350, 300))
    away_logo = get_logo_image(game["away_logo"], size=(350, 300))

    # Home Team Logo
    if home_logo:
        home_logo_label = tk.Label(root, image=home_logo, bg="black")
        home_logo_label.image = home_logo
        home_logo_label.grid(row=0, column=2, padx=(20, 10), sticky="nsew")

    # Away Team Logo
    if away_logo:
        away_logo_label = tk.Label(root, image=away_logo, bg="black")
        away_logo_label.image = away_logo
        away_logo_label.grid(row=0, column=0, padx=(10, 20), sticky="nsew")

    # Create team names with NHL font
    home_team_img = create_text_image(
        text=game["home_team"], font_path=abs_font_path, font_size=36, image_size=(350, 50)
    )
    away_team_img = create_text_image(
        text=game["away_team"], font_path=abs_font_path, font_size=36, image_size=(350, 50)
    )

    home_team_label = tk.Label(root, image=home_team_img, bg="black")
    home_team_label.image = home_team_img
    home_team_label.grid(row=1, column=2)

    away_team_label = tk.Label(root, image=away_team_img, bg="black")
    away_team_label.image = away_team_img
    away_team_label.grid(row=1, column=0)

    # "At" Label
    at_label = tk.Label(root, text="AT", font=custom_font, fg="white", bg="black")
    at_label.grid(row=1, column=1)

    # Game Date and Time
    date_label = tk.Label(root, text=f"{game['date']}", font=("Arial", 20), fg="white", bg="black")
    date_label.grid(row=2, column=0, columnspan=3, pady=(10, 10))

    # Run the GUI event loop
    root.mainloop()

def display_countdown_gui(days_until_next_season):
    """Display a countdown timer until the next season starts."""
    root = tk.Tk()
    root.title("Season Countdown")
    root.geometry("800x480")  # Set window size to match screen resolution
    root.configure(bg="black")

    # Full-screen mode
    root.attributes("-fullscreen", True)
    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", exit_fullscreen)

    # Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    font_path = os.path.join(project_root, "src", "assets", "fonts", "NHL.ttf")
    abs_font_path = os.path.abspath(font_path)
    print("Resolved font path:", abs_font_path)
    print("Current working directory:", os.getcwd())
    if not os.path.exists(abs_font_path):
        print("Font file not found.")
    else:
        print("Font file found.")

    # Load custom font
    try:
        if 'NHL' not in tkFont.names():
            root.tk.call('font', 'create', 'NHL', '-family', 'NHL', '-size', 14, '-weight', 'bold')
        custom_font = tkFont.Font(name='NHL')
    except Exception as e:
        print(f"Error loading font: {e}")
        custom_font = tkFont.Font(family="Arial", size=14, weight="bold")

    # Grid layout configuration
    root.grid_columnconfigure(0, weight=1)  # Center column
    root.grid_rowconfigure(0, weight=1)  # Logo
    root.grid_rowconfigure(1, weight=1)  # Name
    root.grid_rowconfigure(2, weight=1)  # Countdown

    # Washington Capitals Logo
    capitals_logo_url = "https://assets.nhle.com/logos/nhl/svg/WSH_secondary_light.svg"
    capitals_logo = get_logo_image(capitals_logo_url, size=(350, 300))
    capitals_logo_label = tk.Label(root, image=capitals_logo, bg="black")
    capitals_logo_label.image = capitals_logo
    capitals_logo_label.grid(row=0, column=0, pady=(20, 10), sticky="nsew")

    # Washington Capitals Name
    capitals_name_img = create_text_image(
        text="Washington Capitals", font_path=abs_font_path, font_size=36, image_size=(800, 50)
    )
    capitals_name_label = tk.Label(root, image=capitals_name_img, bg="black")
    capitals_name_label.image = capitals_name_img
    capitals_name_label.grid(row=1, column=0, pady=(10, 20))

    # Countdown Timer
    countdown_frame = tk.Frame(root, bg="black")
    countdown_frame.grid(row=2, column=0, pady=(10, 10), sticky="nsew")

    countdown_text_label = tk.Label(countdown_frame, text="Season start: ", font=("Arial", 20), fg="white", bg="black")
    countdown_text_label.pack(side="left", padx=(250, 0))

    days_label = tk.Label(countdown_frame, text=f"{days_until_next_season}", font=("Arial", 20), fg="red", bg="black")
    days_label.pack(side="left")

    days_label = tk.Label(countdown_frame, text=f"days", font=("Arial", 20), fg="white", bg="black")
    days_label.pack(side="left")

    # Run the GUI event loop
    root.mainloop()