from flask import Flask, jsonify, render_template, request, session
import pandas as pd # data wrangling

from bokeh.plotting import figure
from bokeh.embed import components

from bokeh.plotting import figure, output_file, show, Column
from bokeh.models import DataTable, TableColumn, PointDrawTool, ColumnDataSource

from bokeh.events import SelectionGeometry
from bokeh.models import ColumnDataSource, CustomJS, Rect
from bokeh.plotting import figure, output_file, show

import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, Div, Row
from bokeh.events import *
from math import pi

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pk'


@app.route('/informe')
def informe():

    beta=session["beta"]
    phi=session["phi"]
    alpha=session["alpha"]
    P=session["P"]

    #  devuelta navegador
    informe=render_template('notebook.html', phi=phi, alpha=alpha, beta=beta, P=P)
    return jsonify( informe=informe)





@app.route('/formulario')
def formulario():
    # datos del navegador
    beta = request.args.get('inclinacion', 0, type=int)
    alpha = request.args.get('orientacion', 0, type=int)
    phi = request.args.get('latitud', 0, type=float)

    # calculos


    if beta > 15:
        # P=   100*(1.2*10**(-4)*(beta-phi+10)**2+3.5*10**(-5)*alpha**2),2)
        P =  100*((1.2*10**(-4)*(beta-phi+10)**2)+(3.5*(10**(-5))*alpha**2))
        P=round(P,2)
    elif beta <= 15:
        P =  100*((1.2*10**(-4)*(beta-phi+10)**2))
        P=round(P,2)


    #  figura

    # 
    session["beta"]=beta
    session["alpha"]=alpha
    session["phi"]=phi
    session["P"]=P

    return jsonify( P=P)



@app.route('/infor')
def infor():
    return render_template('informe.html')



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8000,debug=True)
    