import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

path = "D:\AIU\AIU_FInal\Senior\pytorch_pix2code\compiler\dataset\gui2\html"
photo_path = "D:/AIU/AIU_FInal/Senior/pytorch_pix2code/compiler/dataset/gui2/"
directory = os.fsencode(path)
test = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    test.append(filename)

for i in test:
    driver.get(photo_path+i)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1080,S('Height')) # May need manual adjustment                                                                                                                
    driver.find_element(By.TAG_NAME, 'body').screenshot(i.replace('.html', '.png'))

driver.quit()
