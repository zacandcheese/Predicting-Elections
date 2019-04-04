#cmd /K "$(FULL_CURRENT_PATH)"
#https://kivy.org/doc/stable/tutorials/pong.html
from kivy.config import Config
Config.set('kivy','window_icon','C:/Users/nogos/Documents/GitHub/Predicting-Elections/firstphotothingy_MtD_icon.ico')
Config.set('kivy', 'exit_on_escape', '0')

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

kv_str = """
#:import MAIN MAIN
#:import main MAIN
#:import TextInput kivy.uix.textinput

MyScreenManager:
    WELCOME:
        name: 'welcome'
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
    SECRET_PAGE:
        name: 'secretMain'
<WELCOME>
    FloatLayout:
        Image:
            source: "FirstPhotoThingy.png"
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 90
            text: 'Welcome'
            color: 0, 0, 0, 1
        Button:
            text: 'Click to Continue.'
            color: 1.0, 0.6, 0.0, 1
            font_size: 30
            size_hint_x: 0.50
            size_hint_y: 0.25
            pos_hint: {'x': 0.25, 'y': 0.25}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'branch'
<BRANCH>
    FloatLayout:
    Button:
        text: 'Run Main Project'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.25, 'y': 0.75}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'mainPage'
    Button:
        text: 'Run Collection'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.25, 'y': 0.375}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'collectPage'
    Button:
        text: 'Run Scoring'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.25, 'y': 0.0}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'scorePage'
<MAINPAGE>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'this is SCREEN-1'
            color: 1, 1, 1, 1
        Button:
            text: 'Forward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.50, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
        TextInput:
            id: txt1
            text: ""
            hint_text: 'Input Candidates First and Last Names'
            size_hint_x: 0.75
            size_hint_y: None
            pos_hint: {'x': 0.125, 'y': 0.40}
            multiline: True
            font_size: 35
            on_quad_touch:
                root.manager.current = 'secretMain'
        Button:
            text: 'FIND'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.30, 'y': 0.15}
            on_release:
                print(root.textConvert(self))
                MAIN.main(root.textConvert(self))
<COLLECTIONPAGE>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'me este SCREEN-2'
            color: 1, 1, 1, 1
        Button:
            text: 'Onward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
<SCORINGPAGE>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'something SCREEN-3'
            color: 1, 1, 1, 1
        Button:
            text: 'Lets Go'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
<FINAL_SCREEN>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'Final Screen'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.60, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = root.previous
        Button:
            text: 'Restart'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.20, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
<SECRET_PAGE>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'WELCOME TO THE SECRET PAGE'
            color: 1, 1, 1, 1
        Button:
            text: 'Onward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
"""

class MyScreenManager(ScreenManager):
    pass

class WELCOME(Screen):
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

class SECRET_PAGE(Screen):
    pass

class MAINApp(App):
    def build(self):
        self.title = 'Election Prediction'
        self.icon = 'FirstPhotoThingy.png'
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