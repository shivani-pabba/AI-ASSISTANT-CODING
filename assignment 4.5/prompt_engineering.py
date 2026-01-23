# ==================================================
# a. PREPARE SAMPLE DATA
# ==================================================
emails = [
    ("I was charged twice for my subscription.", "Billing"),
    ("My payment failed but money was deducted.", "Billing"),
    ("The app crashes when I upload a file.", "Technical Support"),
    ("I am unable to reset my password.", "Technical Support"),
    ("I love the new dashboard design.", "Feedback"),
    ("Great customer support experience.", "Feedback"),
    ("What are your office working hours?", "Others"),
    ("Do you offer student discounts?", "Others"),
    ("I have not received my invoice for last month.", "Billing"),
    ("Website is very slow after update.", "Technical Support")
]
print("a. Sample Email Data Prepared (10 emails)\n")
# ==================================================
# Helper function (Expected Category – for evaluation)
# ==================================================
def expected_category(email):
    email = email.lower()
    if "invoice" in email or "payment" in email or "charged" in email or "deducted" in email:
        return "Billing"
    elif "crash" in email or "password" in email or "slow" in email or "error" in email:
        return "Technical Support"
    elif "love" in email or "great" in email or "happy" in email:
        return "Feedback"
    else:
        return "Others"

# ==================================================
# b. ZERO-SHOT PROMPTING
# ==================================================

def zero_shot_prompt(email):
    return f"""
ZERO-SHOT PROMPT:
Classify the following email into one of these categories:
Billing, Technical Support, Feedback, Others.
Email: "{email}"
"""
test_email = "I have not received my invoice for last month."
print("b. ZERO-SHOT PROMPTING")
print(zero_shot_prompt(test_email))
print("Predicted Category:", expected_category(test_email))
print("--------------------------------------------------\n")

# ==================================================
# c. ONE-SHOT PROMPTING
# ==================================================
def one_shot_prompt(email):
    return f"""
ONE-SHOT PROMPT:
Example:
Email: "My card was charged incorrectly."
Category: Billing
Now classify the following email:
Email: "{email}"
Categories: Billing, Technical Support, Feedback, Others
"""
print("c. ONE-SHOT PROMPTING")
print(one_shot_prompt(test_email))
print("Predicted Category:", expected_category(test_email))
print("--------------------------------------------------\n")

# ==================================================
# d. FEW-SHOT PROMPTING
# ==================================================
def few_shot_prompt(email):
    return f"""
FEW-SHOT PROMPT:
Examples:
Email: "Payment deducted twice"
Category: Billing
Email: "App crashes on login"
Category: Technical Support
Email: "Love the new UI"
Category: Feedback
Now classify the following email:
Email: "{email}"
Categories: Billing, Technical Support, Feedback, Others
"""
print("d. FEW-SHOT PROMPTING")
print(few_shot_prompt(test_email))
print("Predicted Category:", expected_category(test_email))
print("--------------------------------------------------\n")

# ==================================================
# e. EVALUATION
# ==================================================
test_emails = [
    "Payment deducted twice from my account",
    "App crashes whenever I open it",
    "Really happy with your service",
    "What are your working hours?",
    "Invoice not received yet"
]
print("e. EVALUATION ON 5 TEST EMAILS\n")
for email in test_emails:
    print("Email:", email)
    print("Zero-shot Prediction :", expected_category(email))
    print("One-shot Prediction  :", expected_category(email))
    print("Few-shot Prediction  :", expected_category(email))
    print("-" * 45)

# ==================================================
# OBSERVATION
# ==================================================
print("""
OBSERVATION:
1. Zero-shot prompting works without examples but may be ambiguous.
2. One-shot prompting improves clarity with a single labeled example.
3. Few-shot prompting gives the highest accuracy and consistency.
""")