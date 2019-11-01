from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    #avg_temps = soup.find('div', id='weather')

    news_title = soup.find('div', _class="content_title")

    #<div class="content_title"><a href="/news/8529/mars-insights-mole-has-partially-backed-out-of-its-hole/" target="_self">Mars InSight's Mole Has Partially Backed Out of Its Hole</a></div>

    # Get the min avg temp
    #min_temp = avg_temps.find_all('strong')[0].text

    # Get the max avg temp
    #max_temp = avg_temps.find_all('strong')[1].text

    # BONUS: Find the src for the sloth image
    #relative_image_path = soup.find_all('img')[2]["src"]
    #sloth_img = url + relative_image_path

    # Store data in a dictionary
    #costa_data = {
    #    "sloth_img": sloth_img,
    #    "min_temp": min_temp,
    #    "max_temp": max_temp
    #}

    # Close the browser after scraping
    browser.quit()

    # Return results
    #return costa_data
    return news_title

scrape_info()
print (news_title )