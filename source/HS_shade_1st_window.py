from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design.kv')
class MyGridLayout(Widget):

    country = ObjectProperty(None)
    city = ObjectProperty(None)

    def press(self):
        # open HS_shade_2nd_window in future
        country = self.country.text
        city = self.city.text
        print(f'You live in {city}, {country}!')

        # clear the input boxes
        self.country.text = ''
        self.city.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
