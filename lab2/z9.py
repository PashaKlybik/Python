__author__ = 'pasha'

class Xrange():
    def _check(self):
        print(self.h,self.start,self.end)
        if self.h>0:
            return self.start <= self.end
        else:
            return self.end <= self.start

    def __init__(self, end, start = 0, h = 1):
        self.start = start
        self.end = end
        self.h = h

    def __iter__(self):
        return self

    def next(self):
        while Xrange._check(self):
            print(self.start)
            self.start += self.h
            print
            yield self.start
        raise StopIteration

