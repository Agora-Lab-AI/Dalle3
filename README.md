[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# DALLE3 API
A radically simple and easy to use DALLE3 API

## DALLE-3 API
`pip install dalle3`


# Usage
```python
# Import the necessary modules
import logging
from dalle3.main import Dalle3

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

```


# License
MIT



