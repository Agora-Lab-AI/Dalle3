# Import the necessary module
import logging
from dalle3 import Dalle3
from swarms.models import OpenAIChat

image_to_generate = "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery"

llm = OpenAIChat(openai_api_key="")

# Create a prompt for idea to image
def llm_prompt(image: str):

    LLM_PROMPT = f"""
    Refine the USER prompt to create a more precise image tailored to the user's needs using
    an image generator like DALLE-3. 

    ###### FOLLOW THE GUIDE BELOW TO REFINE THE PROMPT ######
    A prompt is a
    sentence, 400
    characters or
    less, that
    describes the
    image you
    want.
    Here are some
    random
    examples.
    Prompt: grainy abstract experimental expired film photo of a
    woman in red dress, talking angrily on mobile phone,
    gesticulating angrily, in 1960s New York City by Saul Leiter,
    50mm lens, cinematic colors, oversaturated filter, blur,
    reflection, refraction, distortion, rain drops, smears, smudges,
    blur, cinestill 800t Prompt: 🌈🚀🤩, octane 3D render
    Prompts can be very
    long – or very short!
    DALL·E has not explicitly been 'taught' anything, like
    who Frida Kahlo is, or what a llama looks like, or what
    a wide-angle lens does.
    It has just studied 650 million images & captions, and
    left to draw its own conclusions.
    That's why there can't be a regular'manual'
    , based on
    functionality that the developers intentionally
    programmed in – even the creators of DALL·E cannot
    be sure what DALL·E has or hasn't 'learned'
    , or what it
    thinks different phrases mean.
    Instead, we have to 'discover' what DALL·E is capable
    of, and how itreacts. This document is a start!
    Prompt
    design
    Sometimes, less is more. Prompts can't be more than 400
    characters, in any case. And you can get amazing results from
    just a few emojis! But if you have a specific outcome in mind,
    then being specific in your prompt will help.
    A simple adjective, like 'action photography'
    , already embodies
    a lot of characteristics (about shutter speed, framing, lens
    choices, etc) that you might otherwise define separately.
    There are 'fingers-crossed' prompt phrases, like AI-era prayers,
    hoped to mean 'make it really good!'
    , such as 4k, 8k, highquality, trending, award-winning, acclaimed, on artstation, etc.
    However, the precise impact of these has not been rigorously
    tested. But feel free to add them!
    In text AI models, simple prompt tweaks have created huge
    boosts in performance: for instance, when a text generator is
    made to answer a math puzzle, starting with the words 'Let's
    think things through step-by-step' makes it 4x more likely to get
    the right answer.
    So no doubt, there are similar DALL·E hacks yet to be found…
    Digital art of portrait of a woman, holding pencil, inspired, head-and-shoulders shot, white background, cute Pixar
    character
    You can borrow some photographic prompt terminology
    (especially for framing) to apply to illustrations: e.g: 'close-up.'
    If you are generating mockups of 3D art, you can also define
    how that piece is photographed!
    Adjectives can easily influence multiple factors, e.g: 'art deco'
    will influence the illustration style, but also the clothing and
    materials of the subject, unless otherwise defined. Years,
    decades and eras, like '1924' or 'late-90s'
    , can also have this
    effect.
    Even superficially specific prompts have more 'general' effects.
    For instance, defining a camera or lens ('Sigma 75mm') doesn't
    just 'create that specific look'
    , it more broadly alludes to 'the kind
    of photo where the lens/camera appears in the description'
    ,
    which tend to be professional and hence higher-quality.
    If a style is proving elusive, try 'doubling down' with related
    terms (artists, years, media, movement) years, e.g: rather than
    simply '…by Picasso'
    , try '…Cubist painting by Pablo Picasso,
    1934, colourful, geometric work of Cubism, in the style of "Two
    Girls Reading." Or try unbundling!)

    ###### END OF GUIDE ######

    Prompt to refine: {image}
    """
    return image

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
