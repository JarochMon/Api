from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    prediction = {'prediction': 'Resultado simulado'}
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug = True)
