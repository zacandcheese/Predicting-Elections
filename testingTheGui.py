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
from kivy.clock import Clock
from functools import partial
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import NumericProperty
import MAIN
import loading

kv_str = """
#:import MAIN MAIN
#:import main MAIN
#:import collecting collecting
#:import Collect collecting
#:import scoring scoring
#:import Scoring scoring
#:import TextInput kivy.uix.textinput
#:import ProgressBar kivy.uix.progressbar

MyScreenManager:
    BRANCH:
        name: 'branch'
    MAINPAGE:
        name: 'mainPage'
    COLLECTIONPAGE:
        name: 'collectPage'
    SCORINGPAGE:
        name: 'scorePage'

<BRANCH>
    id: 'branch'
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
                root.manager.transition.direction = 'left'
                root.manager.current = 'mainPage'
        Button:
            text: 'Run Collection Program'
            color: 1, 1, 1, 1
            font_size: 30
            pos_hint: {'x': 0.25, 'y': 0.3}
            size_hint_x: 0.5
            size_hint_y: 0.2
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'collectPage'
        Button:
            text: 'Run Scoring Program'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.5
            size_hint_y: 0.2
            pos_hint: {'x': 0.25, 'y': 0.1}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'scorePage'
<LoadingPopup>:
    title: "Main Program Running"
    size_hint: None, None
    size: 600, 200
    auto_dismiss: False
    Label:
        text: 'Do Not Close Window or Power Off Computer, Program is Running'
        color: 1, 1, 1, 1
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
                root.runMain(root.textConvert(self))
        Button:
            text: 'Back'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.525, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
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
            pos_hint: {'x': 0.00, 'y': 0.35}
            font_size: 75
            text: 'Collection'
            color: 0, 0, 0, 1
        Button:
            text: 'Run the Program'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.125, 'y': 0.15}
            on_release:
                collecting.Collect(root.textConvert(self))
        Button:
            text: 'Back'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.525, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
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
                collecting.Collect(root.textConvert(self))

<SCORINGPAGE>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Background.jpg"
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.35}
            font_size: 75
            text: 'Scoring'
            color: 0, 0, 0, 1
        Button:
            text: 'Run the Program'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.125, 'y': 0.15}
            on_release:
                scoring.Scoring(root.textConvert(self))
        Button:
            text: 'Back'
            color: 1, 1, 1, 1
            font_size: 30
            size_hint_x: 0.35
            size_hint_y: 0.15
            pos_hint: {'x': 0.525, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
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
                scoring.Scoring(root.textConvert(self))
"""

class MyScreenManager(ScreenManager):
    pass

class BRANCH(Screen):
    pass

class LoadingPopup(Popup):
    def __init__(self, obj, **kwargs):
        super(LoadingPopup, self).__init__(**kwargs)

class MAINPAGE(Screen):
    def textConvert(self,btn):
        return(self.ids.txt1.text)
		
    def call(self, text):
        print(MAIN.main(text))
		
    def __init__(self, **kwargs):
        super(MAINPAGE, self).__init__(**kwargs)
        self.popup = LoadingPopup(self)
		
    def open(self):
        self.popup.open()
		
    def runMain(self, text):
        self.open()
        Clock.schedule_once(lambda dt: self.call(text), 0.5)

class COLLECTIONPAGE(Screen):
    def textConvert(self,btn):
        return(self.ids.txt1.text)

class SCORINGPAGE(Screen):
    def textConvert(self,btn):
        return(self.ids.txt1.text)

class MAINApp(App):
    def build(self):
        self.title = 'Election Prediction'
        self.icon = 'Icon.png'
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