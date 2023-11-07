import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from vision_ai import VisionAI
from dalle_ai import DalleAI

parser = argparse.ArgumentParser(
    description="Generate a DALL-E image from a recipe name determined by a vision model."
)
parser.add_argument("food_url", type=str, help="The URL of the food image to analyze.")

load_dotenv()


def main(food_url):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    vision_ai = VisionAI(client)
    dalle_ai = DalleAI(client)

    try:
        recipe_name = vision_ai.get_recipe_name_from_image(food_url)

        prompt = f"Food {recipe_name} as dinner in a nice candlelight atmosphere"

        image_url = dalle_ai.create_image_from_text(prompt)

        print(image_url)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.food_url)
