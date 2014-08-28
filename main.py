
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty, ObjectProperty,NumericProperty

import time
import random



def get_spells():
    s = {}
    with open('./spells.txt','r') as f:
        keys = f.readline().rstrip().split(';')
        for line in f:
            split = line.rstrip().split(';')
            v = dict(zip(keys,split))
            s[split[0]] = v

    
    return s

class MenuBox(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['size_hint_y'] = 0.1
        super(MenuBox, self).__init__(**kwargs)

        search_screen_button = Button(text='Search Screen', id = 'search_screen')
        search_screen_button.bind(on_release = self.menu_button_press)
        self.add_widget(search_screen_button)

        view_list_button = Button(text='View List Screen', id = 'view_list_screen')
        view_list_button.bind(on_release = self.menu_button_press)
        self.add_widget(view_list_button)

        view_spell_button = Button(text='View Spell Screen', id = 'view_spell_screen')
        view_spell_button.bind(on_release = self.menu_button_press)
        self.add_widget(view_spell_button)
    
    def menu_button_press(self,obj):
        App.get_running_app().root.menu_to_screen(obj.id)
        

        

class MyScreen(Screen):
    def __init__(self, **kwargs):
        
        super(MyScreen, self).__init__(**kwargs)
        self.screen_box = BoxLayout(orientation= 'vertical')
        self.mb = MenuBox()
        self.const = 2
        self.screen_box.add_widget(self.mb)


        self.content_box = BoxLayout(size_hint_y=0.9)
        self.screen_box.add_widget(self.content_box)
        self.add_widget(self.screen_box)


        
#############################

class SearchScreen(MyScreen):
    def __init__(self, **kwargs):
        
        super(SearchScreen, self).__init__(**kwargs)
        l = Label(text='Initialized')
        self.content_box.add_widget(l)
        
        
    
    def prepare_yourself(self):
        print 'foo!1'


class ViewListScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ViewListScreen, self).__init__(**kwargs)
        self.sv = ScrollView()
        self.content_box.add_widget(self.sv)
    
    def prepare_yourself(self):
        
        list_grid = GridLayout(cols = 1,
                                size_hint_y = None,
                                orientation = 'vertical')
        c_list = App.get_running_app().root.current_list
        list_grid.height = len(c_list)*40 #HARDCODE
        for k in c_list:
            b = Button(
                text = k,
                size_hint_y = None,
                height = 40
                )
            # b.bind(on_release=b.show_position(self.id))
            list_grid.add_widget(b)
        
        print 
        self.sv.clear_widgets()
        self.sv.add_widget(list_grid)



class ViewSpellScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ViewSpellScreen, self).__init__(**kwargs)
    
    def prepare_yourself(self):
        print 'foo!2'


############################


    


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        
        super(MyScreenManager, self).__init__(**kwargs)
        self.SPELLS = get_spells()
        self.current_list = sorted(self.SPELLS.keys())
        self.current_position = 0

    def menu_to_screen(self,name):
        self.get_screen(name).prepare_yourself()
        self.current = name
    
    
        


        

    

   
        




class MyApp(App):
    def build(self):


        sm = MyScreenManager()

        ss = SearchScreen(name='search_screen')
        sm.add_widget(ss)

        vls = ViewListScreen(name='view_list_screen')
        sm.add_widget(vls)

        vss = ViewSpellScreen(name='view_spell_screen')
        
        sm.add_widget(vss)
        return sm

MyApp().run()
