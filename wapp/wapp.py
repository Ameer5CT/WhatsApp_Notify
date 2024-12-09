import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def send_msg(receiver, msg):
    try:
        is_logged_in = False
        current_dir = os.path.dirname(os.path.abspath(__file__))
        profile_dir = os.path.join(current_dir, "wapp_profile")

        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={profile_dir}")
        chromedriver_path = "/usr/bin/chromedriver"

        # Smaller screen if no need to login
        if os.path.isdir(profile_dir):
            is_logged_in = True
            chrome_options.add_argument("--window-size=1,1")

        # # This driver for windows
        # driver = webdriver.Chrome()

        # This driver for rpi
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chromedriver_path), options=chrome_options)

        driver.get("https://web.whatsapp.com")

        # minimize if no need to login
        if is_logged_in:
            driver.set_window_size(1, 1)
            driver.set_window_position(-2000, 0)
            driver.minimize_window()
        
        time.sleep(60)

        # Search for the receiver
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(receiver + Keys.ENTER)
        time.sleep(15)

        # Send the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

        # Simulate Shift + Enter for newlines
        for char in msg:
            if char == '\n':
                message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            else:
                message_box.send_keys(char)

        # Send the message with Enter key
        message_box.send_keys(Keys.ENTER)

        time.sleep(30)
        driver.quit()

        return True
    except:
        return False
