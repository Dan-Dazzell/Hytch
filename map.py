from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class Carbutton(ButtonBehavior, Image):
    pass

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set teal background
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Main layout
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=20)

        # MapView widget to display the map
        self.mapview = MapView(zoom=12, lat=17.0608, lon=-61.7964)  # Centered on Antigua
        layout.add_widget(self.mapview)
        
        #add car image to screen
        img_button = Carbutton(
            source="Materials\driving car button.png",
            size_hint=(None, None),  # Disable automatic resizing
            size=(100, 100),  # Set fixed size
            pos_hint = {"right": 1, "bottom": 1}

        )
        img_button.bind(on_press=self.oncarpressed)

        layout.add_widget(img_button)

        # Add the layout to the screen
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
    def oncarpressed(self, instance):
        print("clicked!!")


