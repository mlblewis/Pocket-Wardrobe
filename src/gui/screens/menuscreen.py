import os
import pickle

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from gui.openpopup import OpenPopup
from clothing import Clothing

"""
Class: MenuScreen
Methods: __init__, GotoCamera, GotoWardrobe, SelectFile, LoadClothes
Description:
This is the main menu screen of Pocket Wardrobe. It is a kivy Screen type.
It contains several buttons which allow the user to access the functionality
of the rest of the application, in addition to other GUI elements.
Additional features can be added to Pocket Wardrobe in the form of other
classes, and they can be accessed through this screen when appropriate.
"""
class MenuScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.layout = FloatLayout()
		self.layout.orientation = 'vertical'
		self.add_widget(self.layout)

		self.logo = Image(
			source = 'gfx/PWLogo2.png',
			size_hint = (0.6, 0.6),
			pos_hint = {'x':0.2, 'y':0.5})
		self.layout.add_widget(self.logo)

		# A button that takes us to the camera screen
		self.buttonNewPic = Button(
			text='Take a New Photo',
			size_hint = (0.75, 0.1),
			pos_hint = {'x':0.125, 'y':0.5},
			font_size = 32,
			on_press = self.GotoCamera)
		self.layout.add_widget(self.buttonNewPic)
		
		# A button that takes us to the wardrobe screen
		self.buttonWardrobe = Button(
			text='View Wardrobe',
			size_hint = (0.75, 0.1),
			pos_hint = {'x':0.125, 'y':0.4},
			font_size = 32,
			on_press = self.GotoWardrobe)
		self.layout.add_widget(self.buttonWardrobe)
		
		# A button that opens a file
		self.openpop = OpenPopup(load = self.LoadClothes)
		self.buttonOpenPic = Button(
			text='Add Existing Photo',
			size_hint = (0.75, 0.1),
			pos_hint = {'x':0.125, 'y':0.3},
			font_size = 32,
			on_press = self.SelectFile)
		self.layout.add_widget(self.buttonOpenPic)
		
	# Button event handler. Takes the user to the Camera screen
	def GotoCamera(self, event):
		self.manager.transition.direction = 'left'
		self.manager.transition.duration = 0.25
		self.manager.current = 'camScreen'
	
	# Button event handler. Takes the user to the Wardrobe screen
	def GotoWardrobe(self, event):
		self.manager.transition.direction = 'left'
		self.manager.transition.duration = 0.25
		self.manager.current = 'wardrobeScreen'
	
	# Simple event handler for the 'add existing photo' button. Opens a file browser
	def SelectFile(self, event):
		self.openpop.open()
	
	# Grab the current selected file from the file browser and save it to the wardrobe
	def LoadClothes(self, event):
		fileName = self.openpop.GetSelection()
		self.openpop.dismiss()
		
		# Determines if we should create wardrobe.dat, or append it if it exists
		if os.path.isfile('wardrobe.dat'):
			access = 'ab'
		else:
			access = 'wb'
		
		# Put the filepath to the image in a Clothing object and save it to the wardrobe
		with open('wardrobe.dat', access) as out:
			cloth = Clothing(image = fileName)
			pickle.dump(cloth, out, 0)
		del cloth
		
