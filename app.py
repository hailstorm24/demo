from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/adjectives', methods=['POST','OPTIONS'])
def adjectives():
    word_checks = {
        'flagged': {"pretty" : "Consider Eliminating."},
        'suggestions': {"helpful": "collaborative", "bossy" : "assertive"}
    }
    response = jsonify(word_checks)
    return response

if __name__ == '__main__':
    app.run(debug=True)
