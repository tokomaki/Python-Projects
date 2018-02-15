# order_check.py: Takes three floats values x, y, and z as command-line
# arguments and prints True if the values are strictly ascending or
# descending (i.e., x<y<z or x>y>z), and False otherwise.

import stdio
import sys

# Takes and assigns float values x, y, and z
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

# Prints True if values are either ascending or descending
# and prints False otherwise
stdio.writeln(x < y < z or x > y > z)
