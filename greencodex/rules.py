
# this dictionary is the "brain" of green codex
# each rule has a message, a fix suggestion, a severity and an energy weight

RULES = {
    "NESTED_LOOP": {
        "message": "You have a loop inside another loop. This uses a lot of energy.",
        "fix": "Try to use a dictionary instead of the inner loop.",
        "severity": "HIGH",
        "weight": 0.30,
    },
    "QUERY_IN_LOOP": {
        "message": "You are calling the database inside a loop. This is slow and wastes energy.",
        "fix": "Get all the data in one call before the loop.",
        "severity": "HIGH",
        "weight": 0.25,
    },
}


