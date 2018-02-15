"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self.k = k
        self.st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i + k]
            nextchar = circ_text[i + k]
            self.st.setdefault(kgram, {})
            self.st[kgram].setdefault(nextchar, 0)
            self.st[kgram][nextchar] += 1

    def order(self):
        """
        Returns order k of Markov model.
        """

        return self.k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))
        elif kgram not in self.st:
            return 0
        count = 0
        for v in self.st[kgram].values():
            count += v
        return count

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))
        elif kgram not in self.st or c not in self.st[kgram]:
            return 0
        return self.st[kgram][c]

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self.k))
        if kgram not in self.st:
            raise ValueError('Unknown kgram ' + kgram)
        key_list = self.st[kgram].keys()
        value_list = self.st[kgram].values()
        rand = stdrandom.discrete(value_list)
        return key_list[rand]

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """

        string = kgram
        while len(string) < T:
            string += self.rand(string[-self.k:])
        return string

    def replace_unknown(self, corrupted):
        """
        Replaces unknown characters (~) in corrupted with most probable
        characters, and returns that string.
        """

        # Given a list a, argmax returns the index of the maximum element in a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram = corrupted[i-self.k:i]
                c_list = self.st[kgram].keys()
                change = [kgram[1:] + c for c in c_list]
                for v in c_list:
                    probs_list = []
                    probs = 1
                    for k in range(1, self.k + 1):
                        numer = self.char_freq(kgram, v)
                        denom = float(self.kgram_freq(kgram))
                        probs *= numer / denom
                        probs_list.append(probs)
                index = argmax(probs_list)
                original += c_list[index]
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text = 'banana'
    k = 2
    model = MarkovModel(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'an\', \'a\')  = %d\n', model.char_freq('an', 'a'))
    stdio.writef('freq(\'na\', \'b\')  = %d\n', model.char_freq('na', 'b'))
    stdio.writef('freq(\'na\', \'a\')  = %d\n', model.char_freq('na', 'a'))
    stdio.writef('freq(\'na\')       = %d\n', model.kgram_freq('na'))
    stdio.writeln()
    text = 'one fish two fish red fish blue fish'
    k = 4
    model = MarkovModel(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'ish \', \'r\') = %d\n', model.char_freq('ish ', 'r'))
    stdio.writef('freq(\'ish \', \'0\') = %d\n', model.char_freq('ish ', '0'))
    stdio.writef('freq(\'ish \')      = %d\n', model.kgram_freq('ish '))
    stdio.writef('freq(\'tuna\')      = %d\n', model.kgram_freq('tuna'))
    stdio.writeln()
    text = 'gagggagaggcgagaaa'
    k = 2
    model = MarkovModel(text, k)
    stdio.writef('text: %s, k = %d\n', text, k)
    stdio.writef('freq(\'aa\', \'a\') = %d\n', model.char_freq('aa', 'a'))
    stdio.writef('freq(\'ga\', \'g\') = %d\n', model.char_freq('ga', 'g'))
    stdio.writef('freq(\'gg\', \'c\') = %d\n', model.char_freq('gg', 'c'))
    stdio.writef('freq(\'ag\')      = %d\n', model.kgram_freq('ag'))
    stdio.writef('freq(\'cg\')      = %d\n', model.kgram_freq('cg'))
    stdio.writef('freq(\'gc\')      = %d\n', model.kgram_freq('gc'))

if __name__ == '__main__':
    _main()
