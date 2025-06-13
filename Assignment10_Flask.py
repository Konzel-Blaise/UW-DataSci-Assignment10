#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 21:35:13 2025

@author: blazer
"""
#%% opeing databases 

import pandas as pd

#loading original crunchbase data into dataframe
crunch_df = pd.read_csv('crunchbase_odm_orgs.csv')

#loading modified US-Ac database into dataframe
US_df = pd.read_json('USdf.json', orient='records')

#%% Flask call (Question 04)

from flask import Flask

#Write the output to a webpage using Flask
app = Flask("Crunchbase - New York City")

@app.route("/")
def printing_df_constraint():
    return US_df[US_df['city'] == 'New York'].values.tolist()

app.run(host='localhost', port=5005)
        
        
#%% Flask call (Question 05)

from flask import Flask, request

app = Flask('CityCrunch')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        # Display a form for the user to input their name
        return '''<form method="POST">
                    <label for="cityname">Enter name of city to query list of companies based there from the CrunchBase database\n:</label>
                    <input type="text" name="cityname" id="cityname" placeholder="Enter name of city">
                    <button type="submit">Submit</button>
                  </form>'''
    else:
        try:
            city = crunch_df[crunch_df['city'] == request.form['cityname']]['name'].values.tolist()
            return f"Companies in {request.form['cityname']}:\n {city}"
        except KeyError:
            # Handle the case where the 'city' key is not present in the form data
            return "Please enter name of city in the form."

#run to localhost  
app.run(host='localhost', port=5006)    
        
#http://localhost:5006/form
        
        
        