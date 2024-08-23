from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import random

with open("messages.txt", "r", encoding="utf-8") as messages:
    messagelist = [line.strip() for line in messages if line.strip()]

def start():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    input("If you scanned the QR code, press a key and enter.")

    try:
        message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    except Exception as e:
        print(f"Error finding message area: {e}")
        driver.quit()
        return

    while True:
        wp_source = driver.page_source
        soup = bs(wp_source, "lxml")

        try:
            status_element = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')

            çevrimiçi = status_element.text.strip()
            print(f"Çevrimdışı kontrol: {çevrimiçi}")

            if çevrimiçi in ["çevrimiçi", "online"] and not flag:
                print("Online detected")
                msgToSend = messagelist[random.randint(0, len(messagelist) - 1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif çevrimiçi not in ["çevrimiçi", "online"]:
                print("currently offline")
                flag = False
        except Exception as e:
            print(f"Error checking online status: {e}")
            print("currently offline")
            flag = False

        time.sleep(5)

start()
