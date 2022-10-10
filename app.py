from flask import Flask, render_template, request, jsonify
import webbrowser
from chat import get_response

app = Flask(__name__)
@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()