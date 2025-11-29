# server.py (updated)
from flask import Flask, request, jsonify
from flask_cors import CORS
import jarvis_api  # <-- import new file

app = Flask(__name__)
CORS(app)

@app.route('/api/command', methods=['POST'])
def process():
    data = request.get_json() or {}
    cmd = data.get("command", "")
    if not cmd:
        return jsonify({"error": "No command"}), 400

    reply = jarvis_api.handle_command(cmd)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5000)
