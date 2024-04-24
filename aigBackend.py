from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/')
def hello():
    return 'Hello, Flask is running!'

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the POST request contains an image file
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']

    # If the user does not select a file, the browser submits an empty part without filename
    if image_file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    # Save the uploaded file to the specified upload directory
    filename = secure_filename(image_file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image_file.save(filepath)

    # Generate ASCII art from the uploaded image
    ascii_art = image_to_ascii(filepath)

    if ascii_art is None:
        return jsonify({'error': 'Failed to generate ASCII art'}), 500

    # Save ASCII art to a text file
    ascii_file_path = os.path.join(APP_ROOT, 'output_ascii_art.txt')

    with open(ascii_file_path, 'w') as f:
        f.write(ascii_art)

    # Debug: Check if the ASCII art file exists and its content
    if os.path.exists(ascii_file_path):
        print(f"ASCII art file created at: {ascii_file_path}")
        with open(ascii_file_path, 'r') as f:
            print(f.read())
    else:
        print("ASCII art file not found!")

    #delete the image after generating ASCII Art
    os.remove(filepath)

    # Trigger file download by sending the file as an attachment
    response = send_file(ascii_file_path, as_attachment=True, download_name='ascii_art.txt', mimetype='text/plain')
    response.headers["Content-Type"] = "text/plain"  # Set Content-Type header explicitly

    # Debug: Print response headers
    print(response.headers)

    return response

if __name__ == '__main__':
    app.run(debug=True)