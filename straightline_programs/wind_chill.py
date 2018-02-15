# wind_chill.py: Takes two floats t and v as command-line arguments and
# prints the wind chill w, calculated as w=35.74+0.6215t+(0.4275t-35.75)v^0.16.

import stdio
import sys
import math

t = float(sys.argv[1])    # Take a float t for temperature
v = float(sys.argv[2])    # Take a float v for wind speed

# Calculate and write the windchill
stdio.writeln(str(35.74 + 0.6215 * t
                  + (0.4275 * t - 35.75) * v ** .16))
