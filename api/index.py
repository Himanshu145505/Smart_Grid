# Imports
from flask import Flask, render_template, request, redirect, url_for
import pickle
import sklearn
import os

# Load pickled models with error handling
try:
    with open(os.path.join(os.path.dirname(__file__), '..', 'models', 'model1.pkl'), 'rb') as file:
        pickled_model1 = pickle.load(file)
except FileNotFoundError as e:
    print(f"Error loading model1.pkl: {e}")
    pickled_model1 = None  # Fallback to avoid crash
except Exception as e:
    print(f"Error loading model1.pkl: {e}")
    pickled_model1 = None

try:
    with open(os.path.join(os.path.dirname(__file__), '..', 'models', 'model2.pkl'), 'rb') as file:
        pickled_model2 = pickle.load(file)
except FileNotFoundError as e:
    print(f"Error loading model2.pkl: {e}")
    pickled_model2 = None  # Fallback to avoid crash
except Exception as e:
    print(f"Error loading model2.pkl: {e}")
    pickled_model2 = None

# Initialize Flask app with corrected template and static paths
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Routes for static pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/features.html')
def features():
    return render_template('features.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

# Results route
@app.route('/results.html')
def results():
    prediction = request.args.get('prediction')
    return render_template('results.html', prediction=prediction)

# Model 1: Grid Stability Prediction
@app.route('/model1.html', methods=['POST', 'GET'])
def model1():
    if request.method == 'POST':
        if pickled_model1 is None:
            return "Error: Model 1 not loaded", 500
        reaction_time_producer = float(request.form['reactionTimeProducer'])
        reaction_time_consumer1 = float(request.form['reactionTimeConsumer1'])
        reaction_time_consumer2 = float(request.form['reactionTimeConsumer2'])
        reaction_time_consumer3 = float(request.form['reactionTimeConsumer3'])
        elasticity_producer = float(request.form['elasticityProducer'])
        elasticity_consumer1 = float(request.form['elasticityConsumer1'])
        elasticity_consumer2 = float(request.form['elasticityConsumer2'])
        elasticity_consumer3 = float(request.form['elasticityConsumer3'])
        stab = float(request.form['stab'])

        prediction_num = pickled_model1.predict([[reaction_time_producer, reaction_time_consumer1, reaction_time_consumer2, reaction_time_consumer3, elasticity_producer, elasticity_consumer1, elasticity_consumer2, elasticity_consumer3, stab]])
        prediction = "Stable" if prediction_num == 1 else "Unstable"

        return redirect(url_for('results', prediction=prediction))
    
    return render_template("model1.html")

# Model 2: Wind Turbine Energy Prediction
@app.route('/model2.html', methods=['POST', 'GET'])
def model2():
    if request.method == 'POST':
        if pickled_model2 is None:
            return "Error: Model 2 not loaded", 500
        wind_speed = float(request.form['windSpeed'])
        wind_direction = float(request.form['windDirection'])
        power_curve = float(request.form['powerCurve'])

        prediction = pickled_model2.predict([[wind_speed, wind_direction, powerCurve]])
        prediction_with_units = f"{prediction} kW"

        return redirect(url_for('results', prediction=prediction_with_units))
    
    return render_template("model2.html")

# Vercel requires this export for serverless functions
def handler(request):
    return app(request.environ, request.start_response)