class HeuristicModel:
    @staticmethod
    def extract_experience(text: str) -> str:
        tokens = text.lower().split()
        keywords = ["experience", "experienced"]
        possible_numbers = []

        for i, token in enumerate(tokens):
            if token in keywords:
                for j in range(max(0, i - 4), min(len(tokens), i + 4)):
                    try:
                        num = float(tokens[j].replace("+", "").replace("-", ""))
                        if 0 < num < 50:  # reasonable range
                            possible_numbers.append(f"{num} years")
                    except:
                        continue

        return possible_numbers[0] if possible_numbers else "Not Found"
