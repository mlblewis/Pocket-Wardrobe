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
class Jacket(Clothing):
"""
Method: __init__
    Creates Jacket object
Takes: brand(string), size(string), price(float), material(String)
Returns: n/a
"""
    __init__(self, brand, size, price, material):
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
    __str__(self):
        return "Brand: %s, Size: %s, Price: %s, Material: %s" \
            % (self.brand, self.size, self.price, self.material)
"""
Method: setBrand
    sets brand attribute of jacket
Takes: self, brand
Returns: n/a
"""
    setBrand(self, brand):
        self.brand = brand
"""
Method: setSize
    Sets size attribute of Jacket
Takes: self, size
Returns: n/a
"""
    setSize(self, size):
        self.size = size
"""
Method: setPrice
    Sets price attribute of Jacket
Takes: self, price
Returns: n/a
""" 
    setPrice(self, price):
        self.price = price 
"""
Method: setMaterial
    Sets Material attribute of Jacket
Takes: Self, material
Returns: n/a
"""
    setMaterial(self, material):
        self.material = material
"""
Method: getBrand
    Returns value of brand in Jacket
Takes: self
Returns: brand
"""
    getBrand(self):
        return self.brand
"""
Method: getSize
    Returns size attribute of Jacket
Takes: self
Returns: size
"""
    getSize(self):
        return self.size
"""
Method: getPrice
    Returns price attribute of Jacket
Takes: self
Returns: price
"""
    getPrice(self):
        return self.price
"""
Method: getMaterial
    Returns material attribute of Jacket
Takes: self
Returns: material
"""
    getMaterial(self):
        return self.material