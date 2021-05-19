import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

#Driver initiation
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

#Get site
driver.get("https://www.mangoplate.com/top_lists/samgyupsal_top25")
driver.implicitly_wait(10)
# 이 때 알아서 광고 없애주세요~

# 카테고리에서 새 탭 열기
for i in range(9,11):
    from selenium.webdriver.common.keys import Keys
    target = driver.find_element_by_xpath('//*[@id="contents_list"]/ul/li['+str(i)+']/div/figure/figcaption/div/span/a')  # 클릭하고 싶은 것 선택
    target.send_keys(Keys.CONTROL +"\n")

for i in range(1,3):
    #switch tap
    driver.switch_to.window(driver.window_handles[i]) 

    # 스크롤 내리기, 더보기 찾기
    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(0.5)
    some_tag = driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[3]/div[2]")
    action = ActionChains(driver)

    while True:
        try:
            action.move_to_element(some_tag).perform()
            driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[3]/div[2]").click()
            time.sleep(2)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        except:
            break

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "lxml")
    #with open ("review.html", "w", encoding = "utf8") as f:
    #    f.write(soup.prettify())

    #식당 이름
    name = soup.find("h1", attrs = {"class" : "restaurant_name"}).get_text()

    #리뷰 가져오기
    reviews = soup.find_all("p", attrs = {"class" : "RestaurantReviewItem__ReviewText"})

    #리뷰 파일 만들기
    f = open(name + '.txt', 'w', encoding="utf8")

    for idx, review in enumerate(reviews):
        f.write(review.get_text().strip() + '\n')
    
    
    
