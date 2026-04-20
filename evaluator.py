import time

class SystemEvaluator:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start_timer(self):
        self.start_time = time.perf_counter()

    def stop_timer(self):
        self.end_time = time.perf_counter()
        return round(self.end_time - self.start_time, 3)

    def estimate_cost(self, model_name: str, tokens: int = 500):
        """
        AI PM Logic: Budgeting for scale.
        Llama 3.3 70B on Groq is roughly $0.79 per million tokens.
        """
        cost_per_1k = 0.00079 # Example rate
        estimated = (tokens / 1000) * cost_per_1k
        return f"${estimated:.6f}"