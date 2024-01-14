from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

class MainScreen(Screen):
    def main(self):
        return Builder.load_file('main_screen.kv')


class MainApp(MDApp):
    def on_tab_screen_2(self):
        print('hshshshsshshshshshshshssh')

    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
