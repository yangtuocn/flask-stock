from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, jsonify, render_template_string
import os
import quandl
import requests
import simplejson as json
import pandas as pd
from bokeh.plotting import figure, output_file, show, save
from bokeh.embed import components
from jinja2 import Markup

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
    p = figure(x_axis_type = "datetime")
    p.line(list(data['date']), list(data['close']))
    scr, di = components(p)
    return render_template('index.html', plot_script=Markup(scr), plot_div=Markup(di))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
    # app.run()
