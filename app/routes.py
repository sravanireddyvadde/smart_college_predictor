from flask import Blueprint, render_template, request
from result import get_prediction

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    rank = int(request.form['rank'])
    gender = request.form['gender']
    caste = request.form['caste']
    region = request.form['region']

    results = get_prediction(rank, gender, caste, region)

    if results.empty:
        return render_template('result.html', colleges=None)

    return render_template('result.html', colleges=results.to_dict(orient='records'))
