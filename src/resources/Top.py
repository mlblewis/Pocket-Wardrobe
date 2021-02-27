    """
    Class: Top
    Methods: __init__, setColor, setForm, setLayer, setGraphic, getColor, getForm,
    getLayer, getGraphic
    Atributes:
        tuple(color) rgba infor for image
        string(form) type of shirt i.g. short sleeve, long sleeve, sleeveless etc.
        string(layer) outer,under, etc
        bool(graphic) does it have a picture(or words) or not essentialy
    """
class Top(Clothing):
    """
    Method: __init__
        Creates the top object, as the name would suggest
    Takes:
        tuple(color) rgba infor for image
        string(form) type of shirt i.g. short sleeve, long sleeve, sleeveless etc.
        string(layer) outer,under, etc
        bool(graphic) does it have a picture(or words) or not essentialy
    Returns: a top object
    """
    def __init__(self):
        self.tops = []
    """
    Method: __str__
        Creates a string representation of the class object
    Takes: self
    Returns: String
    """
    def __str__(self):
        pass
    """
    Method: addTop
        adds an object to tops
    Takes: self, top(object)
    Returns: n/a
    """
    def addTop(self, top):
        self.tops.append(top)
    """
    Method: removeTop
        removes an object from tops
    Takes: self, top(object)
    Returns: n/a"""
    def removeTop(self, top):
        for x in range(len(self.tops))
            if tops[x] = top 
                tops.remove(x)