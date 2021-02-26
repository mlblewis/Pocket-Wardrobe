import bottom
class Pants(bottom):
    __init__(self, color, form, layer, graphic, brand, size, price):
        self.color = color 
        self.form = form 
        self.layer = layer 
        self.graphic = graphic
        self.brand = brand 
        self.size = size 
        self.price = price 
    __str__(self):
        return """Color: %s, Form: %s, Layer %s, Graphic: %s, Brand: %s, Size %s,
         Price: %s""" % (self.color, self.form, self.layer, self.graphic, \
             self.brand, self.size, self.price)
    """
    Method: setColor
        sets the color for the top
    Takes: tuple(color)
    Returns: n/a
        """
    setColor(color):
        self.color = color
    """
    Method: setForm
        sets the type of top
    Takes: string(form)
    Returns: n/a
    """
    setForm(form):
        self.form = form
    """
    Method: setLayer
        sets the layer of the top
    Takes: string(layer)
    Returns: n/a
    """
    setLayer(layer):
        self.layer = layer
    """
    Method: setGraphic
        states wether or not the top has a graphic of some sort
    Takes: bool(graphic)
    Returns: n/a
    """        
    setGraphic(graphic):
        self.graphic = graphic   
    setBrand(self, brand):
        self.brand = brand
    setSize(self, size):
        self.size = size 
    setPrice(self, price):
        self.price = price
    """
    Method: getColor
    Takes: self
    Returns: tuple(color)
    """
    getColor(self):
        return self.color
    """
    Method: getForm
    Takes: self
    Returns: string(form)
    """
    getForm(self):
        return self.form
    """
    Method: getLayer
    Takes: self
    Returns: string(layer)
    """
    getLayer(self):
        return self.layer
    """
    Method: getGraphic
    Takes: self
    Returns: bool(graphic)
    """
    getGraphic(self):
        return self.graphic
    getBrand(self):
        return self.brand
    getSize(self):
        return self.size
    getPrice(self):
        return self.price