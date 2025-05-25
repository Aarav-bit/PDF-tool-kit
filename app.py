from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from utils.split import split_pdf
from utils.rotate import rotate_pdf
from utils.password import add_password, remove_password

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/split', methods=['POST'])
def split():
    file = request.files['pdf']
    start = int(request.form['start_page'])
    end = int(request.form['end_page'])

    input_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(input_path)

    output_path = os.path.join(UPLOAD_FOLDER, 'split.pdf')
    split_pdf(input_path, start, end, output_path)

    return send_file(output_path, as_attachment=True)

@app.route('/rotate', methods=['POST'])
def rotate():
    file = request.files['pdf']
    angle = int(request.form['angle'])

    input_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(input_path)

    output_path = os.path.join(UPLOAD_FOLDER, 'rotated.pdf')
    rotate_pdf(input_path, angle, output_path)

    return send_file(output_path, as_attachment=True)

@app.route('/add-password', methods=['POST'])
def add_pw():
    file = request.files['pdf']
    password = request.form['password']

    input_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(input_path)

    output_path = os.path.join(UPLOAD_FOLDER, 'protected.pdf')
    add_password(input_path, password, output_path)

    return send_file(output_path, as_attachment=True)

@app.route('/remove-password', methods=['POST'])
def remove_pw():
    file = request.files['pdf']
    password = request.form['password']

    input_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(input_path)

    output_path = os.path.join(UPLOAD_FOLDER, 'unprotected.pdf')
    remove_password(input_path, password, output_path)

    return send_file(output_path, as_attachment=True)
