#!/usr/bin/env python3

import sys

# Ensure enough arguments are provided
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument (name)
age = sys.argv[2]  # Second argument (age)

# Output the message
print(f"Hi {name}, you are {age} years old.")

