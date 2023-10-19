[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# DALLE3 API

A radically simple Dalle3 API.

<!-- And, we've also implemented a simple verison of [Idea2Image](https://huggingface.co/papers/2310.08541) that uses an LLM for prompt enrichement! By passing in the desired prompt into a meta prompting agent we're able to guide DALLE3 much better and reliably! -->


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

```
-----

<!-- ## Idea to Image prototype
- A prototype where we use GPT4 to refine a prompt -> then create an image.

```python
from dalle3 import Idea2Image

idea2image = Idea2Image(
    image="Hashashin Assassin's creed ancient persia art",
    #enter in cookie
    cookie="",
    #enter in api key
    openai_api_key=""
)

idea2image.run()


```
------ -->


# `Dalle` Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Dalle Class](#dalle-class)
   - [Initialization Parameters](#initialization-parameters)
3. [Methods and Usage](#methods-and-usage)
   - [get_time Method](#get-time-method)
   - [get_time_save Method](#get-time-save-method)
   - [download Method](#download-method)
   - [create Method](#create-method)
   - [get_urls Method](#get-urls-method)
   - [run Method](#run-method)
4. [Examples](#examples)
   - [Example 1: Creating a Dalle Instance](#example-1-creating-a-dalle-instance)
   - [Example 2: Running the Whole Process](#example-2-running-the-whole-process)
5. [Additional Information](#additional-information)
6. [References and Resources](#references-and-resources)

---

## 1. Introduction <a name="introduction"></a>

Welcome to the documentation on the `Dalle` class. This comprehensive guide provides in-depth information about the Dalle library and its core components. Before we dive into the details, it's crucial to understand the purpose and significance of this library.

### 1.1 Purpose

This library houses the DALL-E 3 Unofficial API, providing tools to download images based on queries. The `Dalle` class facilitates this process, allowing users to interact with the API efficiently.

### 1.2 Key Features

- **DALL-E 3 API Interaction:** The `Dalle` class provides an interface to interact with the DALL-E 3 Unofficial API.

- **Image Download:** Dalle3 allows you to download images from the web based on your queries.

---

## 2. Dalle Class <a name="dalle-class"></a>

The `Dalle` class is a fundamental module in the Dalle3 library, enabling interactions with the DALL-E 3 Unofficial API.

### 2.1 Initialization Parameters <a name="initialization-parameters"></a>

Here are the initialization parameters for the `Dalle` class:

- `cookie_value` (str): A string representing the cookie value to bypass automation detection.

### 2.2 Methods <a name="methods-and-usage"></a>

The `Dalle` class provides the following methods:

- `get_time()`: Returns the current time in the format "[%d/%m/%Y %H:%M:%S]".

- `get_time_save()`: Returns the current time in the format "%d-%m-%Y %H-%M-%S".

- `download(urls: list, save_folder: str)`: Downloads images from the provided URLs and saves them in the specified folder.

- `create(query: str)`: Opens the Bing Image Creator (DALL-E 3) and adds a cookie to interact with the API.

- `get_urls()`: Extracts and returns image URLs from the website.

- `run(query: str)`: Runs the whole process of downloading images from the provided query.

---

## 3. Methods and Usage <a name="methods-and-usage"></a>

Let's explore the methods provided by the `Dalle` class and how to use them effectively.

### 3.1 `get_time` Method <a name="get-time-method"></a>

The `get_time` method returns the current time in the format "[%d/%m/%Y %H:%M:%S]". It's a utility function to help with logging and timestamping.

### 3.2 `get_time_save` Method <a name="get-time-save-method"></a>

The `get_time_save` method returns the current time in the format "%d-%m-%Y %H-%M-%S". It's useful for creating timestamped folders for image downloads.

### 3.3 `download` Method <a name="download-method"></a>

The `download` method takes a list of image URLs and a save folder path. It downloads images from the provided URLs and saves them in the specified folder. This method is crucial for downloading images based on your queries.

### 3.4 `create` Method <a name="create-method"></a>

The `create` method opens the Bing Image Creator (DALL-E 3) website and adds a cookie to bypass automation detection. It prepares the environment for querying and downloading images.

### 3.5 `get_urls` Method <a name="get-urls-method"></a>

The `get_urls` method extracts and returns image URLs from the website. It allows you to retrieve the image URLs that match your query.

### 3.6 `run` Method <a name="run-method"></a>

The `run` method combines the previous methods to execute the whole process of downloading images based on the provided query. It's a convenient way to automate the image download process.

---

## 4. Examples <a name="examples"></a>

Let's dive into practical examples to demonstrate the usage of the `Dalle` class.

### 4.1 Example 1: Creating a Dalle Instance <a name="example-1-creating-a-dalle-instance"></a>

In this example, we create an instance of the `Dalle` class with your provided cookie value:

```python
# Instantiate the Dalle class with your cookie value
dalle = Dalle("your_cookie_value_here")
```

### 4.2 Example 2: Running the Whole Process <a name="example-2-running-the-whole-process"></a>

Here, we demonstrate how to use the `Dalle` class to run the whole process of downloading images based on a query:

```python
# Run the whole process of downloading images from the provided query
dalle.run("Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery")
```

---

## 5. Additional Information <a name="additional-information"></a>

Here are some additional tips and information for using the Dalle3 library and the `Dalle` class effectively:

- The `download` method allows you to specify the folder where downloaded images will be saved. Ensure that you have the necessary permissions to write to that folder.

- If you encounter issues with image downloads, check the prompt you provided. The quality and specificity of your query can affect the results.

---

## 6. References and Resources <a name="

references-and-resources"></a>

For further information and resources related to the Dalle3 library and DALL-E:

- [DALL-E 3 Unofficial API Documentation](https://www.bing.com/images/create): The official documentation for the DALL-E 3 Unofficial API, where you can explore additional features and capabilities.

This concludes the documentation for the Dalle3 library and the `Dalle` class. You now have a comprehensive guide on how to interact with the DALL-E 3 Unofficial API and download images based on your queries using Dalle3.

## 7. Obtaining Your Cookie 🍪
------------------------

To use DALLE3 API, you need to obtain your cookie from Bing Image Creator. Here's how you can do it:

1.  Go to [Bing Image Creator](https://www.bing.com/images/create) in your browser and log in to your account.
2.  Press `Ctrl+Shift+J` (or `Cmd+Option+J` on Mac) to open developer tools.
3.  Navigate to the `Application` section.
4.  Click on the `Cookies` section.
5.  Find the variable `_U` and copy its value.
6.  Paste in the cookie parameter.

Now you can use this cookie value to instantiate the `Dalle` class.

## 8. Edge Cases 🦀
-------------

-   If the `save_folder` path you provide when calling `download` does not exist, the function will attempt to create it. Make sure you have the necessary permissions to create directories in the specified location.
-   If the user is not signed in on the browser that Selenium WebDriver is controlling, the script will not be able to retrieve the cookie. Make sure you're signed in to your Bing Image Creator account in the same browser session.
- If you see: `selenium.common.exceptions.WebDriverException: Message: unknown error: cannot connect to chrome at 127.0.0.1:58296
from session not created: This version of ChromeDriver only supports Chrome version 118 Current browser version is 117.0.5938.15` 
then you need to update [your chrome by going here:](chrome://settings/help)
t add 
chrome://settings/help

-----

## Features 🌊
-----------

-   Easy to Use: With just a few lines of code, you can start generating images.
-   Customizable: You can provide your own creative prompts to generate unique images.
-   Automated Download: The API automatically downloads the generated images to your specified folder.
-   Real-Time Updates: The API provides real-time logging information about the image generation and download process.


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
- [ ] Add bingchat api
- [ ] Add chatgpt dalle api
- [ ] Create Chatgpt V api
