from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        responses = request.form.to_dict()
        return render_template('results.html', data=responses, result=generate_results(responses))
    return render_template('quiz.html')

@app.route('/results')
def results():
    return render_template('results.html')

def generate_results(data):
    result = {}

    # Analyze Skin Type
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

    # Additional custom tips based on lifestyle
    water = int(data.get('water', 0))
    sleep = int(data.get('sleep', 0))

    lifestyle = []
    if water < 5:
        lifestyle.append("Try drinking at least 7-8 glasses of water daily. Hydration = glow ✨")
    if sleep < 6:
        lifestyle.append("Try to sleep at least 7 hours for better skin regeneration 🌙")
    if data.get('junk', '').lower() == 'high':
        lifestyle.append("Reduce sugar & processed food to prevent breakouts 🍭🚫")
    if data.get('sunscreen', '') == 'no':
        lifestyle.append("Start using SPF daily, even indoors ☀️🛡️")

    result['lifestyle'] = lifestyle
    return result
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
