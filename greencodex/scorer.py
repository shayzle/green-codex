from greencodex.rules import RULES

# the score of the code before this change
# we use a fixed number so the demo always behaves the same
BASELINE_SCORE = 1.72


def compute_score(issues):
    # gives the total score
    # start from the baseline, then add the cost of each problem found
    extra = 0.0
    for rule_id, filepath, line in issues:
        extra = extra + RULES[rule_id]["weight"]
    return round(BASELINE_SCORE + extra, 2)

def compute_delta(new_score):
    # says how much it changed compared to before
    # how much worse (or better) is the new score vs the baseline, as a percent
    delta = ((new_score - BASELINE_SCORE) / BASELINE_SCORE) * 100
    return round(delta, 1)