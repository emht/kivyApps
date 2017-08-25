import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label

class pongGame(App):
    def build(self):
        return Label(text='Hello World');

if __name__ == "__main__":
    pongGame().run();
