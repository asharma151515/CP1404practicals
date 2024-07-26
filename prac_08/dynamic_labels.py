from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice Smith", "Bob Brown", "Cat Cyan", "Oren Ochre"]
        self.create_labels()

    def create_labels(self):
        """Create labels for each name in the names list."""
        for name in self.names:
            label = Label(text=name)  # Create a label with the name
            self.add_widget(label)  # Add the label to the layout

class DynamicLabelsApp(App):
    def build(self):
        return MainLayout()  # Return the main layout

if __name__ == '__main__':
    DynamicLabelsApp().run()