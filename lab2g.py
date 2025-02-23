#!/usr/bin/env python3
# Author: Sultan Mahamud
# Author ID: 113561229
# Date Created: 2024/09/19

import sys  


# IF statement to check if a command-line argument is provided
if len(sys.argv) > 1:
    # Assign the first command-line argument as the timer value, converting it to an integer
    timer = int(sys.argv[1])
else:
    # Default timer value if no argument is provided
    timer = 3

# WHILE loop that runs until timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrement timer

# When timer reaches 0, print "blast off!"
print("blast off!")
