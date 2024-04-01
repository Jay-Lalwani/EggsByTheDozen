from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'Image-Upload' not in request.files:
        return 'No file part'
    file = request.files['Image-Upload']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Assuming you have a template named 'display_image.html'
        # that is designed to display an image
        return render_template('predict.html', image_url=filepath)
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True, port=5001)