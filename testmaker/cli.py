# CLI entrypoint (argparse/typer)
import sys
import os

def main():
    if len(sys.argv) > 2:
        print("Usage: testmaker <source.py>")
        sys.exit(1)
    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        sys.exit(1)

    output_dir = "tests"
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.basename(input_file)
    name_without_ext = os.path.splitext(base_name)[0]
    output_file = os.path.join(output_dir, f"test_{name_without_ext}.py")


    test_code = generate_test_from_file(input_file)
    with open(output_file, "w"):
        f.write(test_code)
    print(f"test generated at {output_file}")