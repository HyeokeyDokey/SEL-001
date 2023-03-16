from selenium import webdriver

# Chrome 드라이버 실행
driver = webdriver.Chrome()

# 네이버 메인 페이지 열기
driver.get("https://www.naver.com")

# 검색어 입력
search_box = driver.find_element_by_name("query")
search_box.send_keys("Python")

# 검색 버튼 클릭
search_button = driver.find_element_by_class_name("ico_search_submit")
search_button.click()

# 검색 결과 출력
search_results = driver.find_elements_by_class_name("sh_blog_title")
for result in search_results:
    print(result.text)

# 브라우저 닫기
driver.quit()
