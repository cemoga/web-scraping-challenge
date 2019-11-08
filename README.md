# Necessary Steps to Run all the Project

1. - Install or have installed these libraries in your Git Enviroment:
        -   pandas
        -   splinter
        -   bs4
        -   urllib.parse
        -   time
        -   flask
        -   flask_pymongo
2. - Download or have downloaded the chromedriver.exe in the path "/usr/local/bin/chromedriver" for Mac Users
2. - Run the `Mongo daemon`, in one terminal window run `~/mongodb/bin/mongod`. This will start the Mongo server.
3. - Run the `\Missions_to_Mars\app.py` file
4. - Open your browser and visit the url: http://127.0.0.1:5000/

# File Description
### - `Missions_to_Mars\`
#### - `app.py`
- Contains Python app that uses the flask library that runs the server in the  the url: `http://127.0.0.1:5000/` and calls the `Missions_to_Mars\templates\index.html` file
#### - `mission_to_mars.ipynb` 
- Contains the Jupyter Notebook with the explained code for scrapping the different urls used in the project
#### - `scrape_mars` 
- Contains Python routine used and called by the main routine `\Missions_to_Mars\app.py` and it is called by pressing the `Scrape New Data`button in the url: in the url: `http://127.0.0.1:5000/`
#### -  `ScreenShots`
- `1. Initial.png` - It is the screenshot of the initial state of the `Missions_to_Mars\templates\index.html` file `before` running the `Scrape New Data` button which calls the `\Missions_to_Mars\scrape_mars.py` routine

![Initial](Missions_to_Mars/ScreenShots/1_Initial.png "Page before running the `Scrape New Data`")

- `2. Final.png` - It is the screenshot of the final state of the `Missions_to_Mars\templates\index.html` file `after`running the `Scrape New Data`button which calls the `\Missions_to_Mars\scrape_mars.py` routine

![Initial](Missions_to_Mars/ScreenShots/2_Final.png "Page before running the `Scrape New Data`")

#### -  `Templates`
- `index.html` - Contains the html and css codes necessary for the presentation of the scrapped data obtained by `Scrape New Data`button which calls the `\Missions_to_Mars\scrape_mars.py` routine