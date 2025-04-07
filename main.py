from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Use your Gemini API key here
genai.configure(api_key="AIzaSyCPzOi6Z5eY8-Xpv8NPMxxxjoagA5_PhyI")

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    try:
        response = model.generate_content(user_input)
        answer = response.text
    except Exception as e:
        answer = "Sorry, Mohini AI is tired right now 😢. Try again later."
    return render_template('chat.html', user_input=user_input, response=answer)

if __name__ == '__main__':
    app.run(debug=True)
