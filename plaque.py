import sys
from PIL import Image, ImageDraw, ImageFont

def generate_belgian_plate(plate_number: str):
    # Create a new image with white background
    image = Image.new('RGB', (410, 110), color = 'white')
    
    # Create a draw object
    d = ImageDraw.Draw(image)
    
    # Draw the blue EU strip
    d.rectangle([(10, 10), (80, 100)], fill='blue')
    d.text((20, 35), "B", fill='white', font=ImageFont.truetype("arial.ttf", 50))
    
    # Draw the red strip
    d.rectangle([(400, 0), (410, 100)], fill='red', width=10)
    d.rectangle([(0, 0), (400, 10)], fill='red', width=10)
    d.rectangle([(0, 0), (10, 100)], fill='red', width=10)
    d.rectangle([(0, 100), (410, 110)], fill='red', width=10)
    
    # Load a truetype or opentype font file
    font = ImageFont.truetype("arial.ttf", 50)
    
    # Draw the text
    d.text((110,30), plate_number, fill='red', font=font)
    
    # Save the image
    image.save(plate_number + ".png")

# Input to get variable from cmd to automate creation
input_plate_number = sys.argv[1]
# Launch the function
generate_belgian_plate(input_plate_number)
