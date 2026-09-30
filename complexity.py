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

        # Print (handy function call formatting)
        (r'\bspitout\b', 'print'),
    ]

    python_lines = []

    # Loop line by line so replacement & colon checks work properly
    for line in code.splitlines():
        translated = line

        # Apply all keyword replacements
        for pattern, replacement in replacements:
            translated = re.sub(pattern, replacement, translated)

        # Auto-add colons to Python block headers if missing
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
    
    # Run the transpiled python code directly
    exec(py_code)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 complexity.py <file.complex>")
    else:
        run_file(sys.argv[1])