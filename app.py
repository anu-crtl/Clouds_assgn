from flask import Flask
import numpy as np
app = Flask(_name_)

N_arr = [1, 10, 100, 1000, 10000, 100000, 1000000]

def integral_func(lower, upper): 
    integral = []
    for N in N_arr:
        width = (upper - lower)/N     #calculating the width of each rectangle
        mid_list = np.arange(lower+width/2, upper, width)  #creating list of middle of each rectangle
        areas = np.abs(np.sin(mid_list))*width         #calculating the areas of all rectangles
        integral.append(np.sum(areas))
    return integral

@app.route("/")
def default_integral():
    lower = 0
    upper = 3.14
    results = integral_func(lower,upper)
    return '''<p><b>This is default integration results for 0 and 3.14  : </b> {} </p>'''.format(results)

@app.route("/integral/<lower>/<upper>")
def integral(lower,upper):
    lower = float(lower) 
    upper = float(upper) 
    results = integral_func(lower, upper)
    return '''<p><b>Integration results : </b> {} </p>'''.format(results)