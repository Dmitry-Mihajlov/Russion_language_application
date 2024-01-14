from kivy.core.clipboard import Clipboard
from kivy.lang.builder import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast

KV = '''
MDBoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    padding: "24dp"

    MDScrollView:

        MDBoxLayout:
            id: box
            orientation: "vertical"
            padding: "24dp"
            spacing: "12dp"
            adaptive_height: True

    MDTextField:
        max_height: "200dp"
        mode: "fill"
        multiline: True

    MDWidget:
'''

data = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Sed blandit libero volutpat sed cras ornare arcu. Nisl vel pretium "
    "lectus quam id leo in. Tincidunt arcu non sodales neque sodales ut etiam.",
    "Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. "
    "Nisl rhoncus mattis rhoncus urna neque. Orci nulla pellentesque "
    "dignissim enim. Ac auctor augue mauris augue neque gravida in fermentum. "
    "Lacus suspendisse faucibus interdum posuere."

]


class CopyLabel(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.theme_text_color = "Custom"
        self.text_color = self.theme_cls.text_color


class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for text in data:
            copy_label = CopyLabel(text=text)
            self.root.ids.box.add_widget(copy_label)


Example().run()