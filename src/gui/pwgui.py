# This is all of the GUI-related code for Pocket Wardrobe.

import time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen

# The main menu class for the GUi
class MainMenu(Screen):
	pass

# The menu where photos are taken
class PhotoMenu(Screen):
	
	# This method captures a photo from the camera widget defined in pwgui.kv
	# It saves the photo with a timestamp for a name
	def capture(self):
		camera = self.ids['camera']
		timestr = time.strftime("%Y%m%d_%H%M%S")
		camera.export_to_png("IMG_{}.png".format(timestr))

# Load our pwgui.kv file to run its code
GuiKV = Builder.load_file("pwgui.kv")

# The main app class
class pwguiApp(App):
	def build(self):
		App.title = ('Pocket Wardrobe')  # Sets the window title
		return GuiKV

