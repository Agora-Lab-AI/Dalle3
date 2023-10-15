# Import the necessary module
import os
import logging
from dalle3 import Dalle

# Define cookie using env or empty string
cookie = os.getenv("BING_COOKIE") or "1Dv1qGH6TcGzEQUJqU6AfxnMfxPR4V9yCtKk8ox2kpl-_YwmKzM9CnzPmlge158c0DTSDAEqrDV5itj3Ll0GyuaRrWmXf0Gk_2FIZuL2NvCLUrCF3VALngS9qw9vESZ9EY9vqVVVvjGoIJpxf9HEz6OV3fih4dw_Abc7GrfRC7p8iRDiCmotsgy9lPKf6sSPg9yy2lMTSU9-MNmkga0CACSZsV4La9NU5V5nNowUAMhU"

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle class with your cookie value
dalle = Dalle(cookie)

# Open the website with your query
dalle.open_website(
    "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery"
)

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download_images(urls, "images/")
