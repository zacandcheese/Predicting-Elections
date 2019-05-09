from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.properties import NumericProperty
import sys
import os


class CircularProgressBar(ProgressBar):
    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        self.thickness = 35
        self.label = CoreLabel(text="0%", font_size=60)
        self.texture_size = None
        self.refresh_text()
        self.draw()

    def draw(self):
        with self.canvas:
            self.canvas.clear()
            with self.canvas.before:
                Rectangle(size=(5000,5000), pos=self.pos, source='Background.jpg')
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)
            Color(0, 0.65, 1)
            Ellipse(pos=self.pos, size=self.size, angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized*360))
            Color(0, 0, 0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2), size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture, size=self.texture_size, pos=(self.size[0]/2 - self.texture_size[0]/2, self.size[1]/2 - self.texture_size[1]/2))

    def refresh_text(self):
        self.label.refresh()
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        self.value = value
        self.label.text = str(int(self.value_normalized*100)) + "%"
        self.refresh_text()
        self.draw()

class Main(App):

    # Simple animation to show the circular progress bar in action
    def animate(self, dt):
        if self.root.value < 80:
            self.root.set_value(self.root.value + 1)
    # Simple layout for easy example
    def build(self):
        container = Builder.load_string(
            '''CircularProgressBar:
    size_hint: (None, None)
    height: 200
    width: 200
    max: 80''')

        # Animate the progress bar
        Clock.schedule_interval(self.animate, 0.01)
        return container


if __name__ == '__main__':
    Main().run()