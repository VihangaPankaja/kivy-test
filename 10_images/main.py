from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

class mywidget(Widget):
	pass

class myapp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		Builder.load_file('design.kv')
		return mywidget()

if __name__ == '__main__':
	myapp().run()