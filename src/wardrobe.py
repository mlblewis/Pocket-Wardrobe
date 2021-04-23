import os
import pickle

"""
Class: Wardrobe
Methods: __init__, SaveClothing, GetClothing, DeleteClothing
Description:
This is a wardrobe object. It handles loading and saving of Clothing objects to files.
It also contains a dictionary of clothing objects currently saved.
When the app is opened, a new Wardrobe is created. It loads the default wardrobe path.
Any clothes saved within that path are loaded, and can be managed in the app.
When a different wardrobe is loaded, the default one is closed.
Then, the Wardrobe object will load all the clothing objects from the directory of the
desired wardrobe into its list. Now you can manage that wardrobe and its contents.
"""
class Wardrobe():
	def __init__(self, **kwargs):
		
		if 'name' in kwargs:
			self.name = kwargs['name']
		else:
			self.name = 'default'
		
		self.clothes = {}
		
		self.directory = os.path.join('Wardrobes', ('wardrobe_' + self.name))
		
		if not os.path.isdir('Wardrobes'):
			os.mkdir('Wardrobes')
		
		if not os.path.isdir(self.directory):
			os.mkdir(self.directory)
		
		self.GetClothing()
	
	# Save a clothing object to the wardrobe. Appends the clothes list and creates the file.
	# If a clothing object already exists, it is deleted first, and then the new one is saved.
	def SaveClothing(self, clothing):
		self.DeleteClothing(clothing)
		fileName = clothing.image.replace('.png', '.dat')
		self.clothes[fileName] = clothing
		
		with open(os.path.join(self.directory, fileName), 'wb') as out:
			pickle.dump(clothing, out, 0)
	
	# Load all clothing within the Wardrobe object's directory name
	def GetClothing(self):
		self.clothes = {}
		for fileName in os.listdir(self.directory):
			with open(os.path.join(self.directory, fileName), "rb") as f:
				self.clothes[fileName] = pickle.load(f)
	
	# Remove an article of clothing from the wardrobe
	def DeleteClothing(self, clothing):
		fileName = clothing.image.replace('.png', '.dat')
		
		if fileName in self.clothes:
			self.clothes.pop(fileName)
		
		if fileName in os.listdir(self.directory):
			os.remove(os.path.join(self.directory, fileName))
