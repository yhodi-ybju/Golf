import kivy
kivy.require('2.2.1')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file('app.kv')

# Create a background class that inherits the box layout class
class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    pass


# Create an App class with the name of your App
class SampleApp(App):
    # Return the Window having the background template.
    def build(self):
        return Background()


# Run app in the main function
if __name__ == '__main__':
    SampleApp().run()