import requests
from json import dumps, load

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time


chrome_options = Options()
chrome_options.add_argument("--headless")


def get_lowerst():
    endpoint = 'https://gql-rmrk2-prod.graphcdn.app/'
    with open('kanaria_lowest_2.json', 'r') as file:
        data_to_post = load(file)
    json_param = dumps(data_to_post)

    data = requests.post(endpoint, data=json_param)
    id = data.json()['data']['nfts'][0]['id']

    url = 'https://kanaria.rmrk.app/catalogue/' + id

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    price = driver.find_element(By.TAG_NAME, 'strong').text
    driver.quit()
    return price, url

def start_notify():
    endpoint = 'https://gql-rmrk2-prod.graphcdn.app/'
    with open('kanaria_lowest_2.json', 'r') as file:
        data_to_post = load(file)
    json_param = dumps(data_to_post)

    data = requests.post(endpoint, data=json_param)
    id = data.json()['data']['nfts'][0]['id']

    url = 'https://kanaria.rmrk.app/catalogue/' + id

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    price = driver.find_element(By.TAG_NAME, 'strong').text.split()[0]
    old_price = price
    while (float(old_price) - float(price))/ float(old_price) <= 0.1:
        old_price = price
        endpoint = 'https://gql-rmrk2-prod.graphcdn.app/'
        with open('kanaria_lowest_2.json', 'r') as file:
            data_to_post = load(file)
        json_param = dumps(data_to_post)

        data = requests.post(endpoint, data=json_param)
        id = data.json()['data']['nfts'][0]['id']

        url = 'https://kanaria.rmrk.app/catalogue/' + id

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(3)
        price = driver.find_element(By.TAG_NAME, 'strong').text.split()[0]
        print(price, url, 'not yet')
    else:
        driver.get()
        return price, url




# print(get_lowerst())
# print(start_notify())

