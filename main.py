import pandas as pd
from models import (
    SpacyModel,
    HFQAModel,
    LangchainModel,
    OpenAIModel,
    HeuristicModel
)

from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os

# Load Excel file
input_path ="Job Descriptions 2.xlsx"
output_path = "output/model_comparison_output.xlsx"

def load_data():
    df = pd.read_excel(input_path)
    if "JD_Text" not in df.columns:
        raise ValueError("Excel must have a 'Job Description' column.")
    return df

def run_models_on_text(text):
    return {
        "Spacy": SpacyModel.extract_experience(text),
        "HuggingFace_QA": HFQAModel.extract_experience(text),
        "Langchain": LangchainModel.extract_experience(text),
        "OpenAI": OpenAIModel.extract_experience(text),
        "Heuristic": HeuristicModel.extract_experience(text),
    }

def main():
    print("Loading data...")
    df = load_data()

    print("Running models...")
    results = []
    with ThreadPoolExecutor() as executor:
        for output in tqdm(executor.map(run_models_on_text, df["JD_Text"]), total=len(df)):
            results.append(output)

    
    for model_name in results[0].keys():
        df[model_name] = [r[model_name] for r in results]

    
    os.makedirs("output", exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"✅ Output saved to {output_path}")

if __name__ == "__main__":
    main()
