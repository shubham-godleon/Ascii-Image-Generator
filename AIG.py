from PIL import Image

def image_to_ascii(image_path, width=100, height=70):
    image = Image.open(image_path)
    image = image.convert("L")  # Convert the image to grayscale
    image = image.resize((width, height))

    ascii_chars = "#$%@&!/+=*^-;,'. " [::-1]
    ascii_image = ""

    for y in range(image.height):
        for x in range(image.width):
            pixel_intensity = image.getpixel((x, y))
            ascii_char = ascii_chars[int(pixel_intensity * len(ascii_chars) / 256)]
            ascii_image += ascii_char
        ascii_image += "\n"

    return ascii_image

image_path = r"C:/Users/shubh/Desktop/passport.jpg"
ascii_image = image_to_ascii(image_path)
print(ascii_image)