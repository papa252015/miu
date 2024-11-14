import time


from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




import re


#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_13/')




    # ниже пишем свой код

    driver.find_element(By.ID,'openNewPageBtn').click()
    time.sleep(1)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    time.sleep(1)

    all_windows = driver.window_handles


#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
