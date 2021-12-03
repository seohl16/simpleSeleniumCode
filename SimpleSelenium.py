from bs4 import BeautifulSoup
import os
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json 
import time

# Instantiate an Options object
# and add the "--headless" argument
opts = Options()
opts.add_argument(" --headless")
# If necessary set the path to you browser’s location
# opts.binary_location= os.getcwd() +'\\GoogleChromePortable\GoogleChromePortable.exe'
# Set the location of the webdriver
chrome_driver = './chromedriver_mac'
# Instantiate a webdriver
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

# Load the HTML page
# To scrape a url rather than a local file 
# just do something like this
url = 'https://www.naver.com/'

driver.get(url)

# Scroll page to load whole content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page
    time.sleep(2)
    # Calculate new scroll height and compare with last height.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

htmltext = driver.page_source
soup = BeautifulSoup(htmltext, 'lxml')

# if you print(soup), whole html will be printed

# code where you save data into json
tempdic = {}
mainapi = []
elem = soup.find('a', {'class':'logo_naver'})
tempdic['id'] = elem.find('span').text
print(tempdic)
mainapi.append(tempdic)

# saving json into output file needs json.dumps()
# for UNICODE, used ensure_ascii flag
with io.open('new.txt', 'w', encoding='utf-8') as ht:
    for i in mainapi:
        ht.write(json.dumps(i, ensure_ascii=False))
        ht.write('\n')

driver.quit()