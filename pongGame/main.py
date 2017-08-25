from kivy.app import App
from kivy.uix.widget import Widget

class pongGame(Widget):
    pass

class pongApp(App):
    def build(self):
        return pongGame()

if __name__ == "__main__":
    pongApp().run()


