class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def check(self, user_choice):
        return user_choice.strip().lower() == self.correct_answer.strip().lower()

class Scorecard:
    def __init__(self, total_questions):
        self.total = total_questions
        self.score = 0
        self.history = []

    def record_attempt(self, question, user_ans, is_correct):
        if is_correct:
            self.score += 1
        self.history.append({
            "prompt": question.prompt,
            "user_answer": user_ans,
            "correct": is_correct
        })

    def get_percentage(self):
        if self.total == 0:
            return 0.0
        return (self.score / self.total) * 100