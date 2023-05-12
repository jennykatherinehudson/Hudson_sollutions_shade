from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from KivyCalendar import CalendarWidget

#import HS_shade_first as HS
import sqlite3

Window.size = (360,600)
#database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"
#user_city = HS.HS_shade_first().user_city
user_city = 'Krakow'

class HS_shade_second(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('HS_shade_second.kv')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        #conn = sqlite3.connect(database)
        #conn.close()
        return self.screen


HS_shade_second().run()