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
    def __init__(self, color, form, layer, graphic):
        self.color = color
        self.form = form
        self.layer = layer
        self.graphic = graphic
        self.tops = []
    """
    Method: __str__
        Creates a string representation of the class object
    Takes: self
    Returns: String
    """
    def __str__(self):
        return "Color: %s, Style: %s, Layer: %s, Grahpic: %b " % (self.color, self.form, self.layer, self.graphic)
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
    """
    Method: setColor
        sets the color for the top
    Takes: tuple(color)
    Returns: n/a
        """
    def setColor(color):
        self.color = color
    """
    Method: setForm
        sets the type of top
    Takes: string(form)
    Returns: n/a
    """
    def setForm(form):
        self.form = form
    """
    Method: setLayer
        sets the layer of the top
    Takes: string(layer)
    Returns: n/a
    """
    def setLayer(layer):
        self.layer = layer
    """
    Method: setGraphic
        states wether or not the top has a graphic of some sort
    Takes: bool(graphic)
    Returns: n/a
    """        
    def setGraphic(graphic):
        self.graphic = graphic
    """
    Method: getColor
    Takes: self
    Returns: tuple(color)
    """
    def getColor(self):
        return self.color
    """
    Method: getForm
    Takes: self
    Returns: string(form)
    """
    def getForm(self):
        return self.form
    """
    Method: getLayer
    Takes: self
    Returns: string(layer)
    """
    def getLayer(self):
        return self.layer
    """
    Method: getGraphic
    Takes: self
    Returns: bool(graphic)
    """
    def getGraphic(self):
        return self.graphic
