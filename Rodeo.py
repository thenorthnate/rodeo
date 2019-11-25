# Nathan North
# Rodeo Data Mining
# https://plot.ly/javascript/

# from flask import Flask, render_template, redirect, url_for, request, Response, session
import flask
import os
from app.main.Main import Main

m = Main()

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'Rodeo'
app.config['UPLOAD_FOLDER'] = m.pwd + "/data/"
app.config['ALLOWED_EXTENSIONS'] = m.extensions
port = os.getenv("PORT")
if port is None:
    port = 5000


@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        if "fileUploadButton" in flask.request.form:
            m.dm.upload_file(flask.request)
    return flask.render_template('home.html')


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if flask.request.method == 'POST':
        if "fileUploadButton" in flask.request.form:
            m.dm.upload_file(flask.request)
    # m.test_plot()
    # data = m.tmpData
    data = {"0": [1, 2, 3], "1": [50, 4, 21]}
    return flask.render_template('plot.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=False)
