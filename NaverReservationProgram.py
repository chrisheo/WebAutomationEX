import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyperclip
from openpyxl import Workbook
#Driver initiation
driver = webdriver.Chrome()


#Get site
driver.get("https://booking.naver.com/booking/13/bizes/422463")
driver.implicitly_wait(3)

#자동입력 방지 우회
def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)
#Login process
driver.find_element_by_css_selector("#gnb_login_button > span.gnb_txt").click()

clipboard_input('//*[@id="id"]',"jftj")
clipboard_input('//*[@id="pw"]',"wowowowo")

driver.find_element_by_xpath('//*[@id="log.login"]').click()

# 브라우저 등록 클릭
driver.find_element_by_xpath('//*[@id="new.save"]').click()

time.sleep(30)
