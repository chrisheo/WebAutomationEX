import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from openpyxl import Workbook

# wb = Workbook(write_only=True)
# ws = wb.create_sheet('플레이 리스트')
# ws.append(['제목','해시태그','좋아요 수','곡수'])

# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,3)
# 사이트 접속하기
driver.get('https://www.naver.com/')
time.sleep(1)
#증권 탭을 클릭
driver.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(3) > a').click()

time.sleep(1)
#스크롤을 끝까지
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
time.sleep(3)
#코스피 값을 가져온다(최대 3초)
KospiValueRaw = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')))
KospiValue = KospiValueRaw.text
print(KospiValue)