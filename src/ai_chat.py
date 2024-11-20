import openai

class AIChat:
    def __init__(self, api_key):
        openai.api_key = api_key

    def ask_ai(self, text):
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def should_respond(self, text):
        # 实现判断逻辑
        pass