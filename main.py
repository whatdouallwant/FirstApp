# програма з двома екранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
# Екран (об'єкт класу Screen) – це віджет типу "макет" (Screen – спадкоємець класу RelativeLayout).
# ScreenManager - це особливий віджет, який робить видимим один із прописаних у ньому екранів.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # ім'я екрана має передаватися конструктору класу Screen
        text = Label(text="Виберіть дію:")
        btn = Button(text="Долари в гривні")
        btn2 = Button(text="Гривні в долари")
        layout = BoxLayout(orientation='vertical', spacing = '10sp')
        layout.add_widget(text)
        layout.add_widget(btn)
        layout.add_widget(btn2)


        btn.on_press = self.next
        self.add_widget(layout) # екран - це віджет, на якому можуть створюватись всі інші (нащадки)
    def next(self):
        self.manager.transition.direction = 'left' # об'єкт класу Screen має властивість manager 
        # - це посилання на батьківський клас
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        self.result = Label(text="Результат")
        self.input = TextInput(text='', multiline=False)
        btn = Button(text="Назад")

        layout = BoxLayout(orientation='vertical', spacing = '10sp')
        layout.add_widget(btn)
        layout.add_widget(self.input)
        layout.add_widget(self.result)
        btn.on_press = self.back
        self.add_widget(layout)
        self.input.bind(text=self.convert)

    def convert(self, *args):
        amount = float(self.input.text)
        res = round(amount * 41)
        self.result.text = f'UAH: {res}'


        

    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyConvertApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # буде показано FirstScr, тому що він доданий першим. Це можна змінити ось так:
        # sm.current = 'second'
        return sm

app = MyConvertApp()
app.run()