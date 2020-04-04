from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
import time

url = "http://zzzscore.com/1to50/en/?ts=1586038059172"
#
# html_content = requests.get(url).text
# soup = BeautifulSoup(html_content, "lxml")
# tag_description = soup.find('div', class_="description")
# tag_grid = soup.find('div', class_="grid x5")
# print(tag_description)
# print(tag_description.attrs)



def open_browser():
    driver = webdriver.Chrome("D:\chromedriver.exe")
    driver.get(url)
    time.sleep(0.8)
    driver.find_element_by_class_name("resetBtn").click()
    x = driver.find_elements_by_class_name('box')
    print(x)
    print(x[0])
    print(x[0].text)
    y = driver.find_elements_by_class_name('proposeFbLike')
    print(y)
    print(y[0])
    print(y[0].text)
    # text = wait(driver, 10).until(lambda driver: not text_field.text == 'Gerando...' and text_field.text)
    # return text
    time.sleep(3)


print(open_browser())













# import scrapy
#
#
# class BlogSpider(scrapy.Spider):
#     name = '1to50'
#     start_urls = ['http://zzzscore.com/1to50/en/?ts=1586038059172']
#
#     def parse(self, response):
#         for title in response.css('.post-header>h2'):
#             yield {'title': title.css('a ::text').get()}
#
#         for next_page in response.css('a.next-posts-link'):
#             yield response.follow(next_page, self.parse)
