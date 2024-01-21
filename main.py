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
import random

data_button = []
data_count_app = 0


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

    def start_app(self):
        kv = '''
    <MainScreen>:

    BoxLayout:
        orientation: 'vertical'
        MDBottomNavigation:
            #panel_color: "#eeeaea"
            text_color_active: "lightgrey"
            text_color_normal: 1, 1, 1, 1
            text_color_active: 0, 0, 0, 1

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Практикум'
                icon: 'pencil'

                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout:
                        ScrollView:
                            MDBoxLayout:
                                id: box
                                orientation: "vertical"
                                padding: "10dp"
                                spacing: "10dp"
                                adaptive_height: True
                                MDLabel:
                                    adaptive_height: True
                                    font_style: 'Button'
                                    text: '9 задание'
                                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Теория'
                icon: 'book'

                MDLabel:
                    text: 'Сакшен Сакшен Сакшен Сакс'
                    halign: "center"

        '''
        global data_answer_flag, data_count_app
        data_count_app = 0
        data_answer_flag = [1 for i in range(10)]

        Builder.load_string(kv)
        print('перезапуск')
        MainApp().start_func(kv)


    def start_func(self, kv):
        data_app = random.choices(data, k=1)
        for i in range(len(data_app)):
            text_1 = data[i][0]
            text_2 = data[i][1]
            locale_1 = f'''
MDTextField:
    id: {i}
    hint_text: "Ответ"
    font_style: 'Caption'
    font_size: '10sp'
    helper_text_mode: "on_focus"
'''
            locale_2 = f'''  
MDRectangleFlatIconButton:
    icon: 'key'
    text: 'Проверить ответ'
    theme_text_color: 'Hint'
    on_release: app.show_data({i})
    
'''

            copy_label_1 = CopyLabel_1(text=text_1)
            copy_label_2 = CopyLabel_2(text=text_2)
            self.root.ids.box.add_widget(copy_label_1)
            self.root.ids.box.add_widget(copy_label_2)

            data_1 = Builder.load_string(locale_1)
            data_button.append(data_1)
            data_2 = Builder.load_string(locale_2)

            self.root.ids.box.add_widget(data_1)
            self.root.ids.box.add_widget(data_2)

            if i == len(data_app) - 1:
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
            dialog.dismiss()
            self.on_start()

        if data_count_app < len(data) / 5:
            text = 'Лучше потренируйтесь еще и обязательно повторите теорию'
        elif data_count_app < 8 * len(data) / 10:
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
        if input_answer == data_answer[id_element] and data_answer_flag[id_element]:
            print(input_answer, 'YES')

            def dialog_answer_good():
                global data_count_app
                dialog.dismiss()
                data_count_app += 1
                print(data_count_app)

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

        elif data_answer_flag[id_element]:
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
                data_answer_flag[id_element] = 0

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

    def on_start(self):
        return self.start_app()


if __name__ == '__main__':
    MainApp().run()
