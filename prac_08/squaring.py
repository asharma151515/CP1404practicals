from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class SquaringApp(App):
    result = StringProperty('')

    def build(self):
        self.title = "Squaring a Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def calculate_square(self):
        try:
            # Get the number from the TextInput
            number = float(self.root.ids.input_number.text)
            # Calculate the square
            square = number ** 2
            # Update the result property
            self.result = str(square)
        except ValueError:
            self.result = "Invalid input!"

    def clear_input(self):
        # Clear the TextInput and the result
        self.root.ids.input_number.text = ''
        self.result = ''

SquaringApp().run()