"""
Case Study to Self Understand & Explain in Class
------------------------------------------------
The Metropolitan Transportation Authority is North America's largest transportation network, serving a population of 15.3 million people across a 5,000-square-mile travel area surrounding New York City through Long Island, southeastern New York State, and Connecticut.

The MTA network comprises the nation’s largest bus fleet and more subway and commuter rail cars than all other U.S. transit systems combined. The MTA's operating agencies are MTA New York City Transit, MTA Bus, Long Island Rail Road, Metro-North Railroad, and MTA Bridges and Tunnels.

Go to page http://web.mta.info/developers/turnstile.html

Task to be coded :
Try downloading the entire set of data files with a for loop. The code below contains the entire set of code for web scraping the NY MTA turnstile data.
"""


# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

print(len(soup.findAll('a')))   


# To download the whole data set, let's do a for loop through all a tags
# for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
# avoid looping their are too many data files. may take around 2-3 hrs

one_a_tag = soup.findAll('a')[100]
link = one_a_tag['href']
download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
time.sleep(1) #pause the code for a sec

