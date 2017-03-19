from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, jsonify
import os
import quandl
import requests
import simplejson as json
import pandas as pd
from bokeh.plotting import figure, output_file, show

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_query():
    quandl.ApiConfig.api_key = 'oqWh8vNGwgZkRk4PvsyQ'
    data = quandl.get_table('WIKI/PRICES', ticker = request.form['stock'])
    output_file('templates\plot.html')
    p = figure()
    p.line(range(len(data)), list(data['close']))
    # show(p)
    # return redirect(url_for('plot'))
    return render_template('plot.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
    # app.run()
