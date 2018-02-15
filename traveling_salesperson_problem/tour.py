import stdio
from point import Point


class Tour:
    """
    Represents a tour in the traveling salesperson problem.
    """

    def __init__(self):
        """
        Creates an empty tour.
        """

        self._tour = []

    def show(self):
        """
        Prints the tour to standard output.
        """

        for v in self._tour:
            stdio.writeln(v)

    def draw(self):
        """
        Draws the tour to standard output.
        """

        for i in range(self.size()):
            q = self._tour[i]
            a = self._tour[(i + 1) % self.size()]
            q.drawTo(a)

    def size(self):
        """
        Returns the number of points on the tour.
        """

        return len(self._tour)

    def distance(self):
        """
        Returns the total distance of the tour.
        """

        distance = 0.0
        size = self.size()
        for i in range(1, size + 1):
            q = self._tour[i % size]
            a = self._tour[i - 1]
            distance += q.distanceTo(a)
        return distance

    def insertNearest(self, p):
        """
        Inserts the point p using the nearest neighbor heuristic.
        """

        close_dist = float("inf")
        close_index = 0
        for i, v in enumerate(self._tour):
            if v.distanceTo(p) < close_dist:
                close_dist = v.distanceTo(p)
                close_index = i + 1
        self._tour.insert(close_index, p)

    def insertSmallest(self, p):
        """
        Inserts the point p using the smallest increment heuristic.
        """

        close_dist = float("inf")
        close_index = 0
        size = self.size()
        for i in range(1, size + 1):
            distance = (p.distanceTo(self._tour[i % size]) -
                        self._tour[i - 1].distanceTo(self._tour[i % size]) +
                        p.distanceTo(self._tour[i - 1]))
            if distance < close_dist:
                close_dist = distance
                close_index = i
        self._tour.insert(close_index, p)


# Test client [DO NOT EDIT]. Sets up and shows a tour of four points, using
# both nearest neighbor and smallest insertion heuristic.
def _main():
    a = Point(200.0, 400.0)
    b = Point(300.0, 100.0)
    c = Point(100.0, 100.0)
    d = Point(300.0, 200.0)
    tour1 = Tour()
    tour1.insertNearest(a)
    tour1.insertNearest(b)
    tour1.insertNearest(c)
    tour1.insertNearest(d)
    stdio.writeln('Tour 1:~')
    tour1.show()
    stdio.writef('Tour distance = %f\n', tour1.distance())
    stdio.writef('Number of points = %d\n', tour1.size())
    tour2 = Tour()
    tour2.insertSmallest(a)
    tour2.insertSmallest(b)
    tour2.insertSmallest(c)
    tour2.insertSmallest(d)
    stdio.writeln('Tour 2:~')
    tour2.show()
    stdio.writef('Tour distance = %f\n', tour2.distance())
    stdio.writef('Number of points = %d\n', tour2.size())

if __name__ == '__main__':
    _main()
