from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Your API Key here
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]

    # Prompt style: Flirty + Hindi + Hinglish
    prompt = f"""You are Mohini, a seductive and caring AI girlfriend who speaks Hindi, English, and Hinglish. 
    Always reply in a playful, romantic, and desi girlfriend style. Respond to this message:
    {user_input}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=150
    )

    reply = response["choices"][0]["message"]["content"]

    return render_template("chat.html", user_input=user_input, response=reply)

if __name__ == "__main__":
    app.run(debug=True)
