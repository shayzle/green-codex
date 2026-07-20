import ast

def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    # turn the code text into a tree we can search through
    tree = ast.parse(source)
    issues = []

    # look at every single piece of the code, one by one
    for node in ast.walk(tree):

        # rule 1 : is this a loop with another loop inside it?
        if isinstance(node, ast.For):
            for inner in ast.walk(node):
                if isinstance(inner, ast.For) and inner is not node:
                    issues.append(("NESTED_LOOP", filepath, node.lineno))
                    break
        
        # rule 2 : is this a loop that calls the database inside it?
        if isinstance(node, ast.For):
            for inner in ast.walk(node):
                if isinstance(inner, ast.Call) and _is_db_call(inner):
                    issues.append(("QUERY_IN_LOOP", filepath, node.lineno))
                    break
    
    return issues


def _is_db_call(call_node):
    # check if the thing being called is named "query"
    if isinstance(call_node.func, ast.Attribute):
        return call_node.func.attr == "query"
    return False 