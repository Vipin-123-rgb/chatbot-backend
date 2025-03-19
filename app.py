import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify

# Basic conversation pairs
pairs = [
    [r"hi|hello", ["Namaste bhai!", "Hi, kya chal raha hai?"]],
    [r"kya kar raha hai", ["Bas, tujhse baat kar raha hoon!", "Coding, aur tu?"]],
    [r"bye", ["Alvida bhai!", "Phir milte hai!"]]
]

# Chatbot banaye
chatbot = Chat(pairs, reflections)

# Flask app
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message").strip()
    if user_input.lower() == "exit":
        response = "Bhai, phir milte hai!"
    else:
        response = chatbot.respond(user_input)
        if not response:
            response = "Bhai, yeh toh samajh nahi aaya!"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()