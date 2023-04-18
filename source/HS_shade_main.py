from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 

import HS_shade_first as HS

HS.HS_shade_first().run()

class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file('HS_shade_second.kv')


class AwesomeApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	AwesomeApp().run()