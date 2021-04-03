import os

from gui.screens.menuscreen import MenuScreen
from gui.screens.camerascreen import CameraScreen
from gui.screens.wardrobescreen import WardrobeScreen
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

"""
Class: PocketWardrobe
Methods: build
Description:
This is the main app class for Pocket Wardrobe. It inherits from kivy's
App type. It returns a screen manager containing all of the app's menus.
"""
class PocketWardrobe(App):
	def build(self):
		App.title = ('Pocket Wardrobe')
		
		# Set the window's background to white
		Window.clearcolor = (1, 1, 1, 1)
		
		# A vertical resolution to approximate a phone screen
		Window.size = (540, 1080)
		
		# Add all of the screens into a screen manager
		menuMan = ScreenManager()
		menuMan.add_widget(MenuScreen(name = 'mainMenu'))
		menuMan.add_widget(CameraScreen(name = 'camScreen'))
		menuMan.add_widget(WardrobeScreen(name = 'wardrobeScreen'))
		
		return menuMan
