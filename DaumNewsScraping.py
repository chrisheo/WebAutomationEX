import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
#Driver initiation
driver = webdriver.Chrome()

#Get site
driver.get("https://news.daum.net/")
driver.implicitly_wait(3)
#Scroll to End line
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scroll to scrollheight
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # wait for new info
    time.sleep(0.5)

    # check height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(1)
ThumbnailHeadlines = driver.find_elements_by_css_selector("#cSub > div > ul > li")
Headlines = driver.find_elements_by_css_selector("#mArticle > div.box_headline > ul > li")
Headlines = ThumbnailHeadlines + Headlines
for headline in Headlines:
    print(headline.text.strip())
