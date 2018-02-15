# mercator.py: Takes three floats l0, phi, and l as command-line arguments and
# prints its projection, i.e., the x and y values separated by a space,
# calculated using x=l-l0 and y=ln(1+sin(phi)/(1-sin(phi)))/2.

import math
import stdio
import sys

# Take and assign floats l0, phi, and l
l0 = float(sys.argv[1])
phi = float(sys.argv[2])
l = float(sys.argv[3])

# Calculates x and y values
x = l - l0
y = math.log((1 + math.sin(math.radians(phi)))
             / (1 - math.sin(math.radians(phi)))) / 2

# Formats and writes coordinates
stdio.writeln(str(x) + ' ' + str(y))
