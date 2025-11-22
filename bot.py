import os
import requests
from flask import Flask, request

TOKEN = os.getenv("TOKEN")  # il token lo metti come variabile su Railway
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        # Risposta semplice
        requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": f"Hai scritto: {text}"})
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)