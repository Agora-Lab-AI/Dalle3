import logging
from dalle3 import Dalle

# Define cookie using env or empty string
cookie = ""

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle class with your cookie value
dalle = Dalle(cookie)

# Open the website with your query
dalle.create(
    "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish"
)

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download(urls, "images/")
