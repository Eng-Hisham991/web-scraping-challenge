 ### Dependencies ###
import pandas as pd
from bs4 import BeautifulSoup 
import requests
import pandas as pd
from splinter import Browser
import time
import pymongo


def init_browser():
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)
    return Browser("chrome", headless=True)


def scrape():
    mars_data = {}

    ### NASA MARS NEWS ###
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html= browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_data["news_title"] = soup.find('div', class_="list_text").find('div', class_="content_title").get_text()
    mars_data["news_paragraph"] = soup.find("div", class_="article_teaser_body").get_text()
    browser.quit()
    
    ### JPL Mars Space Images - Featured Image ###
    browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.find_by_id('full_image').click()
    xpath= "/html/body/div[3]/div/div[2]/div/div[1]/a[2]"
    time.sleep(0.5)
    browser.find_by_xpath(xpath).click()
    xpath= '//*[@id=\"page\"]/section[1]/div/article/figure/a'
    time.sleep(0.5)
    browser.find_by_xpath(xpath).click()
    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")
    mars_data["featured_image_url"] = soup.find("img")["src"]
    browser.quit()

    ### Mars Weather ###
    url= 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup= BeautifulSoup(response.text, 'lxml')
    mars_weather1 = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()
    mars_weather= mars_weather1.split('pic.twitter.com/U8P9d9J696')[0]
    mars_data["mars_weather"]= mars_weather


    ### Mars Facts ###
    url= 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df= tables[0]
    df.columns=['Parameters', 'Values']
    df.set_index('Parameters', 'Values', inplace=True)
    html_table = df.to_html()
    mars_data["table"] = html_table.replace('\n', '') 

    ### Mars Hemispheres ###
    hemisphere_image_urls = []

        #### Cerberus
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    browser.find_by_xpath(f'//*[@id=\"product-section\"]/div[2]/div[1]/div/a/h3').click()
    time.sleep(1.0)
    browser.find_by_xpath('//*[@id=\"wide-image-toggle\"]').click()
    html= browser.html
    soup= BeautifulSoup(html, 'lxml')
    hemisphere_title= soup.find('h2', class_='title').text
    base_url= 'https://astrogeology.usgs.gov/'
    img= soup.find('img', class_='wide-image')["src"]
    img_url= base_url + img
    cerberus = {'title':hemisphere_title, 'img_url':img_url}
    hemisphere_image_urls.append(cerberus) 
    browser.quit()

     #### Schiaparelli 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    browser.find_by_xpath(f'//*[@id=\"product-section\"]/div[2]/div[2]/div/a/h3').click()
    time.sleep(1.0)
    browser.find_by_xpath('//*[@id=\"wide-image-toggle\"]').click()
    html= browser.html
    soup= BeautifulSoup(html, 'lxml')
    hemisphere_title= soup.find('h2', class_='title').text
    base_url= 'https://astrogeology.usgs.gov/'
    img= soup.find('img', class_='wide-image')["src"]
    img_url= base_url + img
    schiaparelli = {'title':hemisphere_title, 'img_url':img_url}
    hemisphere_image_urls.append(schiaparelli) 
    browser.quit()

     #### Syrtis 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    browser.find_by_xpath(f'//*[@id=\"product-section\"]/div[2]/div[3]/div/a/h3').click()
    time.sleep(1.0)
    browser.find_by_xpath('//*[@id=\"wide-image-toggle\"]').click()
    html= browser.html
    soup= BeautifulSoup(html, 'lxml')
    hemisphere_title= soup.find('h2', class_='title').text
    base_url= 'https://astrogeology.usgs.gov/'
    img= soup.find('img', class_='wide-image')["src"]
    img_url= base_url + img
    syrtis = {'title':hemisphere_title, 'img_url':img_url}
    hemisphere_image_urls.append(syrtis) 
    browser.quit()

    #### Valles Marineris 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)
    browser.find_by_xpath(f'//*[@id=\"product-section\"]/div[2]/div[4]/div/a/h3').click()
    time.sleep(1.0)
    browser.find_by_xpath('//*[@id=\"wide-image-toggle\"]').click()
    html= browser.html
    soup= BeautifulSoup(html, 'lxml')
    hemisphere_title= soup.find('h2', class_='title').text
    base_url= 'https://astrogeology.usgs.gov/'
    img= soup.find('img', class_='wide-image')["src"]
    img_url= base_url + img
    valles_marineris = {'title':hemisphere_title, 'img_url':img_url}
    hemisphere_image_urls.append(valles_marineris) 
    browser.quit()
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_data







if __name__ == "__main__":
    print("\nTesting Data Retrieval...\n")
    print(scrape())




    
