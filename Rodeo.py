# Nathan North
# Rodeo Data Mining
# https://plot.ly/javascript/

from flask import Flask, render_template, redirect, url_for, request, Response, session
import os

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


@app.route('/import_data', methods=['GET', 'POST'])
def import_data():
    if request.method == 'POST':
        dM.import_new_file(request.files)
    return render_template('import.html')


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    dM.test_plot()
    data = dM.tmpData
    print(data)
    return render_template('plot.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=False)
