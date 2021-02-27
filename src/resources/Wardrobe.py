from resources.Clothing import Clothing

class Wardrobe():
	def __init__(self):
		self.clothing = []
		self.outfits = []

	def __str__(self):
		pass

	def add(self, fileName):
		newCloth = Clothing()
		newCloth.setImage(fileName)
		self.clothing.append(newCloth)

	def remove(self):
		pass
