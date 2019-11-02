#!/usr/bin/env python
# coding: utf-8

# # Step 1 - Scraping

# ## Declare dependencies

# In[ ]:


# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from urllib.parse import urlparse


# ## Initialize Browser Funcion

# In[ ]:


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)




# In[ ]:
def scrape():
    # ## NASA Mars News

    # In[ ]:


    # Run init_browser function and open it
    browser = init_browser()
    # Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # Get Title and Paragrapht Text
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_="article_teaser_body").text

    browser.quit()
    #print(news_title + "\n" +  news_p)


    # ## JPL Mars Space Images - Featured Image

    # In[ ]:


    # Run init_browser function and open it
    browser = init_browser()
    # Visit https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    time.sleep(1)

    # Click in one of the images
    browser.click_link_by_partial_text('Curiosity')
    time.sleep(5)

    # Click in the button for more information
    browser.click_link_by_partial_text('more info')
    time.sleep(1)

    # Get the new url after clicking "more info" and visiting it
    url = browser.url
    browser.visit(url)
    time.sleep(1)

    # Scrape clicked page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the base url to be used with relative paths
    parsed = urlparse(url)
    base_url = parsed.scheme +"://"+ parsed.netloc

    # Get the high resolution image from the accesed page
    featured_image_url = base_url +  soup.find('img', class_="main_image")["src"]

    browser.quit()
    #print(featured_image_url)


    # ## Mars Weather

    # In[ ]:


    # Run init_browser function and open it
    browser = init_browser()
    # Visit https://twitter.com/marswxreport?lang=en
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the image URL

    # Get all the text
    mars_weather_p_a = soup.find("div", class_="js-tweet-text-container").text

    # Get the text in the last part
    mars_weather_a = soup.find("div", class_="js-tweet-text-container").findChildren()[1].text

    # Eliminate the last part of the text
    mars_weather = mars_weather_p_a.replace(mars_weather_a,'')

    browser.quit()
    #print(mars_weather)


    # ## Mars Facts

    # In[ ]:


    # Run init_browser function and open it
    browser = init_browser()
    # Visit https://space-facts.com/mars/
    url = "https://space-facts.com/mars/"

    time.sleep(1)

    # Scrape with Paandas
    tables_df = pd.read_html(url)

    # Get first table with the facts
    mars_facts_df = tables_df[1]

    # Rename column of the dataframe
    mars_facts_df = mars_facts_df.rename(columns={0: "Description", 1: "Value"})


    # Use the titles as index
    mars_facts_df.set_index("Description", inplace=True)

    # Convert the dataframe to html
    mars_facts_html = mars_facts_df.to_html()

    browser.quit()
    #print (mars_facts_html)
    #print (mars_facts_df)


    # ## Mars Hemispheres

    # In[ ]:


    # Run init_browser function and open it
    browser = init_browser()

    # Visit https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Get the base url to be used with relative paths
    parsed = urlparse(url)
    base_url = parsed.scheme +"://"+ parsed.netloc

    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the image URL

    results = soup.find("div", class_="collapsible results")

    # Initialize the Dictionary
    hemisphere_image_urls = []
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of the image
            title = result.find("div").h3.text
            
            # Identify and return link to the high resolution image
            link_parent = base_url + result.a['href']
            
            # Use the link to the page to get the high resolution Page
            link_son = link_parent
            browser.visit(link_son)
            
            time.sleep(1)
            
            # Scrape the socond page into Soup
            html = browser.html
            soup = bs(html, "html.parser")
            
            # Get the image URL of the high resolution URL
            # For getting the Original .tif
            link_son = soup.find("a", text="Original")['href']
            
            # For getting the Sample .jpg
            #link_son = soup.find("a", text="Sample")['href']
            
            # Print results only if title, price, and link are available
            if (title and link_parent):
                #print('-------------')
                #print(title)
                #print(link_parent)
                #print(link_son)

                # Create Dictionary
                url_dict = {}
                url_dict["title"] = title
                url_dict["img_url"] = link_son
                hemisphere_image_urls.append(url_dict)

        except AttributeError as e:
                #print(e)
                pass

    browser.quit()
    #print (hemisphere_image_urls)


    # ## Final Result Dictionary

    # In[ ]:


    # Store data in a dictionary
    scraping_results = {
            "news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "mars_weather": mars_weather,
            "mars_facts_html": mars_facts_html,
            "hemisphere_image_urls": hemisphere_image_urls
            }
    return scraping_results