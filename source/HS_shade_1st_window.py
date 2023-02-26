import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MyGridLayout(Widget):

    def press(self, instance):
        # open HS_shade_2nd_window in future
        country = self.country.text
        city = self.city.text
        self.add_widget(Label(text=f'You live in {city}, {country}!'))


class HS_shade_1st_window(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    HS_shade_1st_window().run()
