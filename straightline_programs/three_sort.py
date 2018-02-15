# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

# Takes 3 integers and assigns them to variables a, b, and c
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# Calculate the largest amongst all variables to use in medium value
big_a_b = max(a, b)
big_b_c = max(b, c)
big_a_c = max(a, c)

smallest = min(a, b, c)
medium = min(big_a_b, big_b_c, big_a_c)  # Finds the smallest of the biggest
largest = max(a, b, c)

# Writes result
stdio.writeln(str(smallest) + ' ' + str(medium) + ' ' + str(largest))
