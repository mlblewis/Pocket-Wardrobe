import Clothing
class Shirt(Top):
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
    def __str__(self):
        return "Brand: %s, Size: %s, Price: %s " % (self.brand, self.size, self.price)
    def setBrand(self, brand):
        self.brand = brand
    def setSize(self, size):
        self.size = size 
    def setPrice(self, price):
        self.price = price 
    def getBrand(self):
        return self.brand
    def getSize(self):
        return self.size
    def getPrice(self):
        return self.price 
