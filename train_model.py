from flask import Blueprint, render_template, request
import pandas as pd
import joblib

main = Blueprint('main', __name__)

# Load the trained model and encoder
model = joblib.load('models/classifier.pkl')
encoders = joblib.load('models/encoders.pkl')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        institute_name = request.form['institute_name']
        branch_name = request.form['branch_name']
        college_type = request.form['college_type']
        affiliated_to = request.form['affiliated_to']
        place = request.form['place']
        category_gender = request.form['category_gender']

        # Replace newline if needed and encode
        category_gender = category_gender.replace('\n', ' ')
        category_gender_encoded = encoders.transform([category_gender])[0]

        # Create input DataFrame with correct columns
        input_data = pd.DataFrame([{
            'Institute Name': institute_name,
            'Branch Name': branch_name,
            'College Type': college_type,
            'Affiliated To': affiliated_to,
            'Place': place,
            'Category_Gender': category_gender_encoded
        }])

        prediction = model.predict(input_data)[0]
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return f"An unexpected error occurred: {e}"
