import os
import json
from quizpkg.storage import DataManager
from quizpkg.exceptions import QuizError
from quizpkg.engine import Engine

def main():
    sample_file = "data/sample_questions.json"
    
    # Auto-generate a rich sample question bank if it doesn't exist
    if not os.path.exists(sample_file):
        os.makedirs("data", exist_ok=True)
        default_data = [
            {
                "prompt": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "lambda"],
                "correct": "def"
            },
            {
                "prompt": "Which built-in module handles operating system interactions?",
                "options": ["sys", "os", "math", "datetime"],
                "correct": "os"
            },
            {
                "prompt": "What is the primary purpose of a Python generator?",
                "options": [
                    "To generate random numbers", 
                    "To yield items lazily using memory-efficient iteration", 
                    "To compile code into machine language", 
                    "To automatically manage database connections"
                ],
                "correct": "To yield items lazily using memory-efficient iteration"
            },
            {
                "prompt": "Which block is used to handle exceptions in Python?",
                "options": ["try-except", "catch-throw", "do-except", "error-handle"],
                "correct": "try-except"
            },
            {
                "prompt": "What does OOP stand for in software development?",
                "options": [
                    "Ordered Operational Processing", 
                    "Object-Oriented Programming", 
                    "Optional Overriding Parameters", 
                    "Open Online Platform"
                ],
                "correct": "Object-Oriented Programming"
            }
        ]
        with open(sample_file, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=4)

    try:
        raw_questions = DataManager.load_questions(sample_file)
        quiz_engine = Engine(raw_questions)
        quiz_engine.run()
    except QuizError as q_err:
        print(f"Quiz Application Error: {q_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()