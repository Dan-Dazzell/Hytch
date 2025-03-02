from kivy.uix.screenmanager import Screen, ScreenManager
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

class CarButton(ButtonBehavior, Image):
    pass

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = FloatLayout()

        self.mapview = MapView(zoom=12, lat=17.0608, lon=-61.7964)
        layout.add_widget(self.mapview)
        
        self.carbutton = CarButton(
            source='Materials/driving car button.png',
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'right': 0.98, 'y': 0.15}
        )
        self.carbutton.bind(on_press=self.carbuttonpressed)
        layout.add_widget(self.carbutton)   

        # Creating the MDNavigationDrawer
        self.navdrawer = MDNavigationDrawer()

        # Content for the drawer
        self.drawercontent = ScrollView()
        self.drawer_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.drawer_layout.bind(minimum_height=self.drawer_layout.setter('height'))

        # Adding buttons to the drawer
        self.drawer_layout.add_widget(MDRaisedButton(text="Book Ride", on_press=self.book_ride_action))
        self.drawer_layout.add_widget(MDRaisedButton(text="Settings", on_press=self.settings_action))
        self.drawer_layout.add_widget(MDRaisedButton(text="Profile", on_press=self.profile_action))

        self.drawercontent.add_widget(self.drawer_layout)
        self.navdrawer.add_widget(self.drawercontent)

        # Main content layout (the map and toolbar)
        self.main_layout = FloatLayout()
        self.main_layout.add_widget(self.navdrawer)

        # Bottom toolbar
        self.toolbar = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.1),  # 10% of screen height
            pos_hint={'x': 0, 'y': 0}
        )

        with self.toolbar.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal color
            self.toolbar_rect = Rectangle(size=self.toolbar.size, pos=self.toolbar.pos)
        self.toolbar.bind(size=self.update_toolbar_rect, pos=self.update_toolbar_rect)

        # Toolbar buttons
        self.toolbar.add_widget(Button(text="Home", on_press=self.home_action))
        self.toolbar.add_widget(Button(text="Search", on_press=self.search_action))
        self.toolbar.add_widget(Button(text="Profile", on_press=self.profile_action))

        layout.add_widget(self.toolbar)
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
    def book_ride_action(self, instance):
        print("Book Ride button clicked")

    def settings_action(self, instance):
        print("Settings button clicked")

    def update_toolbar_rect(self, *args):
        self.toolbar_rect.size = self.toolbar.size
        self.toolbar_rect.pos = self.toolbar.pos

    def home_action(self, instance):
        print("Home button clicked")

    def search_action(self, instance):
        print("Search button clicked")

    def profile_action(self, instance):
        print("Profile button clicked")
        
    def carbuttonpressed(self, instance):
        print("I love Shanik")
        self.navdrawer.set_state('open')

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Map(name='map'))
        return sm

if __name__ == '__main__':
    MyApp().run()
