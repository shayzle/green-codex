import sys
import glob
from greencodex.analyzer import analyze_file
from greencodex.scorer import compute_score, compute_delta
from greencodex.reporter import build_report

# how much worse a PR is allowed to be before i block it
THRESHOLD = 10.0


def main():
    # find every python file in the project
    # skip our own tool files and test files
    files = glob.glob("**/*.py", recursive=True)
    files = [f for f in files if "greencodex" not in f and "scan.py" not in f and "test" not in f]

    # collect all problems from all files
    all_issues = []
    for filepath in files:
        all_issues = all_issues + analyze_file(filepath)
    
    # calculate the score and the change
    score = compute_score(all_issues)
    delta = compute_delta(score)

    # build and print the report
    report = build_report(all_issues, score, delta)
    print(report)

    # decide if the check passes or fails
    if delta > THRESHOLD:
        print(f"\nFAIL: the code got {delta:+}% worse (limit is +{THRESHOLD}%)")
        sys.exit(1)
    else:
        print(f"\nPASS: the code is within the limit")
        sys.exit(0)


if __name__ == "__main__":
    main()
    