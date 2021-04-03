from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from gui.wardrobegui import WardrobeGUI

"""
Class: WardrobeScreen
Methods: __init__, GotoMenu, UpdateWardrobe
Description:
This is a kivy Screen type object. It contains a few of its own GUI elements
in addition to a WardrobeGUI object. The user can browse the contents
of their wardrobe in this screen.
"""
class WardrobeScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		# Update the wardrobe when the user enters the screen
		self.on_enter = self.UpdateWardrobe
		
		self.layout = BoxLayout(orientation = 'vertical')
		
		self.wardrobeList = WardrobeGUI()
		self.layout.add_widget(self.wardrobeList)
		
		self.menuButton = Button(
			size_hint_y = 0.15,
			text = 'Back to Menu',
			on_press = self.GotoMenu)
		self.layout.add_widget(self.menuButton)
		
		self.add_widget(self.layout)
	
	# Button event handler. Takes the user back to the main menu
	def GotoMenu(self, event):
		self.manager.transition.direction = 'right'
		self.manager.transition.duration = 0.25
		self.manager.current = 'mainMenu'
	
	# Tells the WardrobeGUI object to re-load the wardrobe
	def UpdateWardrobe(self):
		self.wardrobeList.UpdateWidgets()
	
	
