'''
how fast is your brain? are you ready for challange?
'''
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen,RiseInTransition,FallOutTransition,WipeTransition ,FadeTransition,SlideTransition,SwapTransition
import random
class MyScreenManager(ScreenManager):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    info= "Instruction \n tap when you \nsee the  same letter \nas two letter befor"

class TestScreen(Screen):
    lista=[]
    minus=0
    plus=0
    expected=0
    def on_enter(self, *args):
        Clock.schedule_interval(self.update, 0.5)
    def update(self, *args):
        tekst=self.ids['letter']
        # zakres liter w chr jest od 65-90 ale biorac tak dlugi zakres, rzadko beda sie powtarzac
        #wezmy 10 pierwszych liter
        liter=chr(random.randint(65,75))
        tekst.text=liter
        self.lista.append(liter)
        print self.lista
        if len(self.lista)==20:
            Clock.unschedule(self.update)
            root_widget.current = 'menu'
            self.lista=[]
            print 'You missed: ', str(self.expected-self.plus)
            self.expected=0
        if len(self.lista)>2:
            if self.lista[-1] == self.lista[-3]:
                self.expected+=1
    def on_touch_down(self, touch):
        if self.lista[-1] == self.lista[-3]:
            self.plus+=1
        else:
            self.minus-=1
        print 'poprawnych: ',str(self.plus), ' niepoprawnych: ', str(self.minus)




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
            size_hint: 1,0.1
            text:"tap"
        Label:
            id: letter
            size_hint: 1,1
            text: "letter"


''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()