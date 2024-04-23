from flask import Flask, request, jsonify
import joblib

# Load the pre-trained model
model = joblib.load('dtc2.pkl')

app = Flask(__name__)

@app.route('/ping')
def ping():  #vjjjj
    return {"message": "Hi there, I'm working!!"}

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure that the request is JSON and it contains the expected data
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    data = request.get_json()
    try:
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input data"}), 400

    prediction_returned = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    if prediction_returned == 0:
        prediction_returned = 'setosa'
    elif prediction_returned == 1:
        prediction_returned = 'versicolor'
    else:
        prediction_returned = 'virginica'

    return jsonify({"prediction": prediction_returned})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)  
    
    # Set debug=False in a production environment
    # -f /path/to/your/Dockerfile C:\Users\dell\Documents\GitHub\Iris_FlaskDeployment