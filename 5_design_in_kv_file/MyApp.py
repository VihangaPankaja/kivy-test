from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from time import sleep
from threading import Thread

class grid(Widget):
	
	text1 = ObjectProperty(None)
	text2 = ObjectProperty(None)

	def press(self):
		text1 = self.text1.text
		text2 = self.text2.text

		self.text1.text = ''
		self.text2.text = ''

		self.lbl1.text = f'{text1} {text2}'

		self.btn.background_color = (0,0,0,1)
		self.btn.color = (1,1,1,1)

	def release(self):
		def f1():
			self.btn.background_color = (136/255, 176/255, 75/255, 1)
			self.btn.color = (1,0,0,1)

		def f2():
			sleep(2)
			self.lbl1.text = ''

		Thread(target=f1).start()
		Thread(target=f2).start()


class Myapp(App):
	def build(self):
		Window.size = (1200, 600)
		return grid()

if __name__ == '__main__':
	Myapp().run()