import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS, cross_origin
from predictFromModel import prediction

app = Flask(__name__)
CORS(app)

# Configurations
app.config["csv_file"] = "Prediction_Output_File/"
app.config["sample_file"] = "Prediction_SampleFile/"

# Routes
@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        try:
            if 'csvfile' not in request.files:
                return render_template("invalid.html")
            file = request.files['csvfile']
            df = pd.read_csv(file)
            df.to_csv('Prediction_InputFileFromUser/InputFile.csv', index=False)

            # Run Prediction
            pred = prediction()
            pred.predictionFromModel()
            print("Prediction is Done !!")
        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template("invalid.html")
    return render_template('predict.html')

@app.route('/result', methods=['GET'])
@cross_origin()
def result():
    try:
        # Load prediction results into a table
        output_file = os.path.join(app.config["csv_file"], os.listdir(app.config["csv_file"])[0])
        df = pd.read_csv(output_file)
        data = df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
        columns = df.columns.tolist()       # Extract column names
        return render_template('results.html', data=data, columns=columns)
    except Exception as e:
        print(f"Error displaying results: {e}")
        return render_template("invalid.html")

@app.route('/return_file/')
@cross_origin()
def return_file():
    try:
        final_file = os.listdir(app.config["csv_file"])[0]
        return send_from_directory(app.config["csv_file"], final_file)
    except Exception as e:
        print(f"Error returning file: {e}")
        return render_template("invalid.html")

@app.route('/return_sample_file/')
@cross_origin()
def return_sample_file():
    sample_file = os.listdir(app.config["sample_file"])[0]
    return send_from_directory(app.config["sample_file"], sample_file)

if __name__ == '__main__':
    app.run(debug=True)
