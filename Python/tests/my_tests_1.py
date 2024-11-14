
import time


from selenium import webdriver


from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get('https://erikdark.github.io/Qa_autotest_01/')
time.sleep(10)


# driver.find_element(By.CSS_SELECTOR,'.level-1 button').click()

# driver.find_element(By.CSS_SELECTOR,'.level-2 button').click()

driver.find_element(By.ID,'inputField').send_keys('Полный пиздец')
buttons = driver.find_elements(By.CLASS_NAME, 'btn')

target_text = 'Button 3'

for button in buttons:
    if button.text==target_text:
        button.click()


time.sleep(10)
driver.quit()


