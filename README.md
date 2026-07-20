# Green Codex

A green-coding CI/CD linter for Python. Green Codex analyses the carbon impact
of your code on every Pull Request, calculates a Software Carbon Intensity (SCI)
score, and blocks the merge if the code becomes too energy-inefficient.

Think of it as ESLint or SonarQube, but for **energy consumption** instead of
bugs or code style.

## How it works

1. A developer opens a Pull Request on GitHub.
2. Green Codex runs automatically as a GitHub Action.
3. It scans the Python files using static analysis (Python's built-in `ast` module).
4. It detects energy-inefficient patterns (nested loops, database queries in loops).
5. It calculates an SCI score and compares it to a baseline (the delta).
6. If the score gets worse than the allowed threshold, the merge is blocked.

## Rules detected (MVP)

| Rule          | What it catches                     | Severity |
| ------------- | ----------------------------------- | -------- |
| NESTED_LOOP   | A loop inside another loop (O(n^2)) | HIGH     |
| QUERY_IN_LOOP | A database call inside a loop (N+1) | HIGH     |

## Project structure

```
green-codex-project/
  greencodex/
    __init__.py       marks the folder as a Python package
    rules.py          the rulebook: problems and their fixes
    analyzer.py       reads the code and finds the problems
    scorer.py         turns the problems into a carbon score
    reporter.py       writes the readable report
  scan.py             the main file you run; ties everything together
  sample_bad_code.py  test file with intentional problems
  test_greencodex.py  unit tests
  .github/
    workflows/
      carbonlint.yml  the GitHub Action that makes it real CI/CD
  README.md
  LICENSE
```

## Run it locally

```bash
python3 scan.py
```

Clean code prints PASS and exits with code 0. Inefficient code prints the
issues, a FAIL message, and exits with code 1 (which blocks a merge in CI/CD).

## Run the tests

```bash
python3 -m pytest test_greencodex.py -v
```

## Methodology

The scoring follows the Green Software Foundation SCI specification. The energy
weights in `rules.py` are first-pass estimates; calibrating them against real
hardware benchmarks is the next step on the roadmap.

## Roadmap

- Support for JavaScript and Java
- AI-generated fix suggestions (Anthropic API)
- Web dashboard with score history
- CSRD report export (PDF)

## Authors

- Shanisya Lahida
- Sofian Belloul

Web@académie, Epitech Paris

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.
