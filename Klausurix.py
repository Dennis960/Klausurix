from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivymd.app import MDApp
# from kivy.app import runTouchApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast



#==================================================================================
#==================================================================================
# Klasse für das Hauptfenster.
# konkrete Implementation fuer die Klasse wird aus der kv-Datei genommen
class Display(BoxLayout):
    pass

#==================================================================================
#==================================================================================
# Klasse fuer den Tab 1.
# konkrete Implementation fuer die Klasse wird aus der kv-Datei genommen
class Tab_One(Screen):
    pass

#==================================================================================
#==================================================================================
# Klasse fuer den Tab 2.
# konkrete Implementation fuer die Klasse wird aus der kv-Datei genommen
class Tab_Two(Screen):
    pass


#========================================================
class KlausurixApp(MDApp):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Window.bind(on_keyboard=self.events)
		self.manager_open = False
		self.file_manager = MDFileManager()
		self.file_manager.exit_manager=self.exit_manager
		self.file_manager.select_path=self.select_path
		self.file_manager.previous=True
		#self.file_manager = MDFileManager(
		#	exit_manager=self.exit_manager,
		#	select_path=self.select_path,
		#	previous=True,
		#)

	#----------------------------------------------------
	def build(self):
		Builder.load_file('Klausurix_UI_Elements.kv')
		return Display()

	#----------------------------------------------------
	def file_manager_open(self):
		self.file_manager.show('/')  # output manager to the screen
		self.manager_open = True

	#----------------------------------------------------
	def select_path(self, path):
		'''It will be called when you click on the file name
		or the catalog selection button.
		:type path: str;
		:param path: path to the selected directory or file;
		'''
		self.exit_manager()
		toast(path)

	#----------------------------------------------------
	def exit_manager(self, *args):
		'''Called when the user reaches the root of the directory tree.'''
		self.manager_open = False
		self.file_manager.close()

	#----------------------------------------------------
	def events(self, instance, keyboard, keycode, text, modifiers):
		'''Called when buttons are pressed on the mobile device.'''
		if keyboard in (1001, 27):
			if self.manager_open:
				self.file_manager.back()
		return True



	
#========================================================

if __name__ == '__main__':
    KlausurixApp().run()