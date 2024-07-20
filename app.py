#Implement all this concept by machine learning with flask
# from tensorflow.keras.models import load_models
from flask import Flask, escape, request, render_template
import pickle



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        message = request.form['news']
        data = [message]
        # Transform the user input data using cv
        # vect = cv.transform(data).toarray()
        # pred = model.predict(vect)
        return render_template("result.html", alert="Data submitted successfully!")
    
    else:
        return render_template("prediction.html",alert="Data submitted successfully!")


if __name__ == '__main__':
    app.debug = True
    app.run()