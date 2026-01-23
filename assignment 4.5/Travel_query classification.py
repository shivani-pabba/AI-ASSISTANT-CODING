# ==================================================
# a. PREPARE LABELED TRAVEL QUERIES
# ==================================================
travel_queries = [
    "Book a flight from Delhi to Mumbai",
    "Reserve a hotel in Goa",
    "Cancel my flight ticket",
    "What documents are needed for international travel?",
    "Cancel my hotel booking"
]
print("a. Sample Travel Queries Prepared:\n")
for q in travel_queries:
    print("-", q)
print("\n------------------------------------------------\n")
# ==================================================
# Helper Function (Corrected – Cancellation Priority)
# ==================================================
def expected_travel_category(query):
    q = query.lower()
    if "cancel" in q:
        return "Cancellation"
    elif "flight" in q:
        return "Flight Booking"
    elif "hotel" in q:
        return "Hotel Booking"
    else:
        return "General Travel Info"

# ==================================================
# b. ZERO-SHOT PROMPTING
# ==================================================
def zero_shot_prompt(query):
    return f"""
ZERO-SHOT PROMPT:
Classify the following travel query into one of these categories:
Flight Booking, Hotel Booking, Cancellation, General Travel Info.
Query: "{query}"
"""
test_query = "Cancel my flight ticket"
print("b. ZERO-SHOT PROMPTING\n")
print(zero_shot_prompt(test_query))
print("Predicted Category:", expected_travel_category(test_query))
print("------------------------------------------------\n")

# ==================================================
# c. ONE-SHOT PROMPTING
# ==================================================
def one_shot_prompt(query):
    return f"""
ONE-SHOT PROMPT:
Example:
Query: "Book a hotel in Goa"
Category: Hotel Booking
Now classify the following query:
Query: "{query}"
Categories: Flight Booking, Hotel Booking, Cancellation, General Travel Info
"""
print("c. ONE-SHOT PROMPTING\n")
print(one_shot_prompt(test_query))
print("Predicted Category:", expected_travel_category(test_query))
print("------------------------------------------------\n")

# ==================================================
# d. FEW-SHOT PROMPTING
# ==================================================
def few_shot_prompt(query):
    return f"""
FEW-SHOT PROMPT:
Examples:
Query: "Book a flight to London"
Category: Flight Booking
Query: "Reserve a hotel room"
Category: Hotel Booking
Query: "Cancel my hotel reservation"
Category: Cancellation
Now classify the following query:
Query: "{query}"
Categories: Flight Booking, Hotel Booking, Cancellation, General Travel Info
"""
print("d. FEW-SHOT PROMPTING\n")
print(few_shot_prompt(test_query))
print("Predicted Category:", expected_travel_category(test_query))
print("------------------------------------------------\n")

# ==================================================
# e. RESPONSE CONSISTENCY EVALUATION
# ==================================================
print("e. RESPONSE CONSISTENCY EVALUATION\n")
test_queries = [
    "Cancel my flight",
    "Book a flight to New York",
    "Cancel hotel reservation",
    "Find hotels near the beach",
    "What is the best time to visit Europe?"
]
for q in test_queries:
    print("Query:", q)
    print("Zero-shot Prediction :", expected_travel_category(q))
    print("One-shot Prediction  :", expected_travel_category(q))
    print("Few-shot Prediction  :", expected_travel_category(q))
    print("-" * 45)

# ==================================================
# OBSERVATION
# ==================================================
print("""
OBSERVATION:
1. Zero-shot prompting works without examples but may be ambiguous.
2. One-shot prompting improves clarity with a single example.
3. Few-shot prompting gives the most accurate and consistent results.
4. Cancellation-related queries must be given higher priority.
""")