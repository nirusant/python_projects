import temperature_CO2_plotter as tCO2_plot
import numpy as np
from flask import render_template
from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/temp_doc')
def show_documentation_for_temp():
    """
    Renders the htmlcode for the help-page
    """
    return render_template('temperature_CO2_plotter.html')

@app.route('/co2country_change', methods=['POST'])
def handle_country_change():
    """
    If the user want's to change the value of the treshold
    this fucntions processes the appropiate form and makes
    appropriate changes
    """
    treshold = np.double(request.form["treshold"])    
    
    country_table = tCO2_plot.get_table('/CO2_by_country.csv')
    tCO2_plot.process_co2_by_country_table(country_table, treshold)

    return render_template('index.html')

@app.route('/temperature_change', methods=['POST']) 
def handle_temp_change():
    """
    Based on the user's preference, changes are made to alter the plot
    That shows how the temperatures is for a month per year
    """
    x_min = np.double(request.form["time_from"])
    x_max = np.double(request.form["time_to"])
    y_min = np.double(request.form["temp_from"])
    y_max = np.double(request.form["temp_to"])
    month = request.form["month"]


    if month == "All":
        month = ['January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']
    
    temp_table = tCO2_plot.get_table('/temperature.csv')
    tCO2_plot.plot_temp(temp_table, month, [x_min, x_max], [y_min, y_max])
    return render_template('index.html')

@app.route('/CO2_change', methods=['POST'])
def handle_CO2_change():
    """
    Handles the user's decisions regarding making changes to the CO2 by
    year plot. 
    """
    x_min = np.double(request.form["time_from"])
    x_max = np.double(request.form["time_to"])
    y_min = np.double(request.form["co2_from"])
    y_max = np.double(request.form["co2_to"])

    co2_table = tCO2_plot.get_table('/co2.csv')
    tCO2_plot.plot_CO2(co2_table, [x_min, x_max], [y_min, y_max] )

    return render_template('index.html')


@app.route("/")
def show_image():
    """
    Renders the index page
    """
    return render_template('index.html')
    
if __name__ == "__main__":
    """
    Starting the web-server and configuring debug-mode and desired port
    """
    app.run(debug= True, port=5002)
