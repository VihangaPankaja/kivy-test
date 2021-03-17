from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class mywidget(Widget):
	pass

class myapp(App):
	def build(self):
		Builder.load_file('design.kv')
		return mywidget()

if __name__ == '__main__':
	myapp().run()