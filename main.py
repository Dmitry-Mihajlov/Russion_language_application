from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from Russion_language_application.data import data, data_answer, data_word
import random

Builder.load_file(r'D:\Programming\PyCharm\Russion_language_application\main_screen.kv')
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
        global data_button
        data_button = []

        self.data_answer_flag = [1 for i in range(10)]
        self.data_count_app = 0

        for i in range(5):
            id_word = random.randint(0, 350)
            text = data_word[f'word_{id_word}']
            self.locale_1 = f'''
MDTextField:
    id: word_{id_word}
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

            # добавить текст задания на экран
            self.copy_label = CopyLabel_1(text=text)
            self.root.ids.box.add_widget(self.copy_label)

            # добавить кнопки на экран
            self.data_1 = Builder.load_string(self.locale_1)
            data_button.append(self.data_1)
            self.data_2 = Builder.load_string(self.locale_2)

            self.root.ids.box.add_widget(self.data_1)
            self.root.ids.box.add_widget(self.data_2)

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

            # добавить текст задания на экран
            self.copy_label_1 = CopyLabel_1(text=text_1)
            self.copy_label_2 = CopyLabel_2(text=text_2)
            self.root.ids.box.add_widget(self.copy_label_1)
            self.root.ids.box.add_widget(self.copy_label_2)

            # добавить кнопки на экран
            self.data_1 = Builder.load_string(self.locale_1)
            data_button.append(self.data_1)
            self.data_2 = Builder.load_string(self.locale_2)

            self.root.ids.box.add_widget(self.data_1)
            self.root.ids.box.add_widget(self.data_2)

            if i == len(data) - 1:
                self.root.ids.box.add_widget(Builder.load_string(
                    '''
MDRoundFlatButton:
    text: 'Результаты'
    theme_text_color: 'Hint'
    on_release: app.result()
    pos_hint: {"center_x": .5}
'''
                ))


    def result(self):
        def func():
            self.root.ids.box.clear_widgets()
            dialog.dismiss()
            self.on_start()

        if self.data_count_app < len(data) / 5:
            text = 'Лучше потренируйтесь еще и обязательно повторите теорию'
        elif self.data_count_app < 8 * len(data) / 10:
            text = 'Хороший результат, так держать!'
        else:
            text = 'Прекрасный результат!'
        dialog = MDDialog(
            text=text,
            buttons=[
                MDFlatButton(
                    text='Пройти следующий тест',
                    on_release=lambda _: func()
                )
            ]
        )
        dialog.open()

    def show_data(self, id_element):
        input_answer = data_button[id_element].text
        if input_answer == data_answer[id_element] and self.data_answer_flag[id_element]:
            print(input_answer, 'YES')

            def dialog_answer_good():
                dialog.dismiss()
                self.data_count_app += 1
                print(self.data_count_app)

            dialog = MDDialog(
                text='Все верно, продолжим дальше!',
                buttons=[
                    MDFlatButton(
                        text='Следующее задание',
                        on_release=lambda _: dialog_answer_good()
                    )
                ]
            )
            dialog.open()

        elif self.data_answer_flag[id_element]:
            print(input_answer, 'NO')
            dialog_2 = MDDialog(
                text=f'Правильный ответ: {data_answer[id_element]}',
                buttons=[
                    MDFlatButton(
                        text='Закрыть',
                        on_release=lambda _: dialog_2.dismiss()
                    )
                ]
            )

            def dialog_review():
                dialog.dismiss()
                dialog_2.open()
                self.data_answer_flag[id_element] = 0

            dialog = MDDialog(
                text='Неверно, попробуете заново или посмотреть ответ?',
                buttons=[
                    MDFlatButton(
                        text='Попытаться',
                        on_release=lambda _: dialog.dismiss()
                    ),
                    MDFlatButton(
                        text='Показать ответ',
                        on_release=lambda _: dialog_review()
                    )
                ]
            )
            dialog.open()
        else:
            dialog = MDDialog(
                text='Вы уже посмотрели ответ, поэтому не можете больше вносить изменения',
                buttons=[
                    MDFlatButton(
                        text='Закрыть',
                        on_release=lambda _: dialog.dismiss()
                    )
                ]
            )
            dialog.open()

    def build(self):
        Window.size = (300, 500)
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
