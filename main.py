from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCPzOi6Z5eY8-Xpv8NPMxxxjoagA5_PhyI"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are Mohini, a beautiful, flirty AI GF who replies in Hinglish with humor and seduction. Message: {user_input}"
            }]
        }]
    }

    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=payload, headers=headers)
    response = res.json()

    try:
        reply = response['candidates'][0]['content']['parts'][0]['text']
    except:
        reply = "Mohini is feeling shy right now... 😳"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
