import numpy as np
import webcolors


def is_external(tree):
    if (tree.NW == None and tree.NE == None and tree.SE == None and tree.SW == None):
        return True
    else:
        return False


class BHTree():
    def __init__(self, quadrant):
        self.quadrant = quadrant
        self.body = None
        self.NW = None
        self.NE = None
        self.SE = None
        self.SW = None

    def insert(self, b):
        if self.body == None:
            self.body = b
        elif is_external(self) == False:
            self.body = b.add(self.body)

            northwest = self.quadrant.NW()
            if b.is_in(northwest):
                if (self.NW == None):
                    self.NW = BHTree(northwest)
                self.NW.insert(b)
            else:
                northeast = self.quadrant.NE()
                if b.is_in(northeast):
                    if self.NE == None:
                        self.NE = BHTree(northeast)
                    self.NE.insert(b)
                else:
                    southeast = self.quadrant.SE()
                    if b.is_in(southeast):
                        if self.SE == None:
                            self.SE = BHTree(southeast)
                        self.SE.insert(b)
                    else:
                        southwest = self.quadrant.SW()
                        if b.is_in(southwest):
                            if self.SW == None:
                                self.SW = BHTree(southwest)
                            self.SW.insert(b)
        elif is_external(self):
            c = self.body
            northwest = self.quadrant.NW()
            if c.is_in(northwest):
                if self.NW == None:
                    self.NW = BHTree(northwest)
                self.NW.insert(c)
            else:
                northeast = self.quadrant.NE()
                if c.is_in(northeast):
                    if self.NE == None:
                        self.NE = BHTree(northeast)
                    self.NE.insert(c)
                else:
                    southeast = self.quadrant.SE()
                    if c.is_in(southeast):
                        if self.SE == None:
                            self.SE = BHTree(southeast)
                        self.SE.insert(c)
                    else:
                        southwest = self.quadrant.SW()
                        if c.is_in(southwest):
                            if self.SW == None:
                                self.SW = BHTree(southwest)
                            self.SW.insert(c)
            self.insert(b)

    def update_force(self, b):
        # To deal with divisions by zero
        if self.body.distance_to(b) == 0:
            distance = self.body.distance_to(b) + 1e-99
        else:
            distance = self.body.distance_to(b)

        if is_external(self):
            if (self.body != b):
                b.add_force(self.body)
        elif self.quadrant.length / (distance) < 0.5:
            b.add_force(self.body)
        else:
            if (self.NW != None):
                self.NW.update_force(b)
            if (self.SW != None):
                self.SW.update_force(b)
            if (self.SE != None):
                self.SE.update_force(b)
            if self.SW != None:
                self.SW.update_force(b)
