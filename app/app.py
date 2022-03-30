from flask import Flask, render_template

import helper

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<value_id>', methods=['GET', 'POST'])
def show_value(value_id: str):
    value = helper.square(int(value_id))
    return render_template('value.html', value_id=value_id, value=value)


@app.route('/search', methods=['GET'])
def search():
    NotImplementedError("Not implemented")
