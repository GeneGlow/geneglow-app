from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import gspread
from google.oauth2.service_account import Credentials
import traceback
import random

app = Flask(__name__)

# --- 🗂️ Google Sheets Setup ---
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Load credentials from service_account.json
creds = Credentials.from_service_account_file(
    'service_account.json',
    scopes=scope
)

client = gspread.authorize(creds)
sheet = client.open_by_key('1LV18tFi7kECetKsC2_UnJAs3cXLiXr2m7rea4SXbZkw').sheet1

# --- 🖼️ Upload Settings ---
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- 🤖 Fake AI Analysis ---
def analyze_skin_tone(image_path):
    tones = ['Fair', 'Medium', 'Olive', 'Brown', 'Dark']
    return random.choice(tones)

# --- 🌸 ROUTES ---
@app.route('/')
def splash():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No image uploaded 😢"
        file = request.files['image']
        if file.filename == '':
            return "No file selected 🙈"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            skin_tone = analyze_skin_tone(filepath)
            image_url = url_for('static', filename=f'uploads/{filename}')
            return render_template('analyze.html', image_url=image_url, skin_tone=skin_tone)
        return "File type not allowed! Upload png/jpg/jpeg."
    return render_template('upload.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        responses = request.form.to_dict()
        image_file = request.files.get('image')

        image_url = None
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)
            image_url = url_for('static', filename=f'uploads/{filename}')
        else:
            filename = None

        ai_skin_tone = analyze_skin_tone(filename) if filename else "Unknown"

        try:
            sheet.append_row([
                responses.get('name', ''),
                responses.get('email', ''),
                responses.get('age', ''),
                responses.get('skin_type', ''),
                responses.get('skin_concerns', ''),
                responses.get('sunscreen', ''),
                responses.get('sleep', ''),
                responses.get('water', ''),
                responses.get('junk', ''),
                responses.get('location', '')
            ])
        except Exception as e:
            print("Error writing to Google Sheet:", e)
            print(traceback.format_exc())

        result = generate_results(responses)
        result['form_data'] = responses
        result['ai_skin_tone'] = ai_skin_tone

        return render_template('results.html', result=result, image_url=image_url)

    return render_template('quiz.html')

# --- 🔬 Result Analysis Logic ---
def generate_results(data):
    result = {}
    skin_type = data.get('skin_type', '').lower()

    if 'dry' in skin_type:
        result['type'] = "Dry Skin"
        result['products'] = ["Hyaluronic Acid Serum", "Cream-based Cleanser", "Ceramide Moisturizer"]
        result['remedies'] = ["Apply honey as a mask", "Use aloe vera gel overnight"]
        result['tips'] = ["Avoid hot water", "Use thick moisturizers", "Hydrate often"]
    elif 'oily' in skin_type:
        result['type'] = "Oily Skin"
        result['products'] = ["Salicylic Acid Cleanser", "Oil-free Gel Moisturizer", "Niacinamide Serum"]
        result['remedies'] = ["Multani mitti mask", "Use green tea toner"]
        result['tips'] = ["Avoid heavy creams", "Blot face during day", "Exfoliate twice a week"]
    elif 'sensitive' in skin_type:
        result['type'] = "Sensitive Skin"
        result['products'] = ["Fragrance-free Moisturizer", "Gentle Cleanser", "Centella Asiatica Cream"]
        result['remedies'] = ["Cucumber mask", "Chilled rose water spray"]
        result['tips'] = ["Patch test new products", "Avoid alcohol-based toners"]
    elif 'combination' in skin_type:
        result['type'] = "Combination Skin"
        result['products'] = ["Foaming Cleanser", "Light Gel Moisturizer", "BHA Serum"]
        result['remedies'] = ["Clay mask for T-zone", "Rose water for cheeks"]
        result['tips'] = ["Use separate products for different zones", "Hydrate & balance"]
    else:
        result['type'] = "Normal or Undetermined Skin"
        result['products'] = ["Balanced Cleanser", "SPF 50 Sunscreen", "Hydrating Toner"]
        result['remedies'] = ["DIY yogurt and honey mask", "Gentle exfoliation once a week"]
        result['tips'] = ["Maintain a simple routine", "Continue monitoring skin changes"]

    water = int(data.get('water', 0) or 0)
    sleep = int(data.get('sleep', 0) or 0)
    lifestyle = []

    if water < 5:
        lifestyle.append("Try drinking at least 7-8 glasses of water daily. Hydration = glow ✨")
    if sleep < 6:
        lifestyle.append("Try to sleep at least 7 hours for better skin regeneration 🌙")
    if data.get('junk', '').lower() == 'high':
        lifestyle.append("Reduce sugar & processed food to prevent breakouts 🍭🚫")
    if data.get('sunscreen', '').lower() == 'no':
        lifestyle.append("Start using SPF daily, even indoors ☀️🛡️")

    result['lifestyle'] = lifestyle
    return result

# --- 🌐 Run Server ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
