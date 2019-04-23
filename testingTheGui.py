#cmd /K "$(FULL_CURRENT_PATH)"
#https://kivy.org/doc/stable/tutorials/pong.html
from kivy.config import Config
Config.set('graphics','window_state','maximized')
Config.set('kivy','window_icon','C:/Users/nogos/Documents/GitHub/Predicting-Elections/firstphotothingy_MtD_icon.ico')
Config.set('kivy','exit_on_escape','0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config

kv_str = """
#:import MAIN MAIN
#:import main MAIN
#:import collecting collecting
#:import Collect collecting
#:import scoring scoring
#:import Scoring scoring
#:import TextInput kivy.uix.textinput

MyScreenManager:
    BRANCH:
        name: 'branch'
    MAINPAGE:
        name: 'mainPage'
    COLLECTIONPAGE:
        name: 'collectPage'
    SCORINGPAGE:
        name: 'scorePage'
    FINAL_SCREEN:
        name: 'final_screen'

<BRANCH>
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Background.jpg"
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.35}
            font_size: 75
            text: 'Election Prediction and Analysis'
            color: 0, 0, 0, 1
        Button:
            id: btn
            text: 'Run Main Program'
            font_size: 30
            pos_hint: {'x': 0.25, 'y': 0.5}
            color: 1, 1, 1, 1
            size_hint_x: 0.5
            size_hint_y: 0.2
            on_release:
                root.manager.current = 'mainPage'
        Button:
            text: 'Run Collection Program'
            color: 1, 1, 1, 1
            font_size: 30
            pos_hint: {'x': 0.25, 'y': 0.3}
            size_hint_x: 0.5
            size_hint_y: 0.2
            on_release:
                root.manager.current = 'collectPage'
        Button:
            text: 'Run Scoring Program'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.5
            size_hint_y: 0.2
            pos_hint: {'x': 0.25, 'y': 0.1}
            on_release:
                root.manager.current = 'scorePage'

<MAINPAGE>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Background.jpg"
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.35}
            font_size: 75
            text: 'Main Program'
            color: 0, 0, 0, 1
        Button:
            text: 'Run the Program'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.125, 'y': 0.15}
            on_release:
                MAIN.main(root.textConvert(self))
        Button:
            text: 'Forward'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.525, 'y': 0.15}
            on_release:
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
        TextInput:
            focus: True
            unfocus_on_touch: False
            id: txt1
            hint_text: 'Input Candidates First and Last Names'
            size_hint_x: 0.75
            size_hint_y: 0.30
            pos_hint: {'x': 0.125, 'y': 0.35}
            multiline: True
            font_size: 35
            on_text_validate:
                MAIN.main(root.textConvert(self))

<COLLECTIONPAGE>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Background.jpg"
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 75
            text: 'Collection Program'
            color: 0, 0, 0, 1
        Button:
            text: 'Collect the Data'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.325, 'y': 0.35}
            on_release:
                collecting.Collect()

<SCORINGPAGE>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Background.jpg"
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 75
            text: 'Scoring Program'
            color: 0, 0, 0, 1
        Button:
            text: 'Score an Election'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.325, 'y': 0.35}
            on_release:
                scoring.Scoring()
"""

class MyScreenManager(ScreenManager):
    pass

class BRANCH(Screen):
    pass

class MAINPAGE(Screen):
    def textConvert(self,btn):
        return(self.ids.txt1.text)

class COLLECTIONPAGE(Screen):
    pass

class SCORINGPAGE(Screen):
    pass

class FINAL_SCREEN(Screen):
    pass

class MAINApp(App):
    def build(self):
        self.title = 'Election Prediction'
        self.icon = 'Logo.jpg'
        Window.bind(on_request_close = self.on_request_close)
        return Builder.load_string(kv_str)
    
    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def textpopup(self, title='', text=''):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='YES', size_hint=(1, 0.5))
        box.add_widget(mybutton)
        mybutton2 = Button(text='NO', size_hint=(1, 0.5))
        box.add_widget(mybutton2)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300), auto_dismiss=False)
        mybutton.bind(on_release=self.stop)
        mybutton2.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    MAINApp().run()