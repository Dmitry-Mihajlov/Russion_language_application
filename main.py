from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from data import data, data_answer

Builder.load_file('main_screen.kv')


class CopyLabel(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.font_style = 'Subtitle2'


class MainScreen(Screen):
    pass



class MainApp(MDApp):
    def on_start(self):
        for i in range(len(data)):
            text = data[i]
            locale = f'''
MDBoxLayout:
    MDTextField:
        id: {i}
        hint_text: "Ответ"
        font_style: 'Subtitle2'
        font_size: '14sp'
        helper_text_mode: "on_focus"
            '''
            copy_label = CopyLabel(text=text)
            self.root.ids.box.add_widget(copy_label)
            self.root.ids.box.add_widget(Builder.load_string(locale))


    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
