# Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this projectt, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

### Overveiw

This project has three files as follow:
	1\ Mission_to_Mars (Jupyter Notebook file).
	2\ Scrape_mars (Python file).
	3\ App (Python file).
	4\ Index (HTML file).


### Steps

## Step 1 - Scraping

  Overview:
  Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, Requests & Splinter.

	* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of our scraping and    analysis tasks. 

# NASA Mars News

	* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that you can reference later.


# JPL Mars Space Images - Featured Image

	* Used the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

	* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

	* Used the image url to the full size `.jpg` image.

	* Saved a complete url string for this image.


# Mars Weather

	* Used the Mars Weather twitter account (https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called `mars_weather`.


# Mars Facts

	* Used the Mars Facts webpage (https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

	* Used Pandas to convert the data to a HTML table string.


# Mars Hemispheres

	* Used the USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

	* Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.

	* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. A Python dictionary was used to store the data using the keys `img_url` and `title`.

	* Appended the dictionary with the image url string and the hemisphere title to a list. This list contained one dictionary for each hemisphere.


## Step 2 - MongoDB and Flask Application

	Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

	* Started by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that would execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

	* Created a route called `/scrape` that would import the `scrape_mars.py` script and call it a `scrape` function.

  	* Stored the return value in Mongo as a Python dictionary.

	* Created a root route `/` that would query the Mongo database and pass the mars data into an HTML template to display the data.

	* Created a template HTML file called `index.html` that would take the mars data dictionary and display all of the data in the appropriate HTML elements. 




### Copyright

Hisham Elhassan © 2020. All Rights Reserved.