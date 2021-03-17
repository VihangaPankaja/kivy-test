from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from time import sleep
from threading import Thread

class grid(Widget):
	
	text1 = ObjectProperty(None)
	text2 = ObjectProperty(None)
	wait = ObjectProperty(None)

	def press(self):
		global wait
		text1 = self.text1.text
		text2 = self.text2.text
		wait = float(self.wait.text)

		self.text1.text = ''
		self.text2.text = ''

		self.lbl1.text = f'text1:{text1} and text2:{text2}'

		self.btn.background_color = get_color_from_hex('#00A170')
		self.btn.color = (1,1,1,1)

	def release(self):
		global wait
		def f1():
			self.btn.background_color = get_color_from_hex('#88b04b')
			self.btn.color = (1,0,0,1)

		def f2():
			global wait
			sleep(wait)
			self.lbl1.text = ''

		Thread(target=f1).start()
		Thread(target=f2).start()


class Myapp(App):
	def build(self):
		Window.size = (1200, 600)
		Builder.load_file('design.kv')
		# or use Builder.load_string('''   ''') method
		return grid()

if __name__ == '__main__':
	Myapp().run()