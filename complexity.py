import sys
import re

def transpile(code: str) -> str:
    replacements = [
        # Functions
        (r'\bWHAT\b', 'def'),
        (r'\bhere\b', 'return'),

        # Conditionals
        (r'\bthis then\b', 'if'),
        (r'\bif aint then\b', 'elif'),
        (r'\baint it then\b', 'else'),
        (r'\bis\b', '=='),
        (r'\bisnt\b', '!='),

        # Loops
        (r'\bspin round while\b', 'while'),
        (r'\bspin round til\b', 'for'),

        # Booleans
        (r'\bdeadass\b', 'True'),
        (r'\bcap\b', 'False'),

        # Print
        (r'\bspitout\b', 'print'),
    ]

    python_lines = []

    # colon checks
    for line in code.splitlines():
        translated = line

        for pattern, replacement in replacements:
            translated = re.sub(pattern, replacement, translated)

        # add colons
        stripped = translated.strip()
        if any(stripped.startswith(k) for k in ["if ", "elif ", "else", "def ", "for ", "while "]):
            if not stripped.endswith(":"):
                translated += ":"

        python_lines.append(translated)

    return "\n".join(python_lines)


def run_file(filename: str):
    with open(filename, "r") as f:
        source_code = f.read()

    py_code = transpile(source_code)
    
    # running the code
    exec(py_code)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 complexity.py <file.complex>")
    else:
        run_file(sys.argv[1])