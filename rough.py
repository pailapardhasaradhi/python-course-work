def welcome():
    print(" Welcome to the Python Quiz Game!\n")

def get_questions():
    return [
        {
            "question": "1. What is the output of: print(10 > 5 and 5 < 2)?",
            "options": {"a": "True", "b": "False", "c": "None", "d": "Error"},
            "answer": "b"
        },
        {
            "question": "2. Which data structure does not allow duplicate values?",
            "options": {"a": "List", "b": "Tuple", "c": "Set", "d": "Dictionary"},
            "answer": "c"
        },
        {
            "question": "3. What is the default return value of a function that doesn't explicitly return anything?",
            "options": {"a": "0", "b": "None", "c": "False", "d": "''"},
            "answer": "b"
        },
        {
            "question": "4. Which function is used to get input from the user?",
            "options": {"a": "scan()", "b": "get()", "c": "input()", "d": "read()"},
            "answer": "c"
        },
        {
            "question": "5. Which keyword is used to create a class in Python?",
            "options": {"a": "def", "b": "class", "c": "function", "d": "object"},
            "answer": "b"
        },
        {
            "question": "6. Which of the following is not a valid Python loop?",
            "options": {"a": "for", "b": "while", "c": "loop", "d": "none"},
            "answer": "c"
        },
        {
            "question": "7. What is the output of: print(2 ** 3 ** 1)?",
            "options": {"a": "64", "b": "8", "c": "16", "d": "6"},
            "answer": "a"
        },
        {
            "question": "8. Which function returns the number of items in an object?",
            "options": {"a": "size()", "b": "count()", "c": "length()", "d": "len()"},
            "answer": "d"
        },
        {
            "question": "9. What does 'break' do in a loop?",
            "options": {"a": "Skips current iteration", "b": "Stops the loop", "c": "Repeats the loop", "d": "Ends program"},
            "answer": "b"
        },
        {
            "question": "10. What is the output of: print(type(True))?",
            "options": {"a": "<class 'int'>", "b": "<class 'bool'>", "c": "<class 'str'>", "d": "<class 'float'>"},
            "answer": "b"
        },
        {
            "question": "11. Which keyword is used to define a function?",
            "options": {"a": "function", "b": "define", "c": "def", "d": "fun"},
            "answer": "c"
        },
        {
            "question": "12. How do you create a dictionary?",
            "options": {"a": "{}", "b": "[]", "c": "()", "d": "<>"},
            "answer": "a"
        },
        {
            "question": "13. What is the result of: 'Python'[0]?",
            "options": {"a": "'P'", "b": "'y'", "c": "'n'", "d": "Error"},
            "answer": "a"
        },
        {
            "question": "14. What is the correct way to start a function?",
            "options": {"a": "function myFunc():", "b": "def myFunc():", "c": "fun myFunc():", "d": "create myFunc():"},
            "answer": "b"
        },
        {
            "question": "15. What is the value of x after: x = [1, 2, 3]; x.append(4)?",
            "options": {"a": "[1, 2, 3, 4]", "b": "[1, 2, 3]", "c": "[4, 1, 2, 3]", "d": "[1, 2, 3][4]"},
            "answer": "a"
        },
        {
            "question": "16. Which of these is not a data type in Python?",
            "options": {"a": "int", "b": "char", "c": "float", "d": "str"},
            "answer": "b"
        },
        {
            "question": "17. Which symbol is used for comments in Python?",
            "options": {"a": "//", "b": "#", "c": "--", "d": "<!--"},
            "answer": "b"
        },
        {
            "question": "18. How do you check if 'x' is equal to 10?",
            "options": {"a": "x = 10", "b": "x == 10", "c": "x === 10", "d": "x != 10"},
            "answer": "b"
        },
        {
            "question": "19. What is the output of: print(len('abc'))?",
            "options": {"a": "2", "b": "3", "c": "1", "d": "4"},
            "answer": "b"
        },
        {
            "question": "20. Which function is used to convert string to lowercase?",
            "options": {"a": "str.lower()", "b": "lowercase()", "c": "toLower()", "d": "str.lowercase()"},
            "answer": "a"
        },
    ]

def ask_question(q, index):
    print(f"{q['question']}")
    for key, val in q["options"].items():
        print(f"{key}) {val}")
    answer = input("Your answer (a/b/c/d): ").strip().lower()
    if answer == q["answer"]:
        print("✅ Correct!\n")
        return 1
    else:
        print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")
        return 0

def run_quiz():
    welcome()
    questions = get_questions()
    score = 0
    for i in range(len(questions)):
        score += ask_question(questions[i], i)
    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Perfect score! You’re a Python pro!")
    elif score >= 15:
        print("🎉 Great job! Keep practicing!")
    else:
        print("📘 Keep learning. You’ll get better!")

run_quiz()
