import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify
from flask_cors import CORS

# NLTK data download (Render pe zaroori hai)
nltk.download('punkt', quiet=True)

# Basic conversation pairs
pairs = [
    [r"hi|hello", ["Namaste bhai!", "Hi, kya chal raha hai?"]],
    [r"kya kar raha hai|kya kar rahe ho", ["Bas, tujhse baat kar raha hoon!", "Coding, aur tu?"]],
    [r"kyu|kyun", ["Bas aise hi, tu bol kyun poochha?"]],
    [r"bye", ["Alvida bhai!", "Phir milte hai!"]]
]

# Chatbot banaye
chatbot = Chat(pairs, reflections)

# Flask app
app = Flask(__name__)
CORS(app)  # CORS enable karo taaki GitHub Pages se requests allow ho

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"response": "Bhai, kuch toh bol!"}), 400
        if user_input.lower() == "exit":
            response = "Bhai, phir milte hai!"
        else:
            response = chatbot.respond(user_input)
            if not response:
                response = "Bhai, yeh toh samajh nahi aaya!"
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"Bhai, error ho gaya: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # Render ke liye host aur port set
