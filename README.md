[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# DALLE3 API

Dive into the world of AI-generated images with DALLE3 API! This radically simple Python package allows you to interact with the DALL-E 3 Unofficial API, enabling you to generate and download images based on your creative prompts! 

And, we've also implemented a simple verison of [Idea2Image](https://huggingface.co/papers/2310.08541) that uses an LLM for prompt enrichement! By passing in the desired prompt into a meta prompting agent we're able to guide DALLE3 much better and reliably!

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
pip3 install --upgrade dalle3
```


## Usage 🐡
--------

Here's a simple example of how to use DALLE3 API:

```python
# Import the necessary module
import os
import logging
from dalle3 import Dalle

# Define cookie using env or empty string
cookie = os.getenv("BING_COOKIE") or ""

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle class with your cookie value
dalle = Dalle(cookie)

# Open the website with your query
dalle.create(
    "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery"
)

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download(urls, "images/")
```
-----

## Idea to Image prototype
- A prototype where we use GPT4 to refine a prompt -> then create an image.

`python idea_to_image.py`

### Arguments

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
6.  Paste in the cookie parameter.

Now you can use this cookie value to instantiate the `Dalle` class.

## Edge Cases 🦀
-------------

-   If the `save_folder` path you provide when calling `download` does not exist, the function will attempt to create it. Make sure you have the necessary permissions to create directories in the specified location.
-   If the user is not signed in on the browser that Selenium WebDriver is controlling, the script will not be able to retrieve the cookie. Make sure you're signed in to your Bing Image Creator account in the same browser session.
- If you see: `selenium.common.exceptions.WebDriverException: Message: unknown error: cannot connect to chrome at 127.0.0.1:58296
from session not created: This version of ChromeDriver only supports Chrome version 118 Current browser version is 117.0.5938.15` 
then you need to update [your chrome by going here:](chrome://settings/help)
t add 
chrome://settings/help


## License 📜
----------

DALLE3 API is licensed under the MIT License. See the [LICENSE](https://domain.apac.ai/LICENSE) file for more details.

# Todo
- [ ] Add Automatic cookie finding seamlessly
- [ ] Automatically upgrade chrome to 118
- [ ] Add automatic browser detection, cross browser
- [ ] Lower amount of endpoints to run by 90% => `dalle = Dalle() dalle.run("image")`
- [ ] Add gpt4 vision api using same approach, scrape and enter but need to find the right cookie
- [ ] Establish Idea2Image Documentation
- [ ] Create tests for Idea2Image
- [ ] Add human feedback for idea2image, prompt -> llm -> dalle -> human feedback -> back to llm -> dalle
- [ ] Different output types, svg, jpg