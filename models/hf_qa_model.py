from transformers import pipeline

class HFQAModel:
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

    @staticmethod
    def extract_experience(text: str) -> str:
        try:
            result = HFQAModel.qa_pipeline({
                "context": text,
                "question": "How many years of experience is required?"
            })
            return result['answer'] if result['score'] > 0.3 else "Not Found"
        except Exception:
            return "Not Found"
