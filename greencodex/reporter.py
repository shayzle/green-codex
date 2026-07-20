from greencodex.rules import RULES


def build_report(issues, new_score, delta):
    # build the message we show to the developer, line by line
    lines = []
    lines.append("## Green Codex : Carbon Report")
    lines.append("")
    lines.append(f"- SCI Score: {new_score} gCO2 / 1k requests")
    lines.append(f"- Delta vs Main: {delta:+}%")
    lines.append(f"- Issues Found: {len(issues)}")
    lines.append("")

    # if there are no problems,  say so and stop
    if not issues:
        lines.append("No energy issues detected. This PR is clean :)")
        return "\n".join(lines)
    
    # otherwise, list every problem with its message and fix
    lines.append("### Issues")
    for rule_id, filepath, line in issues:
        rule = RULES[rule_id]
        lines.append(f"- {filepath}:{line}")
        lines.append(f" Problem: {rule['message']}")
        lines.append(f" Fix: {rule['fix']}")
        lines.append("")

    return "\n".join(lines)