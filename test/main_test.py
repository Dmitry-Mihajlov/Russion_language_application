from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp


Builder.load_file('main_screen_test.kv')



class MainApp(MDApp):

    def build(self):
        return Builder.load_file('main_screen_test.kv')


if __name__ == '__main__':
    MainApp().run()