from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class LangchainModel:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  # Assumes OpenAI key is set in ENV

    prompt_template = PromptTemplate.from_template("""
    Extract only the number of years of experience required from this job description:
    {jd}
    If not found, return "Not Found".
    """)

    @staticmethod
    def extract_experience(text: str) -> str:
        try:
            prompt = LangchainModel.prompt_template.format(jd=text)
            response = LangchainModel.llm.predict(prompt)
            return response.strip()
        except Exception:
            return "Not Found"
