from flask import request, Flask, render_template  # Import necessary modules from Flask
import webbrowser  # Import webbrowser module to open URLs
import json  # Import JSON module to handle JSON data
import dbms  # Import a custom module named dbms
import re  # Import regular expressions module for string operations

app = Flask(__name__)  # Create a Flask application instance

@app.route("/home")  # Define a route for the URL "/home"
@app.route("/")  # Define a route for the root URL "/"
def home():
    return render_template("home.html")  # Render the "home.html" template when this route is accessed

@app.route("/tag")  # Define a route for the URL "/tag"
def tag():
    value = dbms.gettags()  # Call the gettags function from the dbms module to get tags
    data = json.dumps(value)  # Convert the retrieved tags to JSON format
    return render_template(template_name_or_list="tag.html", tag=data)  # Render the "tag.html" template with the tag data

@app.route('/tag/<tag_id>')  # Define a route for the URL "/tag/<tag_id>", where <tag_id> is a variable part of the URL
def city_select(tag_id):
    value = dbms.getcitys(tag_id)  # Call the getcitys function from the dbms module to get cities for the given tag_id
    data = json.dumps(value)  # Convert the retrieved cities to JSON format
    return render_template("activity.html", tag=data, t_name=tag_id)  # Render the "activity.html" template with the city data and tag_id

@app.route('/city/<city>')  # Define a route for the URL "/city/<city>", where <city> is a variable part of the URL
def display_city(city):
    value = dbms.get_destination_info(city)  # Call the get_destination_info function from the dbms module to get destination info for the given city
    data = json.dumps(value)  # Convert the retrieved destination info to JSON format
    c_name = re.sub(r'\(.*?\)', '', city).strip()  # Remove any text within parentheses and strip whitespace from the city name
    value1 = [city.split()[0]+str(x) for x in range(1,5)]  # Generate a list of city slide names based on the city name
    data1 = json.dumps(value1)  # Convert the city slide names to JSON format
    return render_template("city.html", city_slide=data1, city=c_name, city_detail=data)  # Render the "city.html" template with the city slides, cleaned city name, and city details

@app.route("/<click>")  # Define a route for any URL with a single variable part
def other(click):
    return render_template(template_name_or_list=f"{click}.html")  # Render the template named "<click>.html", where <click> is the variable part of the URL

if __name__ == '__main__':  # Check if the script is being run directly
   webbrowser.open("http://127.0.0.1:5000/")  # Open the default web browser with the local URL of the application
   app.run()  # Run the Flask application