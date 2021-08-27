from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=webdriver.Chrome('/path/to/chromedriver')
browser.get(START_URL)
time.sleep(10)