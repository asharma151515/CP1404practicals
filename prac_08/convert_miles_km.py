from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class MilesToKmConverter(App):
    result = StringProperty('')

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self):
        try:
            # Get the miles from the TextInput
            miles = float(self.root.ids.input_miles.text)
            # Convert miles to kilometers (1 mile = 1.60934 kilometers)
            kilometers = miles * 1.60934
            # Update the result property
            self.result = f"{kilometers:.2f} km"
        except ValueError:
            self.result = "Invalid input!"

    def clear_input(self):
        # Clear the TextInput and the result
        self.root.ids.input_miles.text = ''
        self.result = ''

    def increment(self):
        try:
            # Increment the miles value by 1
            miles = float(self.root.ids.input_miles.text)
            miles += 1
            self.root.ids.input_miles.text = str(miles)
            self.convert()  # Update the conversion result
        except ValueError:
            self.root.ids.input_miles.text = '1'  # Default to 1 if input is invalid
            self.convert()

    def decrement(self):
        try:
            # Decrement the miles value by 1
            miles = float(self.root.ids.input_miles.text)
            miles -= 1
            self.root.ids.input_miles.text = str(miles)
            self.convert()  # Update the conversion result
        except ValueError:
            self.root.ids.input_miles.text = '0'  # Default to 0 if input is invalid
            self.convert()

MilesToKmConverter().run()