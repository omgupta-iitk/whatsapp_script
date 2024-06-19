import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://web.whatsapp.com/")
driver.maximize_window()
while(1):
    n  = int(input("how many times? :"))
    user = input("name of the person to send")
    msg = input("what is the message")
    s = input("scan the code tell me when everything is ready ?")

    driver.find_element("xpath",f"//span[contains(@title, '{user}')]").click()
    time.sleep(2)
    for i in range(n):
        driver.find_element("xpath","//div[contains(@class, 'x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf')]").send_keys(msg)
        driver.find_element("xpath","//div[contains(@class, 'x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf')]").send_keys(Keys.RETURN)
        time.sleep(0.001)







