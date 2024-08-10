from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("login.kv")

class Myapp(App):
    def build(self):
        return GUI
    
Myapp().run()