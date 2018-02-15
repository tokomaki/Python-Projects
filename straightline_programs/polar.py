# polar.py: Takes two floats x and y representing the Cartesian coordinates of
# a point as command-line arguments and prints the corresponding polar
# coordinates, calculated as r=(x^2+y^2)^0.5 and theta=arctan(y/x).

import math
import stdio
import sys

x = float(sys.argv[1])    # Takes a float x
y = float(sys.argv[2])    # Takes a float y

# Calculates r and theta coordinates
r = (x**2 + y**2)**.5
theta = math.atan(y / x)

# Writes r and theta coordinates
stdio.writeln(str(r))
stdio.writeln(str(theta))
