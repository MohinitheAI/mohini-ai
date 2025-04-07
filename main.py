from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Mohini AI 👩‍💻"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"reply": response})

def generate_response(msg):
    return f"🤖 Mohini AI says: You said '{msg}'"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
