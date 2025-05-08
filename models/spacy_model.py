import spacy
from spacy.matcher import Matcher

class SpacyModel:
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)

    # Define patterns
    patterns = [
        [{"LIKE_NUM": True}, {"LOWER": {"IN": ["years", "year", "yrs", "yr"]}}],
        [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["years", "year", "yrs", "yr"]}}],
    ]
    matcher.add("ExperiencePattern", patterns)

    @staticmethod
    def extract_experience(text: str) -> str:
        doc = SpacyModel.nlp(text)
        matches = SpacyModel.matcher(doc)
        for match_id, start, end in matches:
            return doc[start:end].text
        return "Not Found"
