import time


from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By


import re

try:
#вы пишите свой код

    #инициализирую драйвер
    driver = webdriver.Chrome()


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotest_16/')




    # ниже пишем свой код
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price1'), '550')
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'buyButton1'))).click()
    

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
