class VisionAI:
    def __init__(self, client):
        self.client = client

    def get_recipe_name_from_image(self, image_url):
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Identify the ingredients in this image and suggest a recipe that could be prepared using these items. Provide ONLY the name of the recipe.",
                        },
                        {"type": "image_url", "image_url": image_url},
                    ],
                }
            ],
            max_tokens=300,
        )

        # Error handling
        if (
            response.choices
            and response.choices[0].message
            and response.choices[0].message.content
        ):
            return response.choices[0].message.content
        else:
            raise ValueError("The AI did not return a valid recipe name.")
