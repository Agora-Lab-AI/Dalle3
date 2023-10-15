import argparse
import logging
from dalle3 import Dalle
from swarms.models import OpenAIChat


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


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate images from text prompts using DALLE-3."
    )
    parser.add_argument(
        "--image_to_generate",
        type=str,
        required=True,
        help="Text prompt for the image to generate.",
        default="Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery",
    )
    parser.add_argument(
        "--openai_api_key",
        type=str,
        required=True,
        help="OpenAI API key.",
    )
    parser.add_argument(
        "--cookie",
        type=str,
        required=True,
        help="Cookie value for DALLE-3.",
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="images/",
        help="Folder to save the generated images.",
    )

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Instantiate the OpenAIChat and Dalle classes with your API key and cookie value
    llm = OpenAIChat(openai_api_key=args.openai_api_key)
    dalle = Dalle(args.cookie)

    # Refine the prompt using the llm
    image_to_generate = llm_prompt(args.image_to_generate)
    refined_prompt = llm(image_to_generate)
    print(f"Refined prompt: {refined_prompt}")

    # Open the website with your query
    dalle.create(refined_prompt)

    # Get the image URLs
    urls = dalle.get_urls()

    # Download the images to your specified folder
    dalle.download(urls, args.output_folder)


if __name__ == "__main__":
    main()
