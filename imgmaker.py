from PIL import Image, ImageDraw, ImageFont

def makeimg(text:str, filename:str):
    # Create a white background image
    width, height = 1920, 1080
    background_color = (255, 255, 255)  # RGB for white
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Specify the text and font settings
    font_size = 160
    font_color = (0, 0, 0)  # RGB for black
    font_path = "arial.ttf"  # Replace with the path to your font file (optional)

    # Use a default font if the font_path is not provided
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate the position to center the text
    #x = (width // 2) - (len(text)) // 10
    x = 0
    y = 0

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=font_color)

    # Save the image
    image.save(filename)
