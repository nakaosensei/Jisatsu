from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import connectionSqlite as cone
import time
import os
import planilha
#import sincronizador

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class CustomPopup(Popup):
    print ("Requisitos nao foram atendidos")

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    #text_input = ObjectProperty(None)

    
    def sincronizar(self):
  

        
        ##sync(self.text_input)

        pass




    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
        
        planilh = planilha.Planilha()
        cam = (filename[0])
        print(cam)

        p = planilh.openPlantsXls(cam)
        print(p)
        self.text_input = p
        print(self.text_input)
        

        self.dismiss_popup()
        

    #def floratpl(self, path,filename)
    
    def nomesvalidos(self):
        PLa = cone.DAOPlant()
        if PLa.tableIsEmpty() == False:
            print("tplplanilha")
            #gera planilha das ocorrencias do species
        else:
            
            content = Label(text='Os requisitos para essa execução não foram atendidos. É necessário sincronizar.')
            self._popup = Popup(title="Erro", content=content,size_hint=(0.9, 0.9))
            self._popup.open()
            Clock.schedule_once(self.dismiss_popup, 4)


    def speciesl(self):
        daoOcurrenc = cone.DAOOcurrence()
        if daoOcurrenc.tableIsEmpty() == False:
            print("species")
            #gera planilha das ocorrencias do species
            pass
        else:
            
            content = Label(text='Os requisitos para essa execução não foram atendidos. É necessário sincronizar.')
            self._popup = Popup(title="Erro", content=content,size_hint=(0.9, 0.9))
            self._popup.open()


            Clock.schedule_once(self.dismiss_popup, 4)
            pass
    
    def tplplanilha(self):
        tplPL = cone.DAOPlant()
        if tplPL.tableIsEmpty() == False:
            print("tplplanilha")
            #gera planilha das ocorrencias do species
            pass
        else:
            
            content = Label(text='Os requisitos para essa execução não foram atendidos. É necessário sincronizar.')
            self._popup = Popup(title="Erro", content=content,size_hint=(0.9, 0.9))
            self._popup.open()


            Clock.schedule_once(self.dismiss_popup, 4)
            pass




    def florxtpl(self):
        flora = cone.DAOPlant()
        species = cone.DAOOcurrence()
        if ((flora.tableIsEmpty() == False) and (species.tableIsEmpty() == False)):
            print("nada vazio, tudo certo")
        else:
            content = Label(text='Os requisitos para essa execução não foram atendidos. É necessário sincronizar.')
            self._popup = Popup(title="Erro", content=content,size_hint=(0.9, 0.9))
            self._popup.open()


            Clock.schedule_once(self.dismiss_popup, 4)

    def wait(self):
        time.sleep(10)
        self.dismiss_popup()

        
class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    Editor().run()