from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

Builder.load_file('main_screen.kv')


class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def on_tab_screen_2(self):
        screen = Builder.load_file('test_screen.kv')
        print('-----------')
        for i in range(5):
            screen.ids.box.add_widget(
                MDLabel(
                    text='gggggg',
                    halign='center',
                    adaptive_height=True
                )
            )
        return screen

    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
