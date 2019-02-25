# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
import pymongo
import mission_to_mars

# Establish connection to mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

# create instance of Flask app
app = Flask(__name__)


@app.route("/")
def index():
    
    # Find record of data from the mongo database
    mars = db.mars_db.find_one()
    # Return template and data
    return render_template("index.html", mars = mars)

# create route that renders index.html template with scraped data

@app.route("/scrape")
def scrape():
    
     # Run the scrape function
    scraped_dict = mission_to_mars.scrape_info()
    for i in scraped_dict:
        scraped_dict = scraped_dict + i
   
    # Update the Mongo database using update and upsert=True
    db.mars_db.insert(scraped_dict)
    
    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
