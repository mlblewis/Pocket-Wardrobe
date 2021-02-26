import Clothing
class Shirt(Clothing):
    __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
    __str__(self):
        return "Brand: %s, Size: %s, Price: %s " % (self.brand, self.size, self.price)
    setBrand(self, brand):
        self.brand = brand
    setSize(self, size):
        self.size = size 
    setPrice(self, price):
        self.price = price 
    getBrand(self):
        return self.brand
    getSize(self):
        return self.size
    getPrice(self):
        return self.price 