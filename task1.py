import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# HTML 코드 받아오기
driver = webdriver.Chrome()
driver.get('https://workey.codeit.kr/orangebottle/index')

branch_infos = []
# 모든 지점에 대한 태그 가져오기
branches = driver.find_elements_by_css_selector('div.branch')
for branch in branches:
    branch_name = branch.find_element_by_css_selector('p.city').text
    address = branch.find_element_by_css_selector('p.address').text
    phone_number = branch.find_element_by_css_selector('span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])
driver.quit()
# 출력 코드
print(branch_infos)
