from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from data import data, data_answer

Builder.load_file('main_screen.kv')

data_button = []


class CopyLabel_1(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.font_style = 'Subtitle2'


class CopyLabel_2(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.font_style = 'Caption'


class MainScreen(Screen):
    pass


class MainApp(MDApp):

    def on_start(self):
        for i in range(len(data)):
            text_1 = data[i][0]
            text_2 = data[i][1]
            self.locale_1 = f'''
MDTextField:
    id: {i}
    hint_text: "Ответ"
    font_style: 'Caption'
    font_size: '10sp'
    helper_text_mode: "on_focus"
'''
            self.locale_2 = f'''  
MDRectangleFlatIconButton:
    icon: 'key'
    text: 'Проверить ответ'
    theme_text_color: 'Hint'
    on_release: app.show_data({i})
    
'''


            self.copy_label_1 = CopyLabel_1(text=text_1)
            self.copy_label_2 = CopyLabel_2(text=text_2)
            self.root.ids.box.add_widget(self.copy_label_1)
            self.root.ids.box.add_widget(self.copy_label_2)

            self.data_1 = Builder.load_string(self.locale_1)
            data_button.append(self.data_1)
            self.data_2 = Builder.load_string(self.locale_2)

            self.root.ids.box.add_widget(self.data_1)
            self.root.ids.box.add_widget(self.data_2)

    def show_data(self, id):
        input_answer = data_button[id].text
        if input_answer == data_answer[id]:
            print(input_answer, 'YES')

            dialog = MDDialog(
                text='Все верно, продолжим дальше!',
                buttons=[
                    MDFlatButton(
                        text='Следующее задание',
                        on_release=lambda _: dialog.dismiss()
                    )
                ]
            )

            dialog.open()

        else:
            print(input_answer, 'NO')
            self.dialog_2 = MDDialog(
                text=f'Правильный ответ: {data_answer[id]}',
                buttons=[
                    MDFlatButton(
                        text='Закрыть',
                        on_release=lambda _: self.dialog_2.dismiss()
                    )
                ]
            )
            def dialog_aaa():
                self.dialog.dismiss()
                self.dialog_2.open()
            self.dialog = MDDialog(
                text='Неверно, попробуете заново или посмотреть ответ?',
                buttons=[
                    MDFlatButton(
                        text='Попытаться',
                        on_release=lambda _: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text='Показать ответ',
                        on_release=lambda _: dialog_aaa()
                    )
                ]
            )
            self.dialog.open()

    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
