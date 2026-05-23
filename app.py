from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form["message"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        chat_history.append(("You", user_message))
        chat_history.append(("AI", response.text))

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
