import json
import os
from .exceptions import QuestionNotFound

class DataManager:
    @staticmethod
    def load_questions(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Question file not found at: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            raise QuestionNotFound("Question database is empty.")

        return data

    @staticmethod
    def save_report(report_data, output_path="reports/history.json"):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=4)
        except IOError as e:
            print(f"Warning: Could not save report: {e}")