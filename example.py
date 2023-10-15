# Import the necessary module
import os
import logging
from dalle3 import Dalle

# Define cookie using env or empty string
cookie = os.getenv("BING_COOKIE")
#or
# cookie = "cookie"

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
