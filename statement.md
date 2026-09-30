# Project Statement: Terminal Quiz Application

## Problem Statement
Traditional text-based or static testing scripts often lack robust input validation, scalable package structures, and structured exception handling. When users input unexpected values, blank entries, or malformed data files, standard scripts tend to crash unexpectedly. Furthermore, hardcoded question banks lack extensibility. This project solves these challenges by providing a modular, robust command-line application that dynamically loads question data from persistent JSON storage, validates user inputs securely using custom exception classes, and manages quiz state cleanly via object-oriented modeling.

## Scope of the Project
The scope of this project includes:
- Designing a modular Python package (`quizpkg`) separating data storage, execution engines, domain models, and custom exceptions.
- Implementing file I/O operations to read questions dynamically from external JSON data files.
- Utilizing generator functions for memory-efficient iteration over questions.
- Handling edge cases and user input errors gracefully through a custom exception hierarchy.
- Providing a clean Command-Line Interface (CLI) for running interactive quizzes and tracking final scores.

## Target Users
- **Students & Learners:** Individuals learning Python programming concepts such as Object-Oriented Programming (OOP), file handling, custom exceptions, and generators.
- **Instructors & Evaluators:** Educators looking for modular code structure and robust software engineering patterns in student CLI applications.

## High-Level Features
- **Dynamic Question Loading:** Automatically reads question sets from a structured JSON data file.
- **Object-Oriented Design:** Encapsulates quiz logic within clean class models (`Question`, `Scorecard`).
- **Generator-Based Iteration:** Streams questions sequentially using Python generator functions for optimized performance.
- **Custom Exception Handling:** Catches invalid inputs, out-of-range selections, and missing files gracefully.
- **Interactive Score Tracking:** Evaluates user answers and calculates final percentages upon completion.