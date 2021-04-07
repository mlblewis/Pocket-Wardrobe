from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

"""
Class: OpenPopup
Methods: __init__, Cancel, GetSelection
Description:
This object inherits from kivy's Popup type. It is pre-loaded with several
GUI elements related to browsing for a file on the user's system and opening it.
This popup can be used anytime a file needs to be opened.
Additional functionality and GUI elements can easily be added to this class.
"""
class OpenPopup(Popup):
	def __init__(self, **kwargs):
		super().__init__()
		
		self.size_hint = (0.9, 0.9)
		self.title = 'Open an Image'
		
		self.layout = BoxLayout(orientation = 'vertical')
		self.add_widget(self.layout)
		
		self.buttonCancel = Button(
			text = 'Cancel',
			on_press = self.Cancel)
			
		# The 'load' button. Its event handler is provided in **kwargs by
		# the containing class.
		self.buttonLoad = Button(
			text = 'Load File',
			on_press = kwargs['load'])
		
		self.buttons = BoxLayout(size_hint_y = 0.1)
		self.buttons.add_widget(self.buttonCancel)
		self.buttons.add_widget(self.buttonLoad)
		
		self.fileBrowser = FileChooserIconView()
		self.layout.add_widget(self.fileBrowser)
		self.layout.add_widget(self.buttons)
		
		self.content = self.layout
	
	# A simple event that closes this popup
	def Cancel(self, event):
		self.dismiss()
	
	# A simple getter for the current selection in the file browser
	def GetSelection(self):
		# Grab the path of the selected file
		path = str(self.fileBrowser.selection)
		
		# Remove unecessary characters from file path string
		path = path.replace('[', '')
		path = path.replace(']', '')
		path = path.replace('\'', '')
		return path
