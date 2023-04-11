from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu

import sqlite3


class RightContentCls(IRightBodyTouch, MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()


class Item(OneLineAvatarIconListItem):
    left_icon = StringProperty()
    right_icon = StringProperty()
    right_text = StringProperty()


database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"


class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('my_app.kv')
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("SELECT name FROM city")
        records = c.fetchall()
        cities = [str(record)[2:].split("'")[0] for record in records]
        menu_items = [
            {
                "text": f'{city}',
                "left_icon": "city-variant",
                "viewclass": "Item",
                "height": dp(54),
                "on_release": lambda x=f"{city}": self.menu_callback(x),
            } for city in cities
        ]
        conn.commit()
        conn.close()
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
        )

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        conn = sqlite3.connect(database)
        conn.close()
        return self.screen


MyApp().run()