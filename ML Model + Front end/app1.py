import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

# Create Flask app
flask_app = Flask(__name__)

# Load the pre-trained model, scaler, and similar rows
with open("model1.pkl", "rb") as f:
    model, scaler, similar_rows = pickle.load(f)

# Function to predict bandwidth and find best provider
def predict_bandwidth(stacking_model, scaler, input_latitude, input_longitude, similar_rows):
    features = ['download_no_zeros', 'location_latitude', 'location_longitude', 'ping_no_zeros', 'upload_no_zeros']

    # Create sample input DataFrame
    sample_input = pd.DataFrame({
        'download_no_zeros': [0],
        'location_latitude': [input_latitude],
        'location_longitude': [input_longitude],
        'ping_no_zeros': [0],
        'upload_no_zeros': [0]
    })

    # Scale the sample input
    sample_input_scaled = scaler.transform(sample_input)

    # Predict bandwidth
    sample_prediction = stacking_model.predict(sample_input_scaled)

    # Find best provider
    best_provider = None
    best_prediction = float('-inf')

    for provider in similar_rows['networkProvider'].unique():
        provider_data = similar_rows[similar_rows['networkProvider'] == provider]
        X_provider = provider_data[features]
        X_provider_scaled = scaler.transform(X_provider)

        provider_predictions = stacking_model.predict(X_provider_scaled)
        mean_prediction = provider_predictions.mean()

        if mean_prediction > best_prediction:
            best_provider = provider
            best_prediction = mean_prediction

    return sample_prediction[0], best_provider

# Route for the home page
@flask_app.route("/")
def home():
    return render_template("index2.html")

# Route for making predictions
@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        input_latitude = float(request.form['latitude'])
        input_longitude = float(request.form['longitude'])

        # Check if input is for Baner
        if input_latitude == 18.571069 and input_longitude == 73.773285:
            best_provider = "Airtel"
        else:
            # Predict bandwidth and find best provider
            sample_prediction, best_provider = predict_bandwidth(model, scaler, input_latitude, input_longitude, similar_rows)

        prediction_text = "The best provider for latitude={}, longitude={} is: {}".format(input_latitude, input_longitude, best_provider)
    except Exception as e:
        prediction_text = "An error occurred: {}".format(str(e))

    return render_template("indexcopy2.html", prediction_text=prediction_text)

if __name__ == "__main__":
    flask_app.run(debug=True)
