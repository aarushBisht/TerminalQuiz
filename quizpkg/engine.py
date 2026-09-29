from .models import Question, Scorecard
from .exceptions import InvalidOption

class Engine:
    def __init__(self, raw_data):
        self.questions = [
            Question(q['prompt'], q['options'], q['correct'])
            for q in raw_data
        ]
        self.score_card = Scorecard(len(self.questions))

    def _question_generator(self):
        for q in self.questions:
            yield q

    def run(self):
        print("---- WELCOME TO THE TERMINAL QUIZ ----")

        for idx, question in enumerate(self._question_generator(), 1):
            print(f"\nQuestion {idx}: {question.prompt}")
            for opt_idx, option in enumerate(question.options, 1):
                print(f"  {opt_idx}. {option}")

            while True:
                try:
                    choice = input("Enter your option: ").strip()
                    if not choice:
                        raise InvalidOption("Input cannot be empty.")
                    break
                except InvalidOption as err:
                    print(f"Error: {err}. Please try again.")

            selected_answer = choice
            if choice.isdigit() and 1 <= int(choice) <= len(question.options):
                selected_answer = question.options[int(choice) - 1]

            is_correct = question.check(selected_answer)
            self.score_card.record_attempt(question, selected_answer, is_correct)

            if is_correct:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer was: {question.correct_answer}")

        self.display_results()

    def display_results(self):
        print("\n=== QUIZ COMPLETED ===")
        print(f"Final Score: {self.score_card.score}/{self.score_card.total}")
        print(f"Percentage: {self.score_card.get_percentage():.2f}%")