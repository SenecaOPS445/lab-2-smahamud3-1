#!/usr/bin/env python3
# Author: Sultan Mahamud
# Author ID: 113561229
# Date Created: 2024/09/19

import sys  


# Check if the correct number of arguments is provided

if len(sys.argv) < 2:
    print("Error: Please provide a starting timer value as an argument.")
    sys.exit(1)

# Assign the first command line argument as the initial timer value, converting it to an integer
timer = int(sys.argv[1])

# WHILE loop that runs until timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrement timer

# When timer reaches 0, print "blast off!"
print("blast off!")

