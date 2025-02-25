from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle

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

        # Add the layout to the screen
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
