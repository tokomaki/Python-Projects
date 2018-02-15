# alignment.py: Reads from standard input, the output produced by
# edit_distance.py, i.e., input strings x and y, and the opt matrix. The
# program then recovers an optimal alignment from opt, and writes to
# standard output the edit distance between x and y and the alignment itself.

# Import necessary modules.
import stdarray
import stdio
import sys

# Read x, y, and opt from standard input.
x = stdio.readString()
y = stdio.readString()
opt = stdarray.readInt2D()

# Compute M and N
M = len(x)
N = len(y)

# Write edit distance between x and y.
stdio.writeln('Edit distance = ' + str(opt[0][0]))

# Recover and write an optimal alignment.
i = 0
j = 0
while i < M and j < N:
    if opt[i][j] == opt[i + 1][j] + 2:
        stdio.writeln(x[i] + ' - 2')
        i += 1
    elif opt[i][j] == opt[i][j + 1] + 2:
        stdio.writeln('- ' + y[j] + ' 2')
        j += 1
    elif opt[i][j] == opt[i + 1][j + 1]:
        stdio.writeln(x[i] + ' ' + y[j] + ' 0')
        i += 1
        j += 1
    elif opt[i][j] == opt[i + 1][j + 1] + 1:
        stdio.writeln(x[i] + ' ' + y[j] + ' 1')
        i += 1
        j += 1
while i < M:
    stdio.writeln(x[i] + ' - 2')
    i += 1
while j < N:
    stdio.writeln('- ' + y[j] + ' 2')
    j += 1
