from kivymd.app import MDApp
from KivyCalendar import CalendarWidget
from kivymd.uix.pickers import MDDatePicker


class MyApp(MDApp):

    def build(self):
        #return CalendarWidget()
        return MDDatePicker(mode="range")

MyApp().run()