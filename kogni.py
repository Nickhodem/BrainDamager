'''
how fast is your brain? are you ready for challange?
'''
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen,RiseInTransition,FallOutTransition,WipeTransition ,FadeTransition,SlideTransition,SwapTransition

class MyScreenManager(ScreenManager):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    info= "Instruction \n tap when you \nsee the  same letter \nas two letter befor"

class TestScreen(Screen):
    pass
root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import RiseInTransition kivy.uix.screenmanager.SlideTransition

MyScreenManager:
    transition: RiseInTransition()
    FirstScreen:
    SecondScreen:
    TestScreen:

<FirstScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        padding: 10,10,10,10
        spacing: 10
        Label:
            text: "Welcome to Brain Challenge"
        Button:
            text: 'START'
            on_release: app.root.current = 'info'
        Button:
            text: 'easy'
        Button:
            text: 'medium'
        Button:
            text: 'hard'
<SecondScreen>:
    name: 'info'
    BoxLayout:
        orientation: 'vertical'
        padding: 10,10,10,10
        spacing: 10
        Label:
            text: root.info
        Button:
            text: 'go and damage your brain'
            on_release: app.root.current = 'test'

<TestScreen>:
    name: 'test'
    BoxLayout:
        orientation: 'vertical'
        padding: 10,10,10,10
        spacing: 10
        Label:
            text:"tap"
''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()