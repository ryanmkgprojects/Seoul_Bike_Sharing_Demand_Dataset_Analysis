from flask import Flask

from flask import Blueprint, render_template, request,jsonify, redirect, url_for
import joblib
import pandas as pd

views = Blueprint(__name__, "views")




@views.route("/")
def home():
    return render_template('index.html', name = 'Hoe')



@views.route("/profile")
def profile():
    return render_template('profile.html')

@views.route("/json")
def get_json():
    
    return jsonify({'name' :'tim', 'coolness':10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    
    return redirect(url_for("views.get_json"))


@views.route('/model1', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        date = request.form.get("date")
        hour = request.form.get("hour")
        temperature = request.form.get("temperature")
        humidity = request.form.get("humidity")
        wind_speed = request.form.get("wind_speed")
        dew_point_temperature = request.form.get("dew_point_temp")
        snowfall = request.form.get("snowfall")
        visibility = request.form.get("visibility")
        solar_radiation = request.form.get("solar_radiation")
        rainfall = request.form.get("rainfall")
        seasons = request.form.get("seasons")
        holiday = request.form.get("holiday")
        Year = request.form.get("year")
        Weekday = request.form.get("weekday")
        print(type(Weekday))
        
        
        # Put inputs to dataframe
        '''X = pd.DataFrame([[date, hour,temperature, humidity, wind_speed,dew_point_temperature, snowfall,visibility,
         solar_radiation, rainfall, seasons, holiday]],
        
         columns = ["Date", "Hour", "Temperature(C)", "Humidity(%)", "Wind speed (m/s)",  "Dew point temperature(C)",
          "Snowfall (cm)","Visibility (10m)", "Solar Radiation (MJ/m2)", "Rainfall(mm)",
            "Seasons", "Holiday", "Functioning Day"])'''
        
        X = pd.DataFrame([[ temperature, humidity, wind_speed,dew_point_temperature, snowfall,visibility,
         solar_radiation, rainfall, seasons, holiday, Year, Weekday]],
        
         columns = [ "Temperature(C)", "Humidity(%)", "Wind speed (m/s)",  "Dew point temperature(C)",
          "Snowfall (cm)","Visibility (10m)", "Solar Radiation (MJ/m2)", "Rainfall(mm)",
            "Seasons", "Holiday", "Year", "Weekday"])
        
        # Get prediction
        prediction = float(clf.predict(X)[0])
        
    else:
        prediction = ""
        
    return render_template("gfg.html", output = prediction)