# logic to scan .py file, detect functions/classes
import ast
import os

def extract_classes_and_functions(source: str):
    tree = ast.parse(source)
    data = {"functions": [], "classes": {}}

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            data["functions"].append(node.name)

        elif isinstance(node, ast.ClassDef):
            methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            data["classes"][node.name] = methods

    return data

def generate_test_from_file(input_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} not found")

    with open(input_file, "r") as f:
        source = f.read()
    ClassAndFunction = extract_classes_and_functions(source)