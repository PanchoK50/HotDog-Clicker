import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation, AnimationTransition
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
import random
import pickle
from kivy.core.window import Window
Window.size = (480, 640)


class SplashScreen(Screen):
    btn = ObjectProperty(None)

    def print(self):
        print("1")

    def btnprint(self):
        print("Button pressed")


class HomeScreen(Screen):
    pass


class ShopWindow(Screen):
    pass


class MembersScreen(Screen):
    pass


class CabezaScreen(Screen):
    doggis = ObjectProperty(None)
    counter = ObjectProperty(None)
    champ = ObjectProperty(None)
    state = 0
    no = ""
    cm_de_completo = ""
    champ_selector_variable = 0

    def changeChamp(self):
        self.champ_selector_variable += 1
        self.champ_selector = self.champ_selector_variable % 4
        print(self.champ_selector)


        if self.champ_selector == 0:
            self.champ.background_normal= "ShaggyNormal.png"
            self.champ.background_down = "ShaggyNormal.png"

        elif self.champ_selector == 1:
            self.champ.background_normal = "Shaggy.png"
            self.champ.background_down = "Shaggy.png"

        elif self.champ_selector == 3:
            self.champ.background_normal = "ScoobyDoo.png"
            self.champ.background_down = "ScoobyDoo.png"

        elif self.champ_selector == 2:
            self.champ.background_normal = "ScoobyDooNormal.png"
            self.champ.background_down = "ScoobyDooNormal.png"






    def getProgress(self):
        try:
            progress = int(pickle.load(open("saveprogress.dat", "rb")))
            print(self.no)
            return int(progress)
        except EOFError:
            return int(0)


    def setProgress(self):
        dogs = self.no
        f = open("saveprogress.dat", "wb")
        pickle.dump(dogs, f)
        f.close()



    def eatDoggis(self):
        self.no = self.getProgress()
        self.counter.text = str(self.no)
        self.state += 1
        self.cm_de_completo = self.state%3
        if self.cm_de_completo%4 == 0 and self.cm_de_completo%4 != 1:
            self.doggis.background_normal = "DoggisCompleto.png"
            self.doggis.background_down = "DoggisCompleto.png"
            self.no += 1
            self.setProgress()
            self.counter.text = str(self.no)
        elif self.cm_de_completo == 1:
            self.doggis.background_normal = "DoggisCompleto1.png"
            self.doggis.background_down = "DoggisCompleto1.png"
        elif self.cm_de_completo == 2:
            self.doggis.background_normal = "DoggisCompleto2.png"
            self.doggis.background_down = "DoggisCompleto2.png"



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("ownown.kv")


class OwnApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    OwnApp().run()
