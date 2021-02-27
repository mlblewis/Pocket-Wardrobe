"""
Class: Jacket
Methods: __init__, __str__, setBrand, setSize, setPrice, setMaterial, getBrand
    getSize, getPrice, getMaterial
Atributes: 
    brand(string) maker of said jacket
    size(string) size of jacket
    price(float) price of jacket
    material(string) material of jacket
"""
class Jacket(Top):
"""
Method: __init__
    Creates Jacket object
Takes: brand(string), size(string), price(float), material(String)
Returns: n/a
"""
    def __init__(self, brand, size, price, material):
        self.brand = brand
        self.size = size
        self.price = price
        self.material = material
"""
Method: __str__
    Creates a string representation of the jacket object
Takes: Self
Returns: String
"""
    def __str__(self):
        return "Brand: %s, Size: %s, Price: %s, Material: %s" \
            % (self.brand, self.size, self.price, self.material)
"""
Method: setBrand
    sets brand attribute of jacket
Takes: self, brand
Returns: n/a
"""
    def setBrand(self, brand):
        self.brand = brand
"""
Method: setSize
    Sets size attribute of Jacket
Takes: self, size
Returns: n/a
"""
    def setSize(self, size):
        self.size = size
"""
Method: setPrice
    Sets price attribute of Jacket
Takes: self, price
Returns: n/a
""" 
    def setPrice(self, price):
        self.price = price 
"""
Method: setMaterial
    Sets Material attribute of Jacket
Takes: Self, material
Returns: n/a
"""
    def setMaterial(self, material):
        self.material = material
"""
Method: getBrand
    Returns value of brand in Jacket
Takes: self
Returns: brand
"""
    def getBrand(self):
        return self.brand
"""
Method: getSize
    Returns size attribute of Jacket
Takes: self
Returns: size
"""
    def getSize(self):
        return self.size
"""
Method: getPrice
    Returns price attribute of Jacket
Takes: self
Returns: price
"""
    def getPrice(self):
        return self.price
"""
Method: getMaterial
    Returns material attribute of Jacket
Takes: self
Returns: material
"""
    def getMaterial(self):
        return self.material
