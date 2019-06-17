import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys

def get_arguments(temperature_month = False):
    """
        When running the script from the terminal, this method prompts the
        user with question necesarry to plot the desired plots.

        Input:
            temperature_month, boolean that decides if one extra question
            is required.

        Output:
            list with two elements, indicating the desired interval we
            want to plot on the x-axis
            
            list with two elements, indicating the desired interval we 
            want to plot on the y-axis

            A string with a name of the month we want to plot. 
    """
    min_year = 0
    min_year = int(input(("min_year: ")))

    max_year = 2500
    max_year = int(input(("max_year: ")))

    if temperature_month:
        month = input(("Month: "))
        month = month.title()
    else:
        month = None

    min_yaxis = -100
    min_yaxis = np.double(input(("y-axis, min: ")))

    max_yaxis = 90000
    max_yaxis = np.double(input(("y-axis, max: ")))
                        
    return [min_year, max_year], [min_yaxis, max_yaxis], month

def plot_temp(temperature_table, month, years, yaxis):
    """
        Plots a dataframe of the temperature table based on some
        specifiactions.
        The plot then gets saved in the static folder.

        Input:
            temperature_table, the dataframe we want to plot.

            month, String telling which month to plot.

            years, a list with two elements deciding the range of years
            we need to plot

            yaxis, decides the range of the y-axis of the plot

        Output:
            none
    """

    temperature_plot = temperature_table.plot(x= 'Year',
                                              y= month,                  
                                              xlim= years,
                                              ylim= yaxis,  
                                              title = "Temperature/Month")
    
    #Saving the figure so that the web-page cane use the image
    plt.savefig('static/temp.png')  
    
def process_temperature_table(temperature_table):
    """
        Processes the information from temperature.csv
        and makes a plot based on the user's preference.

        Input:
            temperature_table, table containing information on 
            how the temperature changes over years for each month

        Output:
            none

    """
    temperature_year_table = temperature_table['Year']
    #Finding the smalest and the largest value on th x-axis
    min_temperature_year = temperature_year_table.nsmallest(1).values[0] 
    max_temperature_year = temperature_year_table.nlargest(1).values[0]
    print("Available years:", min_temperature_year, "-", max_temperature_year)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    #For each month the y-axis is going to vary.
    #Displaying the range where there is data for each month.  	
    for month_i in months:
        temperature_month_table = temperature_table[month_i]
        min_temperature_month = temperature_month_table.nsmallest(1).values[0]
        max_temperature_month = temperature_month_table.nlargest(1).values[0]
        print("Range in y-axis for",month_i,":", min_temperature_month, "to",
              max_temperature_month)
	    	              
    # Geting arguments     
    years, yaxis, month = get_arguments(True)
    
    if month not in months:
        print("Desired month not found")
        month = months
    
    #Sends the table for actual ploting
    plot_temp(temperature_table, month, years, yaxis)

def plot_CO2(co2_table, range_of_year, yaxis):
    """
        Makes a plot based on  the co2-dataframe.
        The plot then gets saved to the static folder.

        Input:
            co2_table, dataframe containing the necessary data to make
            a plot.

            range_of_year, list containg two elements decides the x-axis
            of the plot.

            yaxis, list containing two elements, decides the y-axis of
            the plot

        Output:
            none
    """
    co2_plot = co2_table.plot(x= 'Year',
                              y= 'Carbon',
                              xlim= range_of_year,
                              ylim= yaxis,
                              title= "CO2/years")

    plt.savefig('static/co2.png')

def process_co2_table(co2_table):
    """
        Processes the information from co2.csv
        and makes a plot based on the user's preference.

        Input:
            co2_table, dataframe object containing information on co2 levels
            for each year. 

        Output:
            none
    """
    #Finds the smallest and largest years in the table
    co2_year_table = co2_table['Year']
    min_co2_year = co2_year_table.nsmallest(1).values[0]
    max_co2_year = co2_year_table.nlargest(1).values[0]

    #Finds the smallest and the larges carbon value in the table
    co2_carbon_table = co2_table['Carbon']
    min_co2_carbon = co2_carbon_table.nsmallest(1).values[0]
    max_co2_carbon = co2_carbon_table.nlargest(1).values[0]
	
    #Displaying information to user
    print("Available years:", min_co2_year, "-", max_co2_year)
    print("Available range in y-axis", min_co2_carbon, "to", max_co2_carbon)
    
    #Gets arguments from user
    range_of_year, yaxis, month = get_arguments(False)  
    
    plot_CO2(co2_table, range_of_year, yaxis)

