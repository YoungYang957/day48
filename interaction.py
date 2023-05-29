from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_drive_path = "/Users/jinyuanyang/development/chromedriver_mac64/chromedriver"

s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)

driver.get("https://secure-retreat-92358.herokuapp.com/")






# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# article_count.click()
#
# search = driver.find_element(By.NAME, "Search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
