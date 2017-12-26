from kivy.app import App
from kivy.uix.button import Button

class Myapp(App):
    def build(self):
        return Button(text = "Hello World! This is my first Android app based on Kivy. :)")

if __name__ == "__main__":
    Myapp().run()
