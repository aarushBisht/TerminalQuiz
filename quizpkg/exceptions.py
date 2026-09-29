class QuizError(Exception):
    """Base class for all quiz-related exceptions."""
    pass

class QuestionNotFound(QuizError):
    """Raised when a question bank file is empty or missing questions."""
    pass

class InvalidOption(QuizError):
    """Raised when the user enters an invalid option choice."""
    pass