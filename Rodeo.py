# Nathan North
# Rodeo Data Mining
# https://plot.ly/javascript/

# from flask import Flask, render_template, redirect, url_for, request, Response, session
import flask
import os
from app.main.Main import Main

appMain = Main()

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'Rodeo'
app.config['UPLOAD_FOLDER'] = appMain.datadir
app.config['ALLOWED_EXTENSIONS'] = appMain.extensions
port = os.getenv("PORT")
if port is None:
    port = 5000


@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        print("POST")
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 5, 20, 13, 6, 7]
    return flask.render_template('home.html', x=x, y=y)


@app.route('/import_data', methods=['GET', 'POST'])
def import_data():
    if flask.request.method == 'POST':
        # appMain.import_new_file(request.files)
        print("post")
    return flask.render_template('import.html')


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    # appMain.test_plot()
    # data = appMain.tmpData
    data = {"0": [1, 2, 3], "1": [50, 4, 21]}
    return flask.render_template('plot.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=False)
