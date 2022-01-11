import numpy as np
import random


class Quad:
    def __init__(self, xmid, ymid, length):
        self.xmid = xmid
        self.ymid = ymid
        self._length = length

    @property
    def length(self):
        return self._length

    def contains_point(self, x, y):
        if (x <= self.xmid + self._length/2.0 and x >= self.xmid - self._length/2.0 and y <= self.ymid+self._length/2.0 and y >= self.ymid-self._length/2.0):
            return True
        else:
            return False

    def NW(self):
        newquad = Quad(self.xmid - self._length/4.0, self.ymid +
                       self._length/4.0, self._length/2.0)
        return newquad

    def NE(self):
        newquad = Quad(self.xmid + self._length/4.0, self.ymid +
                       self._length/4.0, self._length/2.0)
        return newquad

    def SW(self):
        newquad = Quad(self.xmid - self._length/4.0, self.ymid -
                       self._length/4.0, self._length/2.0)
        return newquad

    def SE(self):
        newquad = Quad(self.xmid + self._length/4.0, self.ymid -
                       self._length/4.0, self._length/2.0)
        return newquad
