import datetime
import logging
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions


class Dalle:
    """
    A class used to interact with the DALL-E 3 Unofficial API

    ...

    Attributes
    ----------
    options : ChromeOptions
        a ChromeOptions object to configure the Chrome driver
    driver : Chrome
        a Chrome driver object to interact with the website
    cookie_value : str
        a string representing the cookie value to bypass automation detection

    Methods
    -------
    get_time():
        Returns the current time in the format "[%d/%m/%Y %H:%M:%S]"
    get_time_save():
        Returns the current time in the format "%d-%m-%Y %H-%M-%S"
    download_images(urls: list, save_folder: str):
        Downloads images from the provided URLs and saves them in the specified folder
    open_website(query: str):
        Opens the Bing Image Creator (DALL-E 3) and adds a cookie
    get_urls():
        Extracts and returns image URLs from the website


    Usage:
    ------
    # Import the necessary module
    import logging
    from dalle3 import Dalle

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Instantiate the Dalle class with your cookie value
    dalle = Dalle("")

    # Open the website with your query
    dalle.open_website(
        "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery"
    )

    # Get the image URLs
    urls = dalle.get_urls()

    # Download the images to your specified folder
    dalle.download_images(urls, "images/")
    """

    def __init__(self, cookie_value: str):
        self.options = ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless")
        self.driver = Chrome(options=self.options)
        self.cookie_value = cookie_value

    @staticmethod
    def get_time():
        """Returns the current time in the format "[%d/%m/%Y %H:%M:%S]"""
        return datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")

    @staticmethod
    def get_time_save():
        """Returns the current time in the format "%d-%m-%Y %H-%M-%S" """
        return datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    def download_images(self, urls: list, save_folder: str):
        """Downloads images from the provided URLs and saves them in the specified folder"""
        save_folder = (save_folder)[:225]
        try:
            timestamp_folder = os.path.join(save_folder, self.get_time_save())
            if not os.path.exists(timestamp_folder):
                os.makedirs(timestamp_folder)

            for index, url in enumerate(urls):
                response = requests.get(url)
                response.raise_for_status()
                filename = os.path.join(timestamp_folder, f"image_{index + 1}.png")
                with open(filename, "wb") as file:
                    file.write(response.content)

                logging.info(
                    f'{self.get_time()} Image downloaded successfully and saved to "{filename}"'
                )

        except requests.exceptions.RequestException as e:
            logging.critical(f"Image download failed: {str(e)}")

    def open_website(self, query: str):
        """Opens the Bing Image Creator (DALL-E 3) and adds a cookie"""
        cookie = {"name": "_U", "value": self.cookie_value}

        self.driver.get(f"https://www.bing.com/images/create?q={query}")
        logging.info(f"{self.get_time()} Bing Image Creator (Dalle-3) Opened")

        self.driver.add_cookie(cookie)
        self.driver.refresh()
        logging.info(f"{self.get_time()} Cookie values added ")

        return True

    def get_urls(self):
        """Extracts and returns image URLs from the website"""
        try:
            urls = list(
                set(
                    [
                        element.get_attribute("src")
                        for element in WebDriverWait(self.driver, 600).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg"))
                        )
                    ]
                )
            )

            urls = [url.split("?")[0] for url in urls]

            return urls
        except Exception as e:
            logging.critical(
                f"Error while extracting image urls. Maybe something is wrong about your prompt. (You can check you prompt manually) \n{e}"
            )
