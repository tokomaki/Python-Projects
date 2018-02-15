"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):
    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    rb = ring_buffer.create(int((SPS / frequency) + 1))
    for i in range(len(rb[0])):
        ring_buffer.enqueue(rb, 0.0)
    return rb


def create_from_samples(init):
    """
    Create and return a guitar string whose size and initial values are given
    by the list init.
    """

    rb = ring_buffer.create(len(init))
    for i in range(len(rb[0])):
        ring_buffer.enqueue(rb, init[i])
    return rb


def pluck(string):
    """
    Pluck the given guitar string by replacing the buffer with white noise.
    """

    for i in range(len(string[0])):
        #string[0][i] = random.uniform(-0.5, 0.5)
        ring_buffer.dequeue(string)
        ring_buffer.enqueue(string, random.uniform(-.5, .5))


def tic(string):
    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    """

    sample_1 = ring_buffer.dequeue(string)
    sample_2 = ring_buffer.peek(string)
    average = .996 * .5 * (sample_1 + sample_2)
    ring_buffer.enqueue(string, average)


def sample(string):
    """
    Return the current sample from the given guitar string.
    """

    return ring_buffer.peek(string)


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()
