from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

KV = '''
MDScrollView:

    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "1 style"
            halign: "center"
            adaptive_height: True
        MDLabel:
            text: "2 style"
            halign: "center"
            adaptive_height: True
        MDLabel:
            text: "3 style"
            halign: "center"
            adaptive_height: True
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)

        return screen


Test().run()