from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from clothing import Clothing
from gui.clothingpopup import ClothingPopup

"""
Class: ClothingImage
Methods: __init__, ShowAttributes
Description:
This object inherits from kivy's BoxLayout type. It is pre-loaded with several
GUI elements related to displaying Clothing type objects on the screen.
In other words, we can visualize Clothing objects in the app's GUI with this.
Clicking on a ClothingImage object will show the attributes of its 
stored Clothing object using a ClothingPopup object.
Further functionality or GUI elements can easily be added by adding them to this class.
"""
class ClothingImage(ButtonBehavior, BoxLayout):
	def __init__(self, **kwargs):
		super().__init__()
		self.size_hint_y = None
		self.height = (Window.height / 7)
		self.orientation = 'vertical'
		self.on_press = self.ShowAttributes
		
		if 'clothing' in kwargs:
			self.clothing = kwargs['clothing']
			self.image = Image(source = self.clothing.image)
			self.add_widget(self.image)
		else:
			self.error = Label(text = 'Error loading image')
			self.add_widget(self.error)
	
	def ShowAttributes(self):
		self.attrPopup = ClothingPopup(clothing = self.clothing)
		self.attrPopup.open()
		
		
