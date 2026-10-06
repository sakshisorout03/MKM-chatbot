from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(msg):
    msg = msg.lower()
    
    if "mca" in msg:
        return "MCA is 2 years course. Total fees Rs 2.5 Lakhs. Eligibility Graduation with 50%."
    elif "bca" in msg:
        return "BCA is 3 years course. Total fees Rs 1.8 Lakhs. Eligibility 12th with 50%."
    elif "msc" in msg:
        return "MSc is 2 years course. Total fees Rs 1.2 Lakhs. Eligibility Graduation with 50%."
    elif "bba" in msg or "mba" in msg:
        return "MBA is 2 years course. Fees Rs 2 Lakhs. BBA is 3 years, Fees Rs 1.5 Lakhs."
    elif "bus" in msg or "transport" in msg:
        return "Yes, College bus facility is available from Ambala, Kurukshetra, Yamunanagar, Karnal."
    elif "hostel" in msg:
        return "Yes, Girls hostel available inside campus. Fees Rs 60,000 per year."
    elif "admission" in msg:
        return "Admission open for 2025-26. Contact college office 0171-1234567."
    else:
        return "Hello! Welcome to MKM Group of Colleges For Girls. How can I help you? You can ask about BCA, MCA, MSc, buses, hostel, admission."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_msg = request.json.get("message")
    bot_reply = get_bot_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run()
