import Clothing
"""
Class: Bottom
Methods: __init__, addBottom, removeBottom
Attributes:
    bottoms(List)
"""
class Bottom(Clothing):
    """
    Method: __init__
        creates the Bottom object
    Takes: self
    Returns: a Bottom object
    """
    __init__(self):
        bottoms = []
    """
    Method: addBottom
        Adds a bottom to the bottoms list
    Takes: self, rhs
    Returns: n/a
    """
    addBottom(self, rhs):
        bottoms.append(rhs)
    """
    Method: removeBottom
        removes an object from the bottoms list
    Takes: self, rhs
    Returns: n/a
    """
    removeBottom(self, rhs):
        for x in range(len(self.bottoms))
            if bottoms[x] = rhs 
                bottoms.remove(x)        