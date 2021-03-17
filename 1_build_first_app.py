from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Kivy(App):
	def build(self):
		l1 = Label(
			text= "Hello World"
			)
		return l1

if __name__ == '__main__':
	Kivy().run()

