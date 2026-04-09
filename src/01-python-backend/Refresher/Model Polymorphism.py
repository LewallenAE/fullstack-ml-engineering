class ClaudeModel:

    def score(self, prompt: str) -> str:
        return f"Claude scored: {prompt}"


class GPTModel:
    def score(self, prompt: str) -> str:
        return f"GPTModel scoredL: {prompt}"


evaluators: list[ClaudeModel | GPTModel] = [ClaudeModel(), GPTModel()]


for model in evaluators:
    current_score = model.score("toxic prompt")
    print(current_score)
