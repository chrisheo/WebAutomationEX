import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
#엑셀파일 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('코스타그램')
ws.append(['이미지 주소','내용','해시태그','좋아요 수','댓글 수'])

driver = webdriver.Chrome()

#사이트 접속
driver.get('https://workey.codeit.kr/costagram/index')
driver.implicitly_wait(3)
#로그인 과정
driver.find_element_by_css_selector('.top-nav__login-link').click()
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input').send_keys("codeit")
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__password-input').send_keys("datascience")
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-button').click()
time.sleep(1)
#스크롤을 끝까지 내리기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(1)
#포스트 클릭하고 끄고
posts = driver.find_elements_by_css_selector('.post-list__post')

for post in posts:
    post.click()
    driver.implicitly_wait(1)
    #필요한 내용 추출
    images_URL = "https://workey.codeit.kr" + driver.find_element_by_css_selector('.post-container__image').get_attribute("style").split("\"")[1]
    content = driver.find_element_by_css_selector(".content__text").text
    hashtags = driver.find_element_by_css_selector(".content__tag-cover").text
    likes = driver.find_element_by_css_selector(".content__like-count").text
    comment = driver.find_element_by_css_selector(".content__comment-count").text
    #추출한 내용을 엑셀파일에 추가
    ws.append([images_URL,content,hashtags,likes,comment])
    driver.find_element_by_css_selector('#app > div > div > div > button').click()
    driver.implicitly_wait(1)
driver.quit()
wb.save("코스타그램.xlsx")