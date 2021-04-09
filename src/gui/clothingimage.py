from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
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
		self.size_hint = (None, None)
		self.height = (Window.height / 4)
		self.width = (Window.height / 4)
		self.orientation = 'vertical'
		self.on_press = self.ShowAttributes
		
		with self.canvas:
			Color(0.9, 0.84, 0.25)
			
			self.rect = Rectangle()
			self.bind(pos = self.UpdateBackground, size = self.UpdateBackground)
		
		if 'clothing' in kwargs:
			self.clothing = kwargs['clothing']
			self.image = Image(source = self.clothing.image)
			self.add_widget(self.image)
		else:
			self.error = Label(text = 'Error loading clothing')
			self.add_widget(self.error)
		
		self.label = Label(text = 'test', size_hint = (None, 0.2), color = (0, 0, 0))
		self.label.font_size = self.label.height / 2
		self.add_widget(self.label)
	
	def ShowAttributes(self):
		self.attrPopup = ClothingPopup(clothing = self.clothing)
		self.attrPopup.open()
		
	def UpdateBackground(self, *args):
		self.rect.pos = self.pos
		self.rect.size = (self.width, self.height)
		
