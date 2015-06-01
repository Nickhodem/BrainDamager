'''
how fast is your brain? are you ready for challange?
'''
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen,RiseInTransition,FallOutTransition,WipeTransition ,FadeTransition,SlideTransition,SwapTransition
import random

fps=1
score=[0,0,0]
class MyScreenManager(ScreenManager):
    pass
class FirstScreen(Screen):
    def do_level(self, level):
        global fps
        if level=='easy':
            fps=1
        elif level =='medium':
            fps=0.5
        else:
            fps=0.2
        root_widget.current = 'info'
        return fps
class SecondScreen(Screen):
    info= "Instruction \n tap when you \nsee the  same letter \nas two letter befor"

class TestScreen(Screen):
    lista=[]
    minus=0
    plus=0
    expected=0
    def on_enter(self, *args):
        self.expected=0
        self.plus=0
        self.minus=0
        print str(fps)
        self.update_score()
        Clock.schedule_interval(self.update, fps)
    def update(self, *args):
        tekst=self.ids['letter']
        # zakres liter w chr jest od 65-90 ale biorac tak dlugi zakres, rzadko beda sie powtarzac
        #wezmy 10 pierwszych liter
        liter=chr(random.randint(65,70))
        tekst.text=liter
        tekst.color=[random.random(),random.random(),random.random(),1]
        self.lista.append(liter)
        print self.lista
        if len(self.lista)==10:
            Clock.unschedule(self.update)
            root_widget.current = 'wynik'
            self.lista=[]
            global score

            print 'You missed: ', str(self.expected-self.plus)
            print 'wrong: ', str(-1*self.minus)
            print 'right: ', str(self.plus)
            score=[self.expected, self.plus, self.minus]
            return score
        if len(self.lista)>2:
            if self.lista[-1] == self.lista[-3]:
                self.expected+=1
    def update_score(self):
        good=self.ids['plus']
        good.text='right: '+str(self.plus)
        schelcht=self.ids['minus']
        schelcht.text='wrong: '+str(self.minus)
    def on_touch_down(self, touch):
        if len(self.lista)>2:
            if self.lista[-1] == self.lista[-3]:
                self.plus+=1
            else:
                self.minus-=1
            print 'poprawnych: ',str(self.plus), ' niepoprawnych: ', str(self.minus)
        self.update_score()

class ScoreBoard(Screen):
    global score
    tekst='Score board\n '+str(score)
    print score
    def on_touch_down(self, touch):
        root_widget.current = 'menu'





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
    ScoreBoard:

<FirstScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        padding: 10,10,10,10
        spacing: 10
        Label:
            text: "Welcome to Brain Challenge"
            color: 0,1,0.9411,1
            bold: True
        Button:
            text: 'easy'
            color: 0,1,0.9411,1
            background_color: 0, 0.5019, 0.8784, 1
            on_press: root.do_level('easy')
        Button:
            text: 'medium'
            color: 0,1,0.9411,1
            background_color: 0,0.5019,0.8784,1
            on_press: root.do_level('medium')
        Button:
            text: 'hard'
            color: 0,1,0.9411,1
            background_color: 0,0.5019,0.8784,1
            on_press: root.do_level('hard')
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
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1,0.1
            Label:
                id: plus
                text: 'right: 0'
            Label:
                text:"tap"
            Label:
                id: minus
                text:'wrong: 0'

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1,1
            Label:
                id: letter
                text: "letter"
                bold: True
                font_size: 24
<ScoreBoard>:
    name: 'wynik'
    orientation: 'vertical'
    BoxLayout:
        Label:
            text: root.tekst

''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()