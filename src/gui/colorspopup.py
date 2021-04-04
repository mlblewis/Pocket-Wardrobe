from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

"""
Class: ColorsPopup
Methods: __init__, Cancel
Description:
This object inherits from kivy's Popup type. It contains GUI elements which
display the color palette being used by Pocket Wardrobe as a list of buttons.
The user can use this popup to select a color. Mainly used for the
ClothingPopup class in order to modify the color data for a Clothing object.
"""
class ColorsPopup(Popup):
	def __init__(self, **kwargs):
		super().__init__()
		
		self.title = 'Select Color'
		self.size_hint = (0.9, 0.7)
		
		self.selectionLayout = BoxLayout(orientation = 'vertical')
		
		# The color palette used by Pocket Wardrobe
		palette = [
		'aqua',
		'black',
		'blue',
		'fuchsia',
		'green',
		'gray',
		'lime',
		'maroon',
		'navy',
		'olive',
		'purple',
		'red',
		'silver',
		'teal',
		'white',
		'yellow']
		
		# Generate the buttons for this popup based on the palette
		for color in palette:
			self.selectionLayout.add_widget(Button(text = color, on_press = kwargs['press'], font_size = 20))
		
		self.selectionLayout.add_widget(Button(text = 'Cancel', on_press = self.Cancel, font_size = 20, bold = True))
		
		self.add_widget(self.selectionLayout)
	
	# Dismiss this popup
	def Cancel(self, event):
		self.dismiss()
	
	
