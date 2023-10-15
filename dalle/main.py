import datetime
import logging
import os
import time

import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome, ChromeOptions


def get_cookie_value():
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    driver = Chrome(options=options)

    # Go to Bing Image Creator and log in manually here.
    # Once logged in, the script will proceed to get the cookie.
    driver.get("https://www.bing.com/images/create")

    input("Press Enter after you've logged in...")

    # Open developer tools
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(
        "j"
    ).key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()
    time.sleep(2)  # Allow devtools to open

    # Execute JavaScript code to return the value of '_U' cookie
    cookie_value = driver.execute_script(
        'return document.cookie.split("; ").find(row => row.startsWith("_U=")).split("=")[1]'
    )
    driver.quit()

    return cookie_value


# Function to get the current time in a specific format
def get_time():
    return datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")


# Function to get the current time in a format suitable for file and folder names
def get_time_save():
    return datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")


# Function to download images from given URLs
def download_images(urls, save_folder):
    save_folder = (save_folder)[:225]
    try:
        timestamp_folder = os.path.join(save_folder, get_time_save())
        if not os.path.exists(timestamp_folder):
            os.makedirs(timestamp_folder)

        for index, url in enumerate(urls):
            response = requests.get(url)
            response.raise_for_status()
            filename = os.path.join(
                timestamp_folder, f"{save_folder} ({index + 1}).png"
            )
            with open(filename, "wb") as file:
                file.write(response.content)

            logging.info(
                f'{get_time()} Image downloaded successfully and saved to "{filename}"'
            )

    except requests.exceptions.RequestException as e:
        logging.critical(f"Image download failed: {str(e)}")


# Function to open the Bing website and set cookies
def open_website(query, cookie_value):
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    driver = Chrome(options=options)

    cookie = {"name": "_U", "value": cookie_value}
    driver.get(f"https://www.bing.com/images/create?q={query}")
    logging.info(f"{get_time()} Bing Image Creator (Dalle-3) Opened")

    driver.add_cookie(cookie)
    driver.refresh()
    logging.info(f"{get_time()} Cookie values added ")
    return driver


# Function to get image URLs
def get_urls(driver):
    try:
        urls = list(
            set(
                [
                    element.get_attribute("src")
                    for element in WebDriverWait(driver, 600).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg"))
                    )
                ]
            )
        )

        urls = [url.split("?")[0] for url in urls]
        return urls
    except Exception as e:
        logging.critical(
            f"Error while extracting image urls. Maybe something is wrong about your prompt. (You can check your prompt manually) \n{e}"
        )


# Main part of the script
if __name__ == "__main__":
    query = "Military Byzantine Orthodox army legions world domination, holy orthodox christian warriors, concept"
    save_folder = "images/"
    cookie_value = get_cookie_value()
    driver = open_website(query, cookie_value)
    urls = get_urls(driver)
    download_images(urls, save_folder)
