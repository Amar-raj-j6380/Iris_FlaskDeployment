from flask import Flask,request,render_template
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('dtc.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict_result():
    if request.method=="POST":
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)[0]
        species=''
        if prediction == 0:
           species='Iris Setosa' 
        if prediction == 1:
           species='Iris Versicolour' 
        if prediction == 2:
           species = 'Iris Virginica'
           
    return render_template('index.html',result='the species of the flower is {}'.format(species))
    
if __name__ == '__main__':
    app.run(debug=True)

"""
sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
def predict_result():
    if request.method=="POST":
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        result =  prediction[0]
    return render_template('index.html')
"""



"""
    if request.method == 'POST':
        # Get the input features from the form
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        feature4 = float(request.form['feature4'])

        # Make prediction using the input features
        prediction = predict([feature1, feature2, feature3, feature4])

        # Pass the prediction result to the template
        return render_template('index.html', prediction=prediction)
"""



