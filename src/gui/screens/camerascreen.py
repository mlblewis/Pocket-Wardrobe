import time
import os
import pickle

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.app import App
from clothing import Clothing


"""
Class: CameraScreen
Methods: __init__, GotoMenu, TakePic
Description:
This is a kivy Screen type object which contains the GUI elements and logic
necessary to load the user's camera and allow them to take photographs.
Photos are saved as Clothing objects to the wardrobe file for later viewing.
"""
class CameraScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.layout = BoxLayout(orientation = 'vertical')
		self.add_widget(self.layout)

		self.camera = Camera(play = True)
		self.layout.add_widget(self.camera)

		self.buttonTake = Button(
			text = 'Take Photo',
			on_press = self.TakePic,
			size_hint_y = 0.15)
		self.layout.add_widget(self.buttonTake)

		self.buttonCancel = Button(
			text = 'Cancel',
			on_press = self.GotoMenu,
			size_hint_y = 0.15)
		self.layout.add_widget(self.buttonCancel)

	# An event handler for the 'cancel' button. Takes us to the main menu
	def GotoMenu(self, event):
		self.manager.transition.direction = 'right'
		self.manager.transition.duration = 0.25
		self.manager.current = 'mainMenu'
	
	# Take a new photo from device's camera. Save into wardrobe as Clothing object
	def TakePic(self, event):
		fileName = "IMG_{}.png".format(time.strftime("%Y%m%d_%H%M%S"))
		self.camera.export_to_png(fileName)
		cloth = Clothing(image = fileName)
		App.get_running_app().wardrobe.SaveClothing(cloth)
		self.GotoMenu(event)
