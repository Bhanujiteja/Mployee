import openai
import os

class OpenAIModel:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def extract_experience(text: str) -> str:
        try:
            prompt = (
                f"Extract the number of years of experience required from the following job description:\n\n"
                f"{text}\n\nIf not mentioned, return 'Not Found'."
            )
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=20,
                temperature=0
            )
            return response.choices[0].message['content'].strip()
        except Exception:
            return "Not Found"
