import stddraw
import stdio
import sys
from point import Point
from tour import Tour


# Reads in points from standard input; runs the nearest neighbor heuristic;
# prints the resulting tour, its distance, and its number of points to
# standard output; and displays the resulting tour on standard draw for
# t milliseconds, where t is a command-line argument.
def main():
    t = int(sys.argv[1])
    w = stdio.readInt()
    h = stdio.readInt()
    stddraw.setCanvasSize(w, h)
    stddraw.setXscale(0, w)
    stddraw.setYscale(0, h)
    stddraw.setPenRadius(.005)

    tour = Tour()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        p = Point(x, y)
        tour.insertNearest(p)
    tour.draw()
    stddraw.show(t)
    tour.show()
    stdio.writef('Tour distance = %f\n', tour.distance())
    stdio.writef('Number of points = %d\n', tour.size())

if __name__ == '__main__':
    main()
