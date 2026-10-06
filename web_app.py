from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sab jawab yahin likhe hai, isliye error kabhi nahi ayega
ANSWERS = {
    "hi": "Hello! Welcome to MKM Group of Colleges For Girls Help Bot. Ask about BCA, MCA, MBA, BBA, BSc, MSc, Bus, Hostel, Library, Canteen.",
    "hello": "Hello! Welcome to MKM Group of Colleges For Girls Help Bot.",
    "mca": "MCA is 2 years, Fees Rs 2.5 Lakhs, Eligibility Graduation 50% + Maths.",
    "bca": "BCA is 3 years, Fees Rs 1.8 Lakhs, Eligibility 12th 50%.",
    "mba": "MBA is 2 years, Fees Rs 2 Lakhs, Eligibility Graduation 50%.",
    "bba": "BBA is 3 years, Fees Rs 1.5 Lakhs, Eligibility 12th 50%.",
    "bsc": "BSc is 3 years, Fees Rs 90k, Medical & Non-Medical available.",
    "msc": "MSc is 2 years, Fees Rs 1.2 Lakhs.",
    "bcom": "B.Com is 3 years, Fees Rs 75k.",
    "ba": "BA is 3 years, Fees Rs 60k.",
    "ma": "MA is 2 years, Fees Rs 50k.",
    "bed": "B.Ed is 2 years, Fees Rs 1.2 Lakhs.",
    "courses": "We offer B.Sc, M.Sc, BCA, MCA, BBA, MBA, B.Com, MA, B.Ed and Diploma.",
    "admission": "Admission open 2025-26, Visit college with docs, Last date 31 July, Phone 7082929917.",
    "bus": "Yes, bus facility available for Palwal, Hodal, Hathin, Ballabgarh. Call 7082929917.",
    "hostel": "Yes, Girls hostel available, Fees Rs 7000-14000 per year.",
    "library": "Big Library with 15000+ books, e-books, Wi-Fi, open 9AM to 4PM.",
    "canteen": "Canteen with hygienic food available inside campus.",
    "sports": "Sports ground for Volleyball, Badminton, Kho-Kho available.",
    "scholarship": "Scholarship for SC/ST/OBC and merit students available.",
    "placement": "Placement available, Companies Infosys, Wipro, TCS, Average package 2.5 LPA.",
    "timing": "College timing 9AM to 3:30PM, Monday to Saturday.",
    "address": "MKM College, Near Bus Stand, Hodal, Palwal - 121106, Phone 7082929917, Email mkmhodal@gmail.com"
}

def get_reply(msg):
    m = msg.lower()
    for key in ANSWERS:
        if key in m:
            return ANSWERS[key]
    return ANSWERS["hi"]

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except:
        return "<h2>MKM Chatbot is Live! Use /get?msg=hi</h2>"

@app.route("/get", methods=["GET", "POST"])
def get_bot():
    try:
        if request.method == "POST":
            data = request.get_json(silent=True)
            user_msg = data.get("message") if data and "message" in data else request.form.get("msg","hi")
        else:
            user_msg = request.args.get("msg","") or request.args.get("message","hi")
        if not user_msg:
            user_msg = "hi"
        reply = get_reply(user_msg)
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"Hello! Ask about MCA, BCA, MBA, Bus, Hostel, Library. Error: {str(e)}"})

if __name__ == "__main__":
    app.run()
