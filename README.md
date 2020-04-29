# web-scraping-challenge

This work has three files:
1\ Jupyter Notebook file (Mission_to_Mars.ipynb)
2\ Python file (scrape_mars.py)
3\ Python file (app.py)
4\ HTML file (index.html)

The describtion of the work is as follows:
- Import the dependencies.
- Firing up chrome webdrive.
- Scraping the dtata from the following sources:
	- Nasa Mars News (https://mars.nasa.gov/news/)
	- JPL Mars Space Images (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
	- Mars Weather (https://twitter.com/marswxreport?lang=en)
	- Mars Facts (https://space-facts.com/mars/)
	- Mars Hemispheres (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

- Transformed the codes used in jupyter notebook to python and placed them in a function called scrape
  which is doing the srape process and return the result in a list called mars_data.

- In the app.py:
	- Import the dependencies.
	- Defining the app.
	- Set the configurations to connect to mongoDB.
	- In the app.route passed the mars_data from mogoDB and rendering it to index.html.
	- In app.route("/scrape") begin the scraping  by calling the scrape_mars file and use 
	  the function scrape to do the scraping.
	- Then update the mars_data in mongoDB with the results from the scraping.

- In the index.html:
	- set the definiton of html needed to create the web page.
	- assign the scraped date in doble {{ }} as variables to the needed section.
	- Use the for loop i.e. {{%for %}} ending with {{%endfor%}}.