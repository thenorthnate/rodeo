# @Author: Nathan North
# @Org: GE Transportation
# @Project: Series X
# Copywrite - all rights reserved. DO NOT COPY OR DISTRIBUTE.

from flask import Flask, render_template, redirect, url_for, request, Response, session
import os
import datetime

from app.main.Main import Main
from app.data_manager.DataManager import DataManager

appMain = Main()
dM = DataManager()

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'Rodeo'
app.config['UPLOAD_FOLDER'] = appMain.datadir
app.config['ALLOWED_EXTENSIONS'] = appMain.extensions
port = os.getenv("PORT")
if port is None:
    port = 5000


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("POST")
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 5, 20, 13, 6, 7]
    return render_template('home.html', x=x, y=y)


@app.route('/data_manager', methods=['GET', 'POST'])
def data_manager():
    if request.method == 'POST':
        dM.import_new_file(request.files)
    return render_template('data_manager.html', showData=dM.showData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=False)
