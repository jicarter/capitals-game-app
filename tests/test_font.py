from PIL import ImageFont
import os

# Define the font path relative to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
font_path = os.path.join(project_root, "src", "assets", "fonts", "NHL.ttf")
abs_font_path = os.path.abspath(font_path)
print("Resolved font path:", abs_font_path)

# Verify if the font file exists
if not os.path.exists(abs_font_path):
    print("Font file not found.")
    # List the contents of the src directory to verify
    src_dir = os.path.join(project_root, "src")
    print("Contents of the src directory:")
    print(os.listdir(src_dir))
else:
    print("Font file found.")

# Try to load the font
try:
    font = ImageFont.truetype(abs_font_path, 36)
    print("Font loaded successfully!")
except Exception as e:
    print(f"Error loading font: {e}")