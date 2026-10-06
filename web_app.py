from flask import Flask, request, jsonify, render_template_string
import json, pickle, random

app = Flask(__name__)

with open('intents.json', 'r') as f:
    data = json.load(f)
with open('chatbot_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

HTML = """
<html><body style="font-family:Arial; background:#f0f2f5;">
<div style="max-width:500px; margin:50px auto; background:white; padding:20px; border-radius:15px; box-shadow:0 0 10px gray;">
<h2 style="text-align:center; color:#8e44ad;">MKM College Help Bot</h2>
<div id="chat" style="height:300px; overflow-y:auto; border:1px solid #ccc; padding:10px; margin-bottom:10px;"></div>
<input id="msg" placeholder="Type your question..." style="width:75%; padding:10px;">
<button onclick="send()" style="padding:10px; background:#8e44ad; color:white; border:none; border-radius:5px;">Send</button>
</div>
<script>
function send(){
 let m=document.getElementById('msg').value;
 document.getElementById('chat').innerHTML += "<p><b>You:</b> "+m+"</p>";
 fetch('/get?msg='+m).then(r=>r.json()).then(d=>{
   document.getElementById('chat').innerHTML += "<p><b>Bot:</b> "+d.reply+"</p>";
 });
 document.getElementById('msg').value="";
}
</script>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/get')
def get_bot_response():
    user_msg = request.args.get('msg')
    X = vectorizer.transform([user_msg])
    tag = model.predict(X)[0]
    for intent in data['intents']:
        if intent['tag'] == tag:
            return jsonify({"reply": random.choice(intent['responses'])})
    return jsonify({"reply": "Sorry, I didn't understand."})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)