def process_co2_by_country_table(co2_by_country_table, treshold = np.nan):
    """
        Instead of displaying the data given as a bar-plot, I have decided
        to show the data as an image/heatmap.
        The y-axis represents all the countries, while the x-axis are the 
        years 1960 to 2016.
        Each pixel's intensity represents the CO2-value

        Input:
            co2_by_coyntry_table, a dateframe object containing information
            on co2 levels for each country by year.

            treshold, double telling where to set the CO2-level.
            If the argument is given as a np.nan this indicates that a 
            treshold is need by the user.

        Output:
            none

    """
    #Changing indexing
    df2 = co2_by_country_table.set_index("Country Name", drop = False)
    df3 = df2.loc[:, "1960":"2016"]

    countries = df2.loc[:,"Country Code"]
    years = df2.loc["Aruba","1960":"2016"].index.values.tolist()

    if str(treshold) == "nan":
        print("Please select a treshold:")
        print("Minimum value:", np.nanmin(df3.values))
        print("Maximum value:", np.nanmax(df3.values))
        treshold = np.double(input(("treshold: ")))
    
    #Using the treshold value to decide what to plot
    df3_tresholded = df3[df3 > treshold]
    vals = df3_tresholded.values

    #The lines after this are configuring the plot's 
    #figure and axex to make them look visually "better".
    fig, ax = plt.subplots()
    im = plt.imshow(vals, aspect=0.5)

    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years)
    ax.set_yticks(np.arange(len(countries)))
    
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=2, ha="right", rotation_mode="anchor")
    plt.setp(ax.get_yticklabels(), fontsize=1, ha="right", rotation_mode="anchor")
    plt.colorbar()
    ax.xlabel = "year"
    ax.ylabel = "Country #"
    plt.savefig('static/global_co2.png', bbox_inches="tight", dpi=400)

def get_table(desired_file):
    """
        Based on the input string the method opens and rads a cvs file
        and converts it to a dataframe object.
    
        Input:
            desired_file,a string with the name of of the file in 
            the directory 

        Output:
            pandas.dataframe object
            
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_location = dir_path + desired_file
    
    return pd.read_csv(file_location)

def main():
    """
        Prompts the user with questions on which plot to make.
        After producing a plot, the functions displays the plot
        
        Input:
            none

        Output:
            none
        
    """

    type_of_plot = ""
    print("Please select desired plot")
    type_of_plot = input(("temp/co2/co2bycountry: "))
    type_of_plot = type_of_plot.lower()
    
    if type_of_plot == "temp":
        temperature_table = get_table('/temperature.csv')
        process_temperature_table(temperature_table)
    
    elif type_of_plot == "co2":
        co2_table = get_table('/co2.csv')
        process_co2_table(co2_table)

    elif type_of_plot == "co2bycountry":
        co2_by_country_table = get_table('/CO2_by_country.csv')
        process_co2_by_country_table(co2_by_country_table)

    else:
        print("Desired option is not valid")
        sys.exit()
    
    #ploting the available plot
    plt.show()

def help_win():
    """
        Help screen for users

        Input:
            none

        Output:
            none

    """
    print('Help screen for temperature_CO2_plotter:')
    print('Usage: python3 temperature_CO2_plotter.py')
    print('Be sure that the files co2.csv, temperature.csv and', 
          'CO2_by_country.csv are in the present folder')
    print('When runing this script you are going to be prompted with several questions',
          'these questions will make the proper decisons based on your answers')


if __name__ == '__main__':
    """
        Main function, searches for the proper files and runs the
        appropiate functions.
        The assignement does not specifiy if the files necessary to run
        this script should be provided as arguments or not.
        I have decided to find the csv files necessary by searching for
        them in the directory where the script resides. 

        Input: 
            none

        Output:
            none
    """
    if(len(sys.argv) > 1):
        if(sys.argv[1] == '--help'):
            help_win()
            sys.exit()
        else:
            help_win()
            sys.exit()

    #Finding the path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    co2_location = dir_path + '/co2.csv'
    temperature_location = dir_path + '/temperature.csv'
    co2_by_country_location = dir_path + '/CO2_by_country.csv' 
    
    #checking if the files exist in the current dir.
    if (os.path.isfile(co2_location) and
       os.path.isfile(temperature_location) and 
       os.path.isfile(co2_by_country_location)):

        print('Files found')
        main()
    else:
        print('Files not found, please place co2.csv, ' 
              'temperature.csv and CO2_by_country.csv'
              'in current directory')
        sys.exit()
