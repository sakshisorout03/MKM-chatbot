from flask import Flask, request, render_template_string
import json, pickle

app = Flask(__name__)

# model load karo
with open('chatbot_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('intents.json', 'r') as f:
    intents = json.load(f)

HTML = """
<h2>MKM College Help Bot</h2>
<form method="post">
<input name="q" style="width:300px" placeholder="Sawal likho">
<button>Send</button>
</form>
<p><b>Bot:</b> {{ans}}</p>
"""

def get_response(q):
    X = vectorizer.transform([q])
    tag = model.predict(X)[0]
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return intent['responses'][0]
    return "Maaf kijiye, jawab nahi mila"

@app.route("/", methods=["GET", "POST"])
def home():
    ans = ""
    if request.method == "POST":
        ans = get_response(request.form["q"])
    return render_template_string(HTML, ans=ans)