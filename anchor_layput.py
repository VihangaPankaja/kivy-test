from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class app(App):
	def build(self):
		layout1 = AnchorLayout(
			anchor_x = "left", 
			anchor_y = "bottom"
			)
		b1 = Button(
			text = "test text",
			size_hint = (.5, 1),
			background_color = (136/255 , 176/255, 75/255 ,1)
			)
		layout1.add_widget(b1)

		return layout1

if __name__ == '__main__':
	app().run()