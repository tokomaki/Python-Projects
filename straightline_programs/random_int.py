# random_integer.py: Takes two integers a and b from the command line and
# writes a random integer between a (inclusive) and b (exclusive).

import random
import stdio
import sys

# Takes and assigns integers a and b
a = int(sys.argv[1])
b = int(sys.argv[2])

# Writes random integer from range including a and excluding b
stdio.writeln(str(random.randrange(a, b)))
