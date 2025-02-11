from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('student_dropout_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST']) 
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template('index.html', prediction_text=f'Prediction: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)
