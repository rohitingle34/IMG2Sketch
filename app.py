from flask import Flask, render_template, request, send_from_directory
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'results'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Image processing code here (similar to your provided code)
            img = cv2.imread(filepath)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_invert = cv2.bitwise_not(img_gray)
            img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)

            def dodgeV2(x, y):
                return cv2.divide(x, 255 - y, scale=256)

            final_img = dodgeV2(img_gray, img_smoothing)

            # Set dark_factor to 1.0 (no darkening)
            dark_factor = 1.0
            darkened_img = np.clip(final_img * dark_factor, 0, 255).astype(np.uint8)

            result_filepath = os.path.join(app.config['RESULT_FOLDER'], filename)
            cv2.imwrite(result_filepath, darkened_img)

            return render_template('index.html', original=filename, result=os.path.basename(result_filepath))

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/results/<filename>')
def result_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

# Create a scheduler
scheduler = BackgroundScheduler(daemon=True)

def clear_folders():
    """
    Function to clear the 'uploads' and 'results' folders.
    """
    uploads_folder = app.config['UPLOAD_FOLDER']
    results_folder = app.config['RESULT_FOLDER']

    for folder in [uploads_folder, results_folder]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# Schedule the task to run every 20 minutes
scheduler.add_job(clear_folders, 'interval', minutes=20)
scheduler.start()

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)
    app.run(debug=True)
