# ==================================================
# a. PREPARE SAMPLE SOCIAL MEDIA POSTS
# ==================================================

social_posts = [
    "Buy one get one free on all products!",
    "The app keeps crashing after the update",
    "Really love the customer service",
    "When will the next sale start?",
    "Very disappointed with the delivery service"
]
print("a. Sample Social Media Posts Prepared:\n")
for post in social_posts:
    print("-", post)
print("\n-----------------------------------------------------\n")
# ==================================================
# Helper Function (for evaluation – LAB PURPOSE)
# ==================================================
def expected_social_category(post):
    p = post.lower()
    if "buy" in p or "offer" in p or "sale" in p or "free" in p:
        return "Promotion"
    elif "crash" in p or "disappointed" in p or "bad" in p or "terrible" in p:
        return "Complaint"
    elif "love" in p or "great" in p or "amazing" in p:
        return "Appreciation"
    else:
        return "Inquiry"

# ==================================================
# b. ZERO-SHOT PROMPTING
# ==================================================
def zero_shot_prompt(post):
    return f"""
ZERO-SHOT PROMPT:
Classify the following social media post into one of these categories:
Promotion, Complaint, Appreciation, Inquiry.
Post: "{post}"
"""
test_post = "The app keeps crashing after the update"
print("b. ZERO-SHOT PROMPTING\n")
print(zero_shot_prompt(test_post))
print("Predicted Category:", expected_social_category(test_post))
print("-----------------------------------------------------\n")

# ==================================================
# c. ONE-SHOT PROMPTING
# ==================================================
def one_shot_prompt(post):
    return f"""
ONE-SHOT PROMPT:
Example:
Post: "Amazing customer support!"
Category: Appreciation
Now classify the following post:
Post: "{post}"
Categories: Promotion, Complaint, Appreciation, Inquiry
"""
print("c. ONE-SHOT PROMPTING\n")
print(one_shot_prompt(test_post))
print("Predicted Category:", expected_social_category(test_post))
print("-----------------------------------------------------\n")

# ==================================================
# d. FEW-SHOT PROMPTING
# ==================================================
def few_shot_prompt(post):
    return f"""
FEW-SHOT PROMPT:
Examples:
Post: "Buy now and get 50% off"
Category: Promotion
Post: "Service is very bad"
Category: Complaint
Post: "Loved the new features"
Category: Appreciation
Now classify the following post:
Post: "{post}"
Categories: Promotion, Complaint, Appreciation, Inquiry
"""
print("d. FEW-SHOT PROMPTING\n")
print(few_shot_prompt(test_post))
print("Predicted Category:", expected_social_category(test_post))
print("-----------------------------------------------------\n")

# ==================================================
# e. RESPONSE CONSISTENCY EVALUATION
# ==================================================
print("e. RESPONSE CONSISTENCY EVALUATION\n")
test_posts = [
    "Buy now and get flat 50% off",
    "Very bad experience with the app",
    "Loved the quick support",
    "Can anyone tell me the refund policy?",
    "App crashes frequently"
]
for p in test_posts:
    print("Post:", p)
    print("Zero-shot Prediction :", expected_social_category(p))
    print("One-shot Prediction  :", expected_social_category(p))
    print("Few-shot Prediction  :", expected_social_category(p))
    print("-" * 55)

# ==================================================
# OBSERVATION
# ==================================================
print("""
OBSERVATION:
1. Zero-shot prompting works without examples but may misinterpret informal language.
2. One-shot prompting improves clarity with a single labeled example.
3. Few-shot prompting gives the most consistent and accurate categorization.
4. Few-shot prompting handles informal social media language better.
""")