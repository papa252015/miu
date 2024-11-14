import time


from selenium import webdriver


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

try:

    driver = webdriver.Chrome()


    driver.get('https://erikdark.github.io/Qa_autotest_07/')

# ниже пишем свой код

    challage_text = driver.find_element(By.ID,'challenge').text
    print(challage_text)



    parts = challage_text.split()
    print(parts)
    a = int(parts[2])
    b = int(parts[4].replace('?'))
    corr_sum = a+b

    select = Select(driver.find_element(By.ID, 'answerSelect'))



    driver.find_element(By.ID,'answer').send_keys(corr_sum)



    driver.find_element(By.ID,'submitBtn').click()


# конец блока с моим кодом

#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
