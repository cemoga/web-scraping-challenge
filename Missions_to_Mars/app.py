from flask import Flask, render_template
#import mission_to_mars
import pymongo


# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars.drop()


db.mars.insert_many(
    [ 
    {'news_title': "Mars InSight's Mole Has Partially Backed Out of Its Hole",
 'news_p': "After making progress over the past several weeks digging into the surface of Mars, InSight's mole has backed about halfway out of its hole this past weekend.",
 'featured_image_url': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23378_hires.jpg',
 'mars_weather': '\nInSight sol 330 (2019-10-31) low -101.8ºC (-151.3ºF) high -24.8ºC (-12.6ºF)\nwinds from the SSE at 5.4 m/s (12.2 mph) gusting to 20.8 m/s (46.5 mph)\npressure at 7.00 hPa\n',
 'mars_facts_html': '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Value</th>\n    </tr>\n    <tr>\n      <th>Description</th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Equatorial Diameter:</th>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>Polar Diameter:</th>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>Mass:</th>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>Moons:</th>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>Orbit Distance:</th>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>Orbit Period:</th>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>Surface Temperature:</th>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>First Record:</th>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>Recorded By:</th>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>',
 'hemisphere_image_urls': [{'title': 'Cerberus Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif'},
  {'title': 'Schiaparelli Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif'},
  {'title': 'Syrtis Major Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif'},
  {'title': 'Valles Marineris Hemisphere Enhanced',
   'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif'}]}
    ]
)



