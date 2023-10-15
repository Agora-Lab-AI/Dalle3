# Import the necessary module
import logging
from dalle3 import Dalle3
from swarms.models import OpenAIChat

image_to_generate = "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery"

llm = OpenAIChat(openai_api_key="")

# Create a prompt for idea to image
def llm_prompt(image_to_generate: str):

    LLM_PROMPT = f"""
    Refine the USER prompt to create a more precise image tailored to the user's needs using
    an image generator like DALLE-3. 

    ###### FOLLOW THE GUIDE BELOW TO REFINE THE PROMPT ######

    - Use natural language prompts up to 400 characters to describe the image you want to generate. Be as specific or vague as needed.

    - Frame your photographic prompts like camera position, lighting, film type, year, usage context. This implicitly suggests image qualities.

    - For illustrations, you can borrow photographic terms like "close up" and prompt for media, style, artist, animation style, etc.  

    - Prompt hack: name a film/TV show genre + year to "steal the look" for costumes, lighting, etc without knowing technical details.

    - Try variations of a prompt, make edits, and do recursive uncropping to create interesting journeys and zoom-out effects.

    - Use an image editor like Photopea to uncrop DALL-E outputs and prompt again to extend the image.

    - Combine separate DALL-E outputs into panoramas and murals with careful positioning/editing.

    - Browse communities like Reddit r/dalle2 to get inspired and share your creations. See tools, free image resources, articles.

    - Focus prompts on size, structure, shape, mood, aesthetics to influence the overall vibe and composition.

    - Be more vague or detailed as needed - DALL-E has studied over 400M images and can riff creatively or replicate specific styles.

    ###### END OF GUIDE ######

    Prompt to refine: {image_to_generate}
    """
    return LLM_PROMPT

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle3 class with your cookie value
dalle = Dalle3("")

# Open the website with your query
dalle.open_website(llm_prompt(image_to_generate))

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download_images(urls, "images/")
