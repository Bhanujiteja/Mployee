# This project compares multiple NLP models for extracting years of experience required from job descriptions using:

- SpaCy Rule-based Matcher
- Hugging Face Question-Answering Pipeline
- LangChain with OpenAI (GPT-3.5)
- OpenAI GPT-3.5 via API
- Heuristic-based Rule Extractor

# Comparing model outputs:

SpacyModel: 3 years
HFQAModel: 3 years
LangchainModel: 3 years
OpenAIModel: 3 years
HeuristicModel: 3.0 years

# Overall Best: OpenAIModel
If you're choosing one model for real-world usage where varied phrasing is expected and accuracy is critical, the OpenAIModel is the most capable 