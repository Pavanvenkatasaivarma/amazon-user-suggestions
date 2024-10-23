from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models
model = joblib.load('categorymodel.pkl')
mdl = joblib.load('purchasemodel.pkl')
product_recommendations = joblib.load('product_recommendations.pkl')

@app.route('/')
def home():
    return render_template('index.html')

# Handle form submission and predict segment
@app.route('/get_suggestions', methods=['get','POST'])
def get_suggestions():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        monthly_income = int(request.form['monthly_income'])
        gender = request.form['gender']
        education = request.form['education']
        region = request.form['region']
        loyalty = request.form['loyalty']
        purchase = int(request.form['purchase'])

        # Prepare data for model prediction
        input_data = np.array([[age, monthly_income, gender, education, region, loyalty, purchase]],dtype=np.float64)

        # Predict user segment
        segment = model.predict(input_data)[0]
        purchase = mdl.predict(input_data)[0]

        names = ['beauty','books','clothing','electronics','food','health','home']

        # Get product recommendations for the predicted segment
        recommendations = product_recommendations.get(segment, [])

        # Render the result in the same HTML page
        return render_template('suggestions.html', segment=names[segment], purchase=int(purchase), recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
