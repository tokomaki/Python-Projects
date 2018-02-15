# bmi.py: Takes two floats w (for weight) and h (for height) as command-line
# arguments and prints the body mass index (BMI), calculated as the ratio of
# the weight to the square of the height.

import stdio
import sys
import math

w = float(sys.argv[1])    # Take a float w for weight
h = float(sys.argv[2])    # Take a float h for height

stdio.writeln(str(w / h ** 2))    # Calculates and writes bmi ratio
