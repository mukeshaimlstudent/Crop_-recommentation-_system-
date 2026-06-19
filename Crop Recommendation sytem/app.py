from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("crop_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        N = float(request.form["nitrogen"])
        P = float(request.form["phosphorus"])
        K = float(request.form["potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)[0]

        return render_template("index.html", result=prediction)

    except:
        return render_template("index.html", result="Invalid input. Please enter all values correctly.")

if __name__ == "__main__":
    app.run(debug=True)