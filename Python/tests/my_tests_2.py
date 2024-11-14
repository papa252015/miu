import time


from selenium import webdriver


from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get('https://erikdark.github.io/Qa_autotests_05/')
time.sleep(10)


text=driver.find_element(By.CLASS_NAME, 'big-number').text





