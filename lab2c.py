#!/usr/bin/env python3

import sys

# Ensure enough arguments are provided
if len(sys.argv) < 3:
    print("Error: You must provide both a name and an age.")
    sys.exit(1)

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument (name)
age = int(sys.argv[2])  # Second argument (age)

# Output the message
print(f"Hi {name}, you are {age} years old.")

