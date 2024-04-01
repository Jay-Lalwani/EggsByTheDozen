from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'Image-Upload' not in request.files:
        return redirect(request.url)
    file = request.files['Image-Upload']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Process the file here
        # For example, save it to a directory or pass it to your prediction model
        return 'File received and processed'
    return 'No file received'

if __name__ == '__main__':
    app.run(debug=True, port=5001)