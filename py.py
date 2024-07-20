import flask
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import pickle
import numpy as np

# Import the necessary modules and libraries

app = Flask(__name__)
app = flask.Flask(__name__, template_folder='template')

# Load the trained model
model = load_model('best_cnn_model.h5')

# Define the cv object for transforming the user input data

@app.route('/')
def page():
    return render_template('fakenews.html')

@app.route('/predict', methods=['POST'])
def home():  
    if request.method == 'POST':
        message = request.form['a']
        data = [message]
        # Transform the user input data using cv
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
    return render_template('fakenews.html', prediction=pred)

'''def predict():
    data=request.get_json()
    inputs=np.array(data[])'''
if __name__ == '__main__':
    app.run(debug=True)