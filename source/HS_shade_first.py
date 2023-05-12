from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu

import sqlite3
database = r"C:\Users\KATCZW\Desktop\MOJE\HS_shade\Hudson_sollutions_shade\Hudson_sollutions_shade.db"

Window.size = (360,600)

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class HS_shade_first(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('HS_shade_first.kv')
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT name FROM city")
        records = c.fetchall()
        cities = [str(record)[2:].split("'")[0] for record in records]
        menu_items = [
            {
                "text": f'{city}',
                "viewclass": "OneLineListItem",
                "height": dp(54),
                "on_release": lambda x=f"{city}": self.set_item(x),
            } for city in cities
        ]
        conn.commit()
        conn.close()
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.field,
            background_color=self.theme_cls.primary_dark,
            items=menu_items,
            position="bottom",
            width_mult=4,

        )

    def set_item(self, text__item):
        self.screen.ids.field.text = text__item
        self.user_city = text__item
        self.menu.dismiss()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        conn = sqlite3.connect(database)
        conn.close()
        return self.screen


HS_shade_first().run()