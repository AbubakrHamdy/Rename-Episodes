from kivy.app import App
from kivy.core.text import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Form (GridLayout):
    def __init__(self,**kwargs):
        super(Form,self).__init__(**kwargs)
        self.ools=2

        self.username=TextInput(multiline=False)
        self.add_widget(self.username)


class TestApp(App):
    def build(self):
        #return Button(text='Hello World')
        return Form()


TestApp().run()