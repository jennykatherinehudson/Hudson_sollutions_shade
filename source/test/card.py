from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

str = '''

MDFloatLayout:
    MDCard:
        pos_hint: {"center_x": .5, "center_y": .8 }
        size_hint: .75, .25
        md_bg_color: "#f4dedc"
        MDLabel:
            text: "Hi"
            text_color: "black"
            haling: "center"
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"

    MDCard:
        pos_hint: {"center_x": .5, "center_y": .3 }
        size_hint: .75, .25
        md_bg_color: "#f8f5f4"
        MDLabel:
            text: "Hi"
            haling: "center"
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"

    
'''

Window.size = (360,600)

class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        card = Builder.load_string(str)
        return card

Test().run()    