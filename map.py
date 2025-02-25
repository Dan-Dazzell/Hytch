from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout  # Allows positioning anywhere

class CarButton(ButtonBehavior, Image):
    pass

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set teal background
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Use FloatLayout to position elements freely
        layout = FloatLayout()

        # MapView widget to display the map
        self.mapview = MapView(zoom=12, lat=17.0608, lon=-61.7964)  # Centered on Antigua
        layout.add_widget(self.mapview)
        
        # Add car image button to screen
        img_button = CarButton(
            source="Materials/driving car button.png",  # Fixed file path
            size_hint=(None, None),  
            size=(100, 100),
            pos_hint={"right": 0.98, "y": 0.05}  # Adjusted position
        )
        img_button.bind(on_press=self.on_car_pressed)

        # Add button on top of the map
        layout.add_widget(img_button)

        # Add layout to screen
        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
    def on_car_pressed(self, instance):
        print("Car button clicked!!")
