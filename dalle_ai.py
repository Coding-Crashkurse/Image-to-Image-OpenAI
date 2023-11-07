class DalleAI:
    def __init__(self, client):
        self.client = client

    def create_image_from_text(self, text_prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=text_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Error handling
        if response.data and response.data[0].url:
            return response.data[0].url
        else:
            raise ValueError("The AI did not return a valid image.")
