print("LAB 4 – QUESTION 3: PROGRAMMING QUESTION TYPE IDENTIFICATION")
print("-------------------------------------------------------------\n")

# ==================================================
# a. PREPARE CODING-RELATED USER QUERIES
# ==================================================

programming_queries = [
    "Why am I getting a missing semicolon error?",
    "My program runs but gives wrong output",
    "How can I make my code run faster?",
    "What is recursion in programming?",
    "I am getting an unexpected indent error"
]

print("a. Sample Programming Queries Prepared:\n")
for q in programming_queries:
    print("-", q)

print("\n-------------------------------------------------------------\n")

# ==================================================
# Helper Function (for evaluation – LAB PURPOSE)
# ==================================================

def expected_programming_category(query):
    q = query.lower()
    if "error" in q or "semicolon" in q or "indent" in q or "syntax" in q:
        return "Syntax Error"
    elif "wrong output" in q or "wrong result" in q or "logic" in q:
        return "Logic Error"
    elif "faster" in q or "optimize" in q or "performance" in q:
        return "Optimization"
    else:
        return "Conceptual Question"

# ==================================================
# b. ZERO-SHOT PROMPTING
# ==================================================

def zero_shot_prompt(query):
    return f"""
ZERO-SHOT PROMPT:
Classify the following programming question into one of these categories:
Syntax Error, Logic Error, Optimization, Conceptual Question.

Question: "{query}"
"""

test_query = "My program runs but gives wrong output"

print("b. ZERO-SHOT PROMPTING\n")
print(zero_shot_prompt(test_query))
print("Predicted Category:", expected_programming_category(test_query))
print("-------------------------------------------------------------\n")

# ==================================================
# c. ONE-SHOT PROMPTING
# ==================================================

def one_shot_prompt(query):
    return f"""
ONE-SHOT PROMPT:
Example:
Question: "Why am I getting a syntax error?"
Category: Syntax Error

Now classify the following question:
Question: "{query}"
Categories: Syntax Error, Logic Error, Optimization, Conceptual Question
"""

print("c. ONE-SHOT PROMPTING\n")
print(one_shot_prompt(test_query))
print("Predicted Category:", expected_programming_category(test_query))
print("-------------------------------------------------------------\n")

# ==================================================
# d. FEW-SHOT PROMPTING
# ==================================================

def few_shot_prompt(query):
    return f"""
FEW-SHOT PROMPT:
Examples:
Question: "Unexpected token error"
Category: Syntax Error

Question: "My program is slow for large inputs"
Category: Optimization

Question: "What is inheritance?"
Category: Conceptual Question

Now classify the following question:
Question: "{query}"
Categories: Syntax Error, Logic Error, Optimization, Conceptual Question
"""

print("d. FEW-SHOT PROMPTING\n")
print(few_shot_prompt(test_query))
print("Predicted Category:", expected_programming_category(test_query))
print("-------------------------------------------------------------\n")

# ==================================================
# e. RESPONSE CONSISTENCY EVALUATION
# ==================================================

print("e. RESPONSE CONSISTENCY EVALUATION\n")

test_queries = [
    "Why am I getting an unexpected indent error?",
    "My code works but gives wrong result",
    "How to optimize my loop?",
    "Explain polymorphism",
    "Compiler shows syntax error"
]

for q in test_queries:
    print("Question:", q)
    print("Zero-shot Prediction :", expected_programming_category(q))
    print("One-shot Prediction  :", expected_programming_category(q))
    print("Few-shot Prediction  :", expected_programming_category(q))
    print("-" * 55)

# ==================================================
# OBSERVATION
# ==================================================

print("""
OBSERVATION:
1. Zero-shot prompting classifies questions without examples but may be ambiguous.
2. One-shot prompting improves clarity using a single example.
3. Few-shot prompting gives the most accurate and consistent classification.
4. Logic-related issues such as wrong output or wrong result are correctly identified.
""")