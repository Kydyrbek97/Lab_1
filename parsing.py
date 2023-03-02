from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import os
import csv
import requests
import lxml

url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
os.environ['PATH'] += "/home/user/Desktop/Lab/chromedriver"
browser = webdriver.Chrome()
browser.get(url)


def write_to_csv(data):
    with open('Lab.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data['price'],
                         data['data_post'],
                         data['image']))


def prepare_csv():
    with open('Lab.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('price', 'data_post', 'image'))


sleep(25)
for p in range(1, 101):
    soup = BeautifulSoup(browser.page_source, 'lxml')
    info = soup.find_all('div', class_='clearfix')
    for inf in info:
        try:
            price = inf.find('div', class_='price') \
                .text.strip() \
                .replace('Please Contact', 'Нет цена') \
                .replace('\n', '') \
                .replace('                                                                            '
                         '', '-')
        except:
            price = "Нет цена!"
        try:
            data_post = inf.find('span', class_='date-posted').text.replace('<', '')
        except:
            data_post = "Нет дата!"
        try:
            image = inf.find('div', class_='image').find('img').get('src')
        except:
            image = "Нет фото!"
        data = {'price': price, 'data_post': data_post, 'image': image}
        write_to_csv(data)
    next_button_link = browser.find_element(By.CSS_SELECTOR, "a[title=Next]")
    next_button_link.click()
    sleep(20)
