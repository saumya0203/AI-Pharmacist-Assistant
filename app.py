from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Pharmacist Backend is running!"})

if __name__ == '__main__':
    app.run(debug=True)
