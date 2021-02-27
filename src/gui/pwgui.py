# This is all of the GUI-related code for Pocket Wardrobe.

import time
import os

from resources.Wardrobe import Wardrobe
from resources.Clothing import Clothing
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

# The main menu class for the GUi
class MainMenu(Screen):
	pass

# The menu where photos are taken
class PhotoMenu(Screen):
	def __init__(self, **kwargs):
		super(PhotoMenu, self).__init__()
		self.wardrobe = Wardrobe()
	
	# This method captures a photo from the camera widget defined in pwgui.kv
	# It saves the photo with a timestamp for a name.
	# The file path of the photo will be stored as a Clothing object
	# inside a Wardrobe object.
	def capture(self):
		camera = self.ids['camera']
		fileName = "IMG_{}.png".format(time.strftime("%Y%m%d_%H%M%S"))
		camera.export_to_png(fileName)
		self.wardrobe.add(os.path.dirname(__file__) + '/' + fileName)

class MenuMan(ScreenManager):
	def __init__(self):
		super(MenuMan, self).__init__()


# The main app class
class pwguiApp(App):
	def build(self):
		App.title = ('Pocket Wardrobe')  # Sets the window title
		return MenuMan()

