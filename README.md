[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# DALLE3 API

Dive into the world of AI-generated images with DALLE3 API! This Python package allows you to interact with the DALL-E 3 Unofficial API, enabling you to generate and download images based on your creative prompts.

## Features 🌊
-----------

-   Easy to Use: With just a few lines of code, you can start generating images.
-   Customizable: You can provide your own creative prompts to generate unique images.
-   Automated Download: The API automatically downloads the generated images to your specified folder.
-   Real-Time Updates: The API provides real-time logging information about the image generation and download process.

## Installation 🐠
---------------

You can install DALLE3 API using pip:

```
pip install dalle3
```


## Usage 🐡
--------

Here's a simple example of how to use DALLE3 API:

```python
# Import the necessary modules
import logging
from dalle3 import Dalle3

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle3 class with your cookie value
dalle = Dalle3("<your_cookie>")

# Open the website with your query
dalle.open_website("Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish")

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download_images(urls, "images/")
```


## Idea to Image prototype
- A prototype where we use GPT4 to refine a prompt -> then create an image.

`python idea_to_image.py`

The script takes the following arguments:

-   `--image_to_generate`: This is a required argument. It is the text prompt for the image you want to generate.

-   `--openai_api_key`: This is a required argument. It is your OpenAI API key.

-   `--cookie`: This is a required argument. It is your cookie value for DALLE-3.

-   `--output_folder`: This is an optional argument. It is the folder where you want to save the generated images. If not provided, it defaults to `"images/"`.

### Examples
--------

Here are some examples of how to use the script from the command line:

#### Example 1

Generate an image with the prompt "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery", using your OpenAI API key and cookie value, and save the images in the default folder (`"images/"`):

```bash
python idea_to_image.py --image_to_generate "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery" --openai_api_key "your_openai_api_key" --cookie "your_cookie_value"
```

#### Example 2

Generate an image with the prompt "A futuristic city skyline at sunset", using your OpenAI API key and cookie value, and save the images in a folder named `"futuristic_city_images/"`:

```bash
python idea_to_image.py --image_to_generate "A futuristic city skyline at sunset" --openai_api_key "your_openai_api_key" --cookie "your_cookie_value" --output_folder "futuristic_city_images/"
```

Remember to replace `"your_openai_api_key"` and `"your_cookie_value"` with your actual OpenAI API key and cookie value.

------

## Obtaining Your Cookie 🍪
------------------------

To use DALLE3 API, you need to obtain your cookie from Bing Image Creator. Here's how you can do it:

1.  Go to [Bing Image Creator](https://www.bing.com/images/create) in your browser and log in to your account.
2.  Press `Ctrl+Shift+J` (or `Cmd+Option+J` on Mac) to open developer tools.
3.  Navigate to the `Application` section.
4.  Click on the `Cookies` section.
5.  Find the variable `_U` and copy its value.

Now you can use this cookie value to instantiate the `Dalle3` class.

## Edge Cases 🦀
-------------

-   If the `save_folder` path you provide when calling `download_images` does not exist, the function will attempt to create it. Make sure you have the necessary permissions to create directories in the specified location.
-   If the user is not signed in on the browser that Selenium WebDriver is controlling, the script will not be able to retrieve the cookie. Make sure you're signed in to your Bing Image Creator account in the same browser session.

## License 📜
----------

DALLE3 API is licensed under the MIT License. See the [LICENSE](https://domain.apac.ai/LICENSE) file for more details.

