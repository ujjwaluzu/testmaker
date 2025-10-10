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
def test_sub(func_name):
     return f"""def test_{func_name}():
    # TODO: write test for {func_name}
    assert False
"""

def generate_test_from_file(input_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} not found")

    with open(input_file, "r") as f:
        source = f.read()
    ClassAndFunction = extract_classes_and_functions(source)
    test_code = "# Auto-generated test file\n\nimport pytest\n\n"

    # Generate test stubs for top-level functions
    for func in ClassAndFunction["functions"]:
        test_code += test_sub(func)

    # Generate test stubs for class methods
    for cls, methods in ClassAndFunction["classes"].items():
        test_code += f"\nclass Test{cls}:\n"
        if not methods:
            test_code += "    pass\n"
        for method in methods:
            test_code += f"""    def test_{method}(self):
        # TODO: write test for {cls}.{method}
        assert False

"""

    return test_code
