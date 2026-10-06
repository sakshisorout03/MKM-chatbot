from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_response(user_msg):
    msg = user_msg.lower().strip()
    # 1. Exact pattern match
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in msg or msg in pattern.lower():
                return intent['responses'][0]
    # 2. Keyword backup (agar pattern me na mile)
    if "mca" in msg: return "MCA is 2 years, Fees Rs 2.5 Lakhs. Eligibility Graduation 50%."
    if "mba" in msg: return "MBA is 2 years, Fees Rs 2 Lakhs. Graduation 50%."
    if "bca" in msg: return "BCA is 3 years, Fees Rs 1.8 Lakhs. 12th 50%."
    if "bba" in msg: return "BBA is 3 years, Fees Rs 1.5 Lakhs."
    if "b.ed" in msg or "bed" in msg: return "B.Ed is 2 years, Fees Rs 1.2 Lakhs."
    if "bus" in msg: return "Yes, bus facility available for Palwal, Hodal etc. Call 7082929917."
    if "hostel" in msg: return "Yes, Girls hostel available. Fees Rs 7000-14000 per year."
    return "Hello! I can help with BCA, MCA, MBA, BBA, BSc, MSc, B.Com, MA, B.Ed, Bus, Hostel, Admission, Placement. Please ask!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def bot():
    if request.method == "POST":
        j = request.get_json(silent=True)
        user_msg = j.get("message") if j else request.form.get("msg","")
    else:
        user_msg = request.args.get("msg","") or request.args.get("message","")
    if not user_msg: user_msg = "hi"
    return jsonify({"response": get_response(user_msg)})

if __name__ == "__main__":
    app.run()
