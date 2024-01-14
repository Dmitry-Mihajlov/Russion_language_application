from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

Builder.load_file('main_screen.kv')

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


class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def on_start(self):
        for text in data:
            copy_label = CopyLabel(text=text)
            self.root.ids.box.add_widget(copy_label)

    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
