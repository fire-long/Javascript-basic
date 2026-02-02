# 크롤링 코드 작성
# 네이버에 키워드를 검색했을 때, 이미지 탭에 보이는 첫번째 이미지 주소를 크롤링
import time
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def crawling_img(senddata):    
    # 1. 크롬창 띄워주기
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) 
    #실행 후 브라우저 안 닫기 옵션 
    #Chrome 창은 남아있고 드라이버만 종료!!
    
    driver = wb.Chrome()
    
    # 2. 네이버 페이지 이동하기
    driver.get('https://www.naver.com')
    time.sleep(1.2)
    
    # 3. 검색창에 키워드 검색
    search = driver.find_element(By.ID, 'query')
    search.send_keys(senddata)
    search.send_keys(Keys.ENTER)# driver.find_element(By.CSS_SELECTOR, 'span.ico_btn_search_svg').click()
    time.sleep(1.5)
    
    # 4. 이미지 탭으로 이동
    image_tab = driver.find_element(By.LINK_TEXT, '이미지').click() #driver.find_elements(By.CSS_SELECTOR, 'a.tab')[0].click()
    
    # 5. 첫번째 이미지 태그 가져오기 -> 주소값(src)만 꺼내와주기
    driver.implicitly_wait(5)#time.sleep()의 대체안
    # imgs = driver.find_elements(By.CSS_SELECTOR, 'div.thumb img')
    # first_img = imgs[0].get_attribute('src')
    img = driver.find_element(By.CSS_SELECTOR, '#main_pack > section > div.api_subject_bx._fe_image_tab_grid_root.ani_fadein > div > div > div.image_tile._fe_image_tab_grid > div:nth-child(1) > div > div > div > img')
    src = img.get_attribute('src')
        
    driver.quit()
    
    return src

def news_crawling(data):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) 
    
    driver = wb.Chrome()
    driver.get('https://www.naver.com')
    time.sleep(1.2)
    
    search = driver.find_element(By.ID, 'query')
    search.send_keys(data)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    
    driver.find_element(By.LINK_TEXT, '뉴스').click()
    time.sleep(2)
    
    driver.implicitly_wait(5)
    
    for i in range(3):
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(2)
        
    titles = driver.find_elements(By.CSS_SELECTOR, 
                                  
                                  'div > div > div > div > div > div > a:nth-child(1) > span.sds-comps-text')
    text_titles = [t.text for t in titles]

    driver.quit()    
    
    return text_titles