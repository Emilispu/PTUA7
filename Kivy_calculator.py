

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config

#konfiguruojame matmenis
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 250)
Config.set('graphics', 'height', 350)


class CalcApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):

        if (str(instance.text).lower() == 'x'):
            self.formula += '*'
        else:
            self.formula += str(instance.text)

        self.update_label()
    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = ''

    def add_operation(self, instrance):
        self.formula += str(instrance.text)
        self.update_label()


    def build(self):
        self.formula = ''
        bl = BoxLayout(orientation='vertical', padding = 10)
        gl = GridLayout(cols = 4, spacing = 5, size_hint = (1, 0.65))

        self.lbl = Label(text='0', font_size = 24, size_hint = (1, 0.35))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='x', on_press=self.add_number))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button())
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text=',', on_press=self.add_operation))
        gl.add_widget(Button(text='=', on_press=self.calc_result))

        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    CalcApp().run()

