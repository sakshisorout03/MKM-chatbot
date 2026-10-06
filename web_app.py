from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(msg):
    msg = msg.lower().strip()
    if "mca" in msg:
        return "MCA is 2 years course. Total fees Rs 2.5 Lakhs. Eligibility Graduation with 50%."
    elif "bca" in msg:
        return "BCA is 3 years course. Total fees Rs 1.8 Lakhs. Eligibility 12th with 50%."
    elif "msc" in msg:
        return "MSc is 2 years course. Total fees Rs 1.2 Lakhs. Eligibility Graduation with 50%."
    elif "bba" in msg or "mba" in msg:
        return "MBA is 2 years, Fees 2 Lakhs. BBA is 3 years, Fees 1.5 Lakhs."
    elif "bus" in msg or "transport" in msg:
        return "Yes, Bus facility available from Ambala, Kurukshetra, Yamunanagar, Karnal."
    elif "hostel" in msg:
        return "Yes, Girls hostel available inside campus. Fees 60,000 per year."
    elif "admission" in msg:
        return "Admission open for 2025-26. Contact college office 0171-1234567."
    else:
        return "Hello! Welcome to MKM Group of Colleges. Ask about BCA, MCA, MSc, buses, hostel."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def get_response():
    if request.method == "POST":
        data = request.get_json()
        if data:
            user_msg = data.get("message", "")
        else:
            user_msg = request.form.get("msg", "")
    else:
        user_msg = request.args.get("msg", "")
    
    if not user_msg:
        user_msg = "hello"
    
    bot_reply = get_bot_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
