from clothingcolor import ClothingColor

"""
Class: Clothing
Methods: __init__, set
Description:
This is a simple object which stores relevant data related to clothing.
This object can be expanded by inheritance to allow for multiple different
objects that represent different kinds of clothing.
"""
class Clothing():
	# The attributes can be set upon declaration. If ignored, they use default values
	def __init__(self, **kwargs):
		if 'image' in kwargs:
			self.image = kwargs['image']
		else:
			self.image = ""
		
		if 'link' in kwargs:
			self.link = kwargs['link']
		else:
			self.link = ""
		
		if 'price' in kwargs:
			self.price = kwargs['price']
		else:
			self.price = -1
		
		if self.image != "":
			self.color = ClothingColor(self.image).GetColor()
	
	# Used to re-initialize a clothing object if necessary
	def setAttributes(self, **kwargs):
		self.__init__(**kwargs)
	
	
		
		
