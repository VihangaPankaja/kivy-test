from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class box(Widget):
	pass


class app(App):
	def build(self):
		Builder.load_file('design.kv')
		return box()

if __name__ == '__main__':
	app().run()