from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation

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

        self.sidebar = BoxLayout(
            orientation='vertical',
            size_hint=(0.6, 1),  # Sidebar width = 60% of screen
            pos_hint={'right': 2},  # Start off-screen
            padding=20,
            spacing=10
        )
        self.sidebar.add_widget(Label(text="Hello, World!", font_size=24, color=(1,1,1,1)))

        layout.add_widget(self.sidebar)

        self.img_button = CarButton(
            source="Materials/driving car button.png",
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={"right": 0.98, "y": 0.05}
        )
        self.img_button.bind(on_press=self.toggle_sidebar)
        layout.add_widget(self.img_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def toggle_sidebar(self, instance):
        target_x = 0.4 if self.sidebar.pos_hint['right'] == 2 else 2  # Slide in or out
        Animation(pos_hint={'right': target_x}, duration=0.3).start(self.sidebar)
        
        
