from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from clothing import Clothing
from gui.colorspopup import ColorsPopup

"""
Class: ClothingPopup
Methods: __init__, Cancel, SaveChanges, ReturnColor, SelectColor
Description:
This object inherits from kivy's Popup type. It contains GUI elements which
display the attributes of a Clothing object. It can use a ColorsPopup
object to edit the stored color of a Clothing object.
It is planned for all attributes to be modifiable and be able to save
those changes to the wardrobe.dat file.
"""
class ClothingPopup(Popup):
	def __init__(self, **kwargs):
		super().__init__()
		
		if 'clothing' in kwargs:
			self.clothing = kwargs['clothing']
		else:
			self.dismiss()
		
		self.title = 'Clothing Attributes'
		self.size_hint = (0.9, 0.6)
		
		self.colorSelection = ColorsPopup(press = self.ReturnColor)
		
		self.layout = GridLayout(cols = 2)
		
		self.layout.add_widget(Label(text = 'Image:', font_size = 20))
		self.layout.add_widget(Label(text = self.clothing.image, font_size = 20))
		self.layout.add_widget(Label(text = 'Link to Store Page:', font_size = 20))
		self.layout.add_widget(Label(text = 'n/a', font_size = 20))
		
		self.labelColor = Label(text = 'Color', font_size = 20)
		self.buttonColor = Button(text = self.clothing.color, on_press = self.SelectColor, font_size = 20)
		self.layout.add_widget(self.labelColor)
		self.layout.add_widget(self.buttonColor)
		
		self.layout.add_widget(Button(
			text = 'Cancel',
			on_press = self.Cancel,
			font_size = 20,
			size_hint_y = 0.2))
		self.layout.add_widget(Button(
			text = 'Save Changes',
			on_press = self.SaveChanges,
			font_size = 20,
			size_hint_y = 0.2))
		
		self.add_widget(self.layout)
	
	# Dismiss this popup, discarding any changes
	def Cancel(self, event):
		self.dismiss()
	
	# Save our changes into the Clothing object
	def SaveChanges(self, event):
		self.clothing.color = self.buttonColor.text
		self.dismiss()
	
	# Passed through to the ColorsPopup object. Updates the Clothing color
	def ReturnColor(self, event):
		self.buttonColor.text = event.text
		self.colorSelection.dismiss()
	
	# Show the ColorsPopup object
	def SelectColor(self, event):
		self.colorSelection.open()


