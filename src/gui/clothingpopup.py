from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from gui.colorspopup import ColorsPopup
from clothing import Clothing

"""
Class: ClothingPopup
Methods: __init__, ConfirmDelete, DeleteClothing, ReturnColor, SelectColor, SaveClothing, UpdateFormality, UpdateGender
Description:
This object inherits from kivy's Popup type. It contains GUI elements which
display the attributes of a Clothing object. It can use a ColorsPopup
object to edit the stored color of a Clothing object.
This popup handles saving/deleting of clothing objects to the wardrobe.
This popup can be used to add new clothing to the wardrobe, and it can also be used
to edit existing clothing. By default, it uses its editing layout, which should
work fine for most use-cases.
"""
class ClothingPopup(Popup):
	def __init__(self, **kwargs):
		super().__init__()
		
		self.size_hint = (0.9, 0.8)
		
		self.layout = BoxLayout(orientation = 'vertical')
		self.add_widget(self.layout)
		
		if 'edit' in kwargs:
			self.isEditing = kwargs['edit']
		else:
			self.isEditing = True
		
		if 'clothing' in kwargs:
			self.clothing = kwargs['clothing']
		else:
			self.clothing = Clothing()
		
		self.title = self.clothing.image
		
		self.clothImg = Image(source = self.clothing.image)
		self.layout.add_widget(self.clothImg)
		
		self.colorSelection = ColorsPopup(press = self.ReturnColor)
		
		self.btnLayout = GridLayout(
		cols = 2,
		size_hint_y = 0.6)
		self.layout.add_widget(self.btnLayout)
		
		self.clrLabel = Label(
			text = 'Color:',
			font_size = 20,
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.clrLabel)
		
		self.clrButton = Button(
			on_press = self.SelectColor,
			font_size = 20,
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.clrButton)
		
		self.formalButton = ToggleButton(
			text = 'Formal',
			on_press = self.UpdateFormality,
			font_size = 20,
			group = 'isFormal',
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.formalButton)
		
		self.casualButton = ToggleButton(
			text = 'Casual',
			on_press = self.UpdateFormality,
			font_size = 20,
			group = 'isFormal',
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.casualButton)
		
		self.mensButton = ToggleButton(
			text = 'Men\'s',
			on_press = self.UpdateGender,
			font_size = 20,
			group = 'gender',
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.mensButton)
		
		self.womensButton = ToggleButton(
			text = 'Women\'s',
			on_press = self.UpdateGender,
			font_size = 20,
			group = 'gender',
			size_hint_y = 0.4)
		self.btnLayout.add_widget(self.womensButton)
		
		self.svcanLayout = BoxLayout(
			size_hint_y = 0.6,
			orientation = 'vertical')
		self.layout.add_widget(self.svcanLayout)
		
		self.saveButton = Button(
			text = 'Save to Wardrobe',
			on_press = self.SaveClothing,
			font_size = 20,
			size_hint_y = 0.2)
		self.svcanLayout.add_widget(self.saveButton)
		
		if self.isEditing == True:
			self.delButton = Button(
				text = 'Delete',
				on_press = self.ConfirmDelete,
				font_size = 20,
				size_hint_y = 0.2)
			self.svcanLayout.add_widget(self.delButton)
		
		self.cancelButton = Button(
			text = 'Cancel',
			on_press = self.dismiss,
			font_size = 20,
			size_hint_y = 0.2)
		self.svcanLayout.add_widget(self.cancelButton)
		
		self.LoadClothing(self.clothing)
	
	
	# Load a clothing object into this popup, updating its GUI elements
	def LoadClothing(self, cloth):
		self.clothing = cloth
		self.title = self.clothing.image
		self.clothImg.source = self.clothing.image
		self.clrButton.text = self.clothing.color
		
		if self.clothing.isFormal == True:
			self.formalButton.state = 'down'
			self.casualButton.state = 'normal'
		else:
			self.formalButton.state = 'normal'
			self.casualButton.state = 'down'
		
		if self.clothing.gender == 'womens':
			self.womensButton.state = 'down'
			self.mensButton.state = 'normal'
		elif self.clothing.gender == 'mens':
			self.womensButton.state = 'normal'
			self.mensButton.state = 'down'
		else:
			self.womensButton.state = 'normal'
			self.mensButton.state = 'normal'
	
	# Passed through to the ColorsPopup object. Updates the Clothing color
	def ReturnColor(self, event):
		self.clrButton.text = event.text
		self.clothing.color = event.text
		self.colorSelection.dismiss()
	
	# Show the ColorsPopup object
	def SelectColor(self, event):
		self.colorSelection.open()
	
	# Save the clothing object to the wardrobe
	def SaveClothing(self, event):
		App.get_running_app().wardrobe.SaveClothing(self.clothing)
		self.dismiss()
	
	# Prompt the user to confirm the deletion
	def ConfirmDelete(self, event):
		self.conPopup = Popup(size_hint = (0.8, 0.2), title = 'Are you sure?')
		conLayout = BoxLayout(orientation = 'horizontal')
		conLayout.add_widget(
			Button(
				on_press = self.conPopup.dismiss,
				text = 'Nevermind',
				font_size = 20))
		conLayout.add_widget(
			Button(
				on_press = self.DeleteClothing,
				text = 'Yes, delete it',
				font_size = 20))
		self.conPopup.add_widget(conLayout)
		self.conPopup.open()
		
	# Delete the clothing from the wardrobe
	def DeleteClothing(self, event):
		App.get_running_app().wardrobe.DeleteClothing(self.clothing)
		self.conPopup.dismiss()
		self.dismiss()
	
	# Update the formality status of the clothing object based on which button is pressed
	def UpdateFormality(self, event):
		if self.casualButton.state == 'down':
			self.clothing.isFormal = False
		else:
			self.clothing.isFormal = True
	
	# Update the formality status of the clothing object based on which button is pressed
	def UpdateGender(self, event):
		if self.womensButton.state == 'down':
			self.clothing.gender = 'womens'
		elif self.mensButton.state == 'down':
			self.clothing.gender = 'mens'
		else:
			self.clothing.gender = 'neutral'
