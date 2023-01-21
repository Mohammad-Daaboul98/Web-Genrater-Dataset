import os
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

path = "C:\\Users\\basel\\Desktop\\Senior Project\\master\\dataset\\landing-samples"
photo_path = "C:/Users/basel/Desktop/Senior Project/master/dataset/landing-samples/"
directory = os.fsencode(path)
test = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.html'):
        test.append(filename)

for i in test:
    driver.get(photo_path+i)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1440, S('Height'))                                                                                                              
    driver.find_element(By.TAG_NAME, 'body').screenshot(i.replace('.html', '.png'))

driver.quit()
