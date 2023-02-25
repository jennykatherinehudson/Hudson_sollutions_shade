import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 1
        #image widget
        self.Hudson_logo = Image(
                            source = 'Hudson_sollutions_white.png', 
                            pos_hint = {'center_x' : 1, 'center_y' : 1 },
                            #size_hint = (1,1)
        )
        self.add_widget(self.Hudson_logo)
        #Add widgets
        self.add_widget(Label(text = 'Select country'))

        #Add input box
        self.country = TextInput(multiline = False)
        self.add_widget(self.country)

        #Add widgets
        self.add_widget(Label(text = 'Select city'))

        #Add input box
        self.city = TextInput(multiline = False)
        self.add_widget(self.city)

        # Create OK button
        self.OKbutton = Button(text = 'OK', font_size = 32)
        #Bind the button
        self.OKbutton.bind(on_press = self.press)
        self.add_widget(self.OKbutton)

    def press(self,instance):
        #open HS_shade_2nd_window in future
        country = self.country.text
        city = self.city.text
        self.add_widget(Label(text = f'You live in {city}, {country}!'))



class HS_shade_1st_window(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    HS_shade_1st_window().run()