from PIL import Image
from colorthief import ColorThief
import webcolors
from scipy.spatial import KDTree

"""
Class: ClothingColor
Methods: __init__, MakeThumb, DominantColor, GetColor
Description:
This is a simple class that allows its user to get the dominant color
of an image. It can return an RGB value, or convert that into the name
of the nearest color in the HTML4 color palette.
The dominant color is found after shrinking the image to a small thumbnail.
This is done because it significantly increases performance.
New thumbnails will overwrite old ones, meaning no further storage will be used.
Each method can be called and used on its own. They build off one another,
so when calling one method, other methods may be called when necessary.
"""
class ClothingColor():
	def __init__(self, path):
		self.imgPath = path
	
	# Make the image into a thumbnail. Much faster to work with
	def MakeThumb(self):
		image = Image.open(self.imgPath)
		image.thumbnail((150, 150))
		
		if image.format == 'PNG':
			self.imgPath = 'thm/imgSmall.png'
			image.save(self.imgPath)
		else:
			self.imgPath = 'thm/imgSmall.jpg'
			image.save(self.imgPath, 'JPEG', quality = 100)
		return self.imgPath
	
	# Get the dominant color of the image after making it into a thumbnail
	def DominantColor(self):
		self.MakeThumb()
		domColor = ColorThief(self.imgPath).get_color(quality = 1)
		return domColor
	
	# Get the nearest color within the HTML4 color palette and return its name
	def GetColor(self):
		domColor = self.DominantColor()
		palette = webcolors.HTML4_NAMES_TO_HEX
		colNames = []
		colRGB = []

		for name, hexVal in palette.items():
			colNames.append(name)
			colRGB.append(webcolors.hex_to_rgb(hexVal))

		tree = KDTree(colRGB) # We use a k-d tree to find the closest match

		dist, index = tree.query(domColor)
		return colNames[index]
