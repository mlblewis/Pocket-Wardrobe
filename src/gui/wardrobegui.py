import os
import pickle

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from gui.clothingimage import ClothingImage
from kivy.core.window import Window
from kivy.app import App

"""
Class: WardrobeGUI
Methods: __init__, UpdateWidgets, LoadWardrobeFile
Description:
This object inherits from kivy's ScrollView type. It is pre-loaded with several
GUI elements and file loading logic which allow it to fill the user's screen
with the contents of their wardrobe. The user can scroll up and down.
This object can be used anytime the user's wardrobe needs to be displayed.
Further functionality and GUI elements can easily be added to it by
simply expanding this class.
"""
class WardrobeGUI(ScrollView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.size_hint = (1, 1)
		self.size = (Window.width, Window.height)
		#self.filename = 'wardrobe.dat'
		
		self.layout = GridLayout(
		cols = 2,
		size_hint_y = None)
		self.layout.bind(minimum_height = self.layout.setter('height'))
		
		self.add_widget(self.layout)
		self.UpdateWidgets()
	
	# Clears the widgets from the layout and re-loads them from the wardrobe
	def UpdateWidgets(self):
		self.layout.clear_widgets()
		
		wardrobe = App.get_running_app().wardrobe.clothes
		for name, cloth in wardrobe.items():
			self.layout.add_widget(ClothingImage(clothing = cloth))
