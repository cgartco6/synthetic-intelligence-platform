class Evaluator:
    def score(self, output):
        score = min(10, len(output) // 50)
        return score

    def improve(self, output):
        return output + " [Improved]"
