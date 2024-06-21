"""
CP1404/CP5632 Practical
Kivy program to demo some basic interactive functionality
"""

import kivy.app
from kivy.lang import Builder
from kivy.properties import StringProperty


class KivyDemo(kivy.app.App):
    status_text = StringProperty("Hello. Click the buttons :)")
    counter = 0

    def build(self):
        self.title = "Kivy Demo"
        self.root = Builder.load_file('6.kivy_layout.kv')
        return self.root

    def handle_press(self, amount):
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"


if __name__ == '__main__':
    KivyDemo().run()
