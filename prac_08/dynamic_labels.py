from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label  # Import the Label class


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels Example"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        # List of names to create labels for
        names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

        # Clear existing labels
        self.root.ids.labels_box.clear_widgets()

        # Create a label for each name and add it to the layout
        for name in names:
            label = Label(text=name, font_size=24, background_color=(1, 0, 0, 1))  # Red background
            self.root.ids.labels_box.add_widget(label)


class MainLayout(BoxLayout):
    pass


DynamicLabelsApp().run()