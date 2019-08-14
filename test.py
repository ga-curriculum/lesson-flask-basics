# import json, requests, time
# import mysql.connector as mysql
from flask import Flask, request, Response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/json')
def json():
    # TODO
    args = request.form
    print(dict(args))
    return Response(200)

@app.route('/hc_page')
def hc_page():
    return '<html><head></head><body><h1>This is a hard coded page!</h1><p>Here is some hard coded content. Isn\'t it pretty?</p></body></html>'

@app.route('/form')
def final_form():
    # TODO
    return render_template('./form.html')



@app.route('/predict')
def make_predictions():
    # load in form data
    # load in pickled model
    # make predictions
    return render_template('./results.html', 
        pred_class = pred_class,
        proba = proba)


if __name__ == '__main__':
    app.run(debug=True)








