from flask import Flask, jsonify

app = Flask(__name__)

# Un chatbot data thaan!
responses = {
    "fees": "B.Sc AI fees 25k da",
    "timing": "College timing 9.30 to 3.30 da",
    "ai": "AI future da thambi!",
}

@app.route('/')
def home():
    return "College AI App Backend is Running da!"

@app.route('/get/<question>')
def get_answer(question):
    question = question.lower()
    for key in responses:
        if key in question:
            return jsonify({"question": question, "answer": responses[key]})
    return jsonify({"answer": "Purila da, fees, timing, ai nu kelu"})

if __name__ == '__main__':
    print("Backend ON! http://127.0.0.1:5000/get/fees nu browser la paaru da")
    app.run(debug=True)