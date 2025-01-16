from openai import OpenAI


class imageGenerator:
    def __init__(self):
        return

    def promptBuilder(self, happiness, abstractness, color_contrast, positivity, top_songs):
        prompt = "Create a playlist icon that looks like: " + top_songs[0] + ', ' + top_songs[1] + ', ' + top_songs[
            2] + '. The image should be inspired by ' + happiness + ', ' + color_contrast + ", and can be described as " + abstractness + "Do not generate text within the image.”"
        return prompt

    def generation(self, prompt):
        client = OpenAI()
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,

            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        return image_url
