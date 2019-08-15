import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, Response, render_template, jsonify

app = Flask(__name__)

# route 1: hello world
@app.route('/')
def home():
    return 'Hello, world!'

# route 2: return a 'web page'
@app.route('/hc_page')
def hc_page():
    return '<html><body><h1>This is a hard coded page!</h1><p>Here is some hard-coded content. Isn\'t it pretty?</p></body></html>'

# route 3: return some data
@app.route('/hc_page.json')
def json():
    best_stuff = {
        'coast': 'west',
        'sandwich': 'el paseo',
        'movie': 'toy story'
    }
    
    return jsonify(best_stuff), 200

# route 4: show a form to the user
@app.route('/form')
def form():
    return render_template('form.html')

# route 5: accept the form submission and do something fancy with it
@app.route('/submit')
def make_predictions():
    # load in form data
    user_input = request.args

    data = np.array([
        int(user_input['TV']),
        int(user_input['radio']),
        int(user_input['newspaper'])
    ]).reshape(1, -1)

    # load in pickled model
    model = pickle.load(open('model.p', 'rb'))

    # make predictions
    prediction = model.predict(data)[0]

    return render_template('results.html', prediction=round(prediction, 2))

    # return render_template('results.html',
    #                         pred_class=pred_class, 
    #                         proba=proba)


if __name__ == '__main__':
    app.run(debug=True)








