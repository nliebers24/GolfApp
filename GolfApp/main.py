from kivy.app import App
from kivy.modules import inspector  # For inspection.
from kivy.core.window import Window  # For inspection.
from kivy.properties import NumericProperty
from kivy.lang import Builder


golf = Builder.load_file("golf.kv")


class GolfApp(App):
    def build(self):
        return golf


if __name__ == '__main__':
    app = GolfApp()
    app.run()
