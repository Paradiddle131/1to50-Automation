#from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
import time

url = "http://zzzscore.com/1to50/en/?ts=1586038059172"
chrome_driver = "#### DRIVER PATH ####"

def open_browser():
    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)
    time.sleep(0.8)

#   time.sleep(5)

    for i in range(2):
        list_box = driver.find_elements_by_class_name('grid')[0].find_elements_by_tag_name('div')
        list_values = []
        for box in list_box:
            print(box.text)
            list_values.append(int(box.text))
        print(list_values)
        sequence = sorted(range(len(list_values)), key=lambda k: list_values[k])
        print(sequence)
        for index in sequence:
            list_box[index].click()
            time.sleep(0.02)

    time.sleep(5)
print(open_browser())
