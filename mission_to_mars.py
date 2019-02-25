#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
import re
import requests
from splinter import Browser
import pandas as pd

def scrape_info():

# Retrieve html with requests
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
# Parse html with soup
    soup = bs(response.text, 'html.parser')
    print(soup)

# Retrieve title with soup and save to a variable
    title = soup.find_all('div', class_ = "content_title")
    title
    news_title = "NASA's Opportunity Rover Mission on Mars Comes to End"
# Retrieve paragraph with soup and save to a variable
    paragraph = soup.find(href = re.compile("nasas-opportunity-rover-mission-on-mars-comes-to-end")).text
    paragraph
    news_p = "NASA''s Opportunity Mars rover mission is complete after 15 years on Mars. Opportunity's record-breaking exploration laid the groundwork for future missions to the Red Planet"

# Create a link to html with broswer
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': 'C:\\/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    browser

# View the html with soup
    html = browser.html
    soup = bs(html, 'html.parser')
    print(soup)
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA22831-1920x1200.jpg'

# Use requests to get the html 
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)

# Print the html text using soup
    soup = bs(response.text, 'html.parser')
    print(soup)

# Find first tweet of the page
    soup.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

# Save it to a variable
    mars_weather = 'InSight sol 81 (2019-02-17), high -17/2F, low -95/-138F, pressure at 7.23hPa, winds from the WNW at 12 mph gusting to 37.8 mph Welcome to the Mars Weather team @NASAInSight! https://mars.nasa.gov/insight/weather/ …pic.twitter.com/SH12FvcMfv'

# Find the table containing facts about the planet
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables

# Create a dataframe to show the table
    df = tables[0]
    df.columns = ['Description', 'Value']
    df.set_index('Description', inplace=True)
    df

# Convert dataframe to html
    html_table = df.to_html()
    html_table


# Retrieve title and image url from the inspector and save in a dictionary
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls = [
{"title": "Cerberus Hemisphere",  "img_url": "https://astrogeology.usgs.gov/cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png"},
{"title": "Schiaparelli Hempishere", "img_url":"https://astrogeology.usgs.gov/cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png"},
{"title": "Syrtis Major Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png"},
{"title": "Valles Marineris Hemisphere", "img_url":"https://astrogeology.usgs.gov/cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png"},
]

    scraped_dict =  {'Mars Facts': tables,
                    'URL': hemisphere_image_urls,
                    'Weather': mars_weather,
                    'Featured Image': featured_image_url,
                    'News Title': news_title,
                    'News Body': news_p
               }
    
    browser.quit()

    return scraped_dict



