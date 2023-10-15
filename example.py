# Import the necessary module
import logging
from dalle3 import Dalle3

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle3 class with your cookie value
dalle = Dalle3("")

# Open the website with your query
dalle.open_website("a cat with a hat")

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download_images(urls, "images/")