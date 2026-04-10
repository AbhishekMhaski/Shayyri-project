from flask import Flask, render_template
import random

app = Flask(__name__)

shayaris = [
    "Dil se roye magar honto se muskura baithe...",
    "Zindagi ek haseen khwab hai, jisme jeene ki chahat honi chahiye...",
    "Mohabbat ka koi rang nahi phir bhi woh rangin hai...",
    "Waqt ke saath sab badal jata hai...",
    "Kabhi kisi ko itna mat chaho ke bhool na pao..."
]

@app.route('/')
def home():
    shayari = random.choice(shayaris)
    return render_template('index.html', shayari=shayari)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
