from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from data import data_ege, data_word
import random

Builder.load_file('main_screen.kv')


class CopyLabel_1(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.font_style = 'Subtitle2'


class CopyLabel_2(MDLabel):
    # Преобразование элементов для текста
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.font_style = 'Caption'


class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.data_2 = None
        self.data_1 = None
        self.copy_label_2 = None
        self.copy_label_1 = None
        self.locale_2 = None
        self.locale_1 = None
        self.data_count_app = None
        self.data_answer_flag = None
        self.data_button = None
        self.id_colection = None


    def on_start(self):
        self.data_button = dict()
        self.data_answer_flag = dict()
        self.id_colection = []
        self.data_count_app = 0

        self.root.ids.box.add_widget(Builder.load_string('''
MDLabel:
    adaptive_height: True
    font_style: 'Button'
    text: '9 задание'
    halign: 'center'
'''))
        for i in range(5):
            id_word = random.randint(0, 350)
            self.data_answer_flag[f'word_{id_word}'] = 1

            text_1 = 'Запишите слово с вставленными в пропуски буквами'
            text_2 = data_word[f'word_{id_word}'][1]
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
    on_release: app.show_data('word_{id_word}')
'''

            # добавить текст задания на экран
            self.copy_label_1 = CopyLabel_1(text=text_1)
            self.copy_label_2 = CopyLabel_2(text=text_2)
            self.root.ids.box.add_widget(self.copy_label_1)
            self.root.ids.box.add_widget(self.copy_label_2)

            # добавить кнопки на экран
            self.data_1 = Builder.load_string(self.locale_1)
            self.data_button[f'word_{id_word}'] = self.data_1
            self.data_2 = Builder.load_string(self.locale_2)

            self.root.ids.box.add_widget(self.data_1)
            self.root.ids.box.add_widget(self.data_2)

        for i in range(5):
            while True:
                id_ege = random.randint(0, len(data_ege) - 1)
                if id_ege not in self.id_colection:
                    self.id_colection.append(id_ege)
                    break

            self.data_answer_flag[f'ege_{id_ege}'] = 1

            text_1 = data_ege[f'ege_{id_ege}'][0][0]
            text_2 = data_ege[f'ege_{id_ege}'][0][1]
            self.locale_1 = f'''
MDTextField:
    id: ege_{id_ege}
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
    on_release: app.show_data('ege_{id_ege}')
'''

            # добавить текст задания на экран
            self.copy_label_1 = CopyLabel_1(text=text_1)
            self.copy_label_2 = CopyLabel_2(text=text_2)
            self.root.ids.box.add_widget(self.copy_label_1)
            self.root.ids.box.add_widget(self.copy_label_2)

            # добавить кнопки на экран
            self.data_1 = Builder.load_string(self.locale_1)
            self.data_button[f'ege_{id_ege}'] = self.data_1
            self.data_2 = Builder.load_string(self.locale_2)

            self.root.ids.box.add_widget(self.data_1)
            self.root.ids.box.add_widget(self.data_2)

            if i == 4:
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

        if self.data_count_app <= 5:
            text = 'Лучше потренируйтесь еще и обязательно повторите теорию'
        elif self.data_count_app <= 10:
            text = 'Хороший результат, так держать!'
        else:
            text = 'Прекрасный результат!'
        dialog = MDDialog(
            title=text,
            buttons=[
                MDFlatButton(
                    text='Пройти следующий тест',
                    on_release=lambda _: func()
                )
            ]
        )
        dialog.open()

    def show_data(self, id_element):
        input_answer = self.data_button[id_element].text

        # проверка вида теста
        if id_element[:3] == 'ege':
            flag = input_answer == data_ege[id_element][2] and self.data_answer_flag[id_element]
        else:
            flag = input_answer == data_word[id_element][0] and self.data_answer_flag[id_element]

        if flag:
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
            if id_element[:3] == 'ege':
                answer = (f"[font=21154.otf]{data_ege[id_element][2][0]}\n"
                          f"{data_ege[id_element][1][0]}\n{data_ege[id_element][1][1]}[/font]")
            else:
                answer = data_word[id_element][0]

            dialog_2 = MDDialog(
                text=f'Правильный ответ: {answer}',
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
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
