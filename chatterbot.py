#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        try:
            data = request.get_json()
            input_text = data['text']
            response_text = process_input(input_text)
            return jsonify({'response': response_text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

def process_input(input_text):
    # Simple echo bot, just return whatever it receives
    return f"You said: {input_text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)