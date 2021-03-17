from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from time import sleep
from threading import Thread

class grid(GridLayout):
	def __init__(self, **kwargs):
		super(grid, self).__init__(**kwargs)

		# create grid
		self.cols = 1

		#create sub grod
		self.top_grid = GridLayout()
		self.top_grid.cols = 2

		self.top_grid.add_widget(Label(text = "text field 1"))

		self.text1 = TextInput(multiline = False)
		self.top_grid.add_widget(self.text1)

		self.top_grid.add_widget(Label(text = "text field 2"))

		self.text2 = TextInput(multiline = False)
		self.top_grid.add_widget(self.text2)

		self.add_widget(self.top_grid)

		self.btn = Button(text = "play", 
                    size_hint = (2,1), 
                    background_normal = '',
                    background_color = (136/255, 176/255, 75/255, 1), 
                    color = (1,0,0,1), 
                    border = (0,0,0,0)
                    )
		self.btn.bind(on_press = self.press,
                on_release = self.release
                )
		self.add_widget(self.btn)

		self.lbl1 = Label(text = 'add')
		self.add_widget(self.lbl1)

	def press(self, instance):
		text1 = self.text1.text
		text2 = self.text2.text

		self.text1.text = ''
		self.text2.text = ''

		self.lbl1.text = f'{text1} {text2}'

		self.btn.background_color = (0,0,0,1)
		self.btn.color = (1,1,1,1)

	def release(self, instance):
		def f1():
			self.btn.background_color = (136/255, 176/255, 75/255, 1)
			self.btn.color = (1,0,0,1)

		def f2():
			sleep(2)
			self.lbl1.text = ''

		Thread(target=f1).start()
		Thread(target=f2).start()


class app(App):
	def build(self):
		return grid()

if __name__ == '__main__':
	app().run()