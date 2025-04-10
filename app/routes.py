from flask import Blueprint, render_template, request
import pandas as pd
from .result import get_prediction

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        rank = int(request.form['rank'])
        gender = request.form['gender']
        caste = request.form['caste']
        region = request.form['region']

        colleges = get_prediction(rank, gender, caste, region)

        return render_template('result.html', colleges=colleges.to_dict(orient='records'))
    except Exception as e:
        return render_template('result.html', colleges=[], error=str(e))
