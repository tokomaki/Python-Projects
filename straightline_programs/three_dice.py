# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

# Creates 3 different random integers between 1 and 6 called a, b, and c
a = random.randrange(1, 7)
b = random.randrange(1, 7)
c = random.randrange(1, 7)

# Writes the sum of the 3 random integers
stdio.writeln(str(a + b + c))
