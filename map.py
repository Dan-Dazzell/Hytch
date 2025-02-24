from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)
        
        # Login page content (just a simple label for now)
        map_label = MDLabel(text="Beat your ass and hide the bible if God watching", halign="center", font_style="H4")
        layout.add_widget(map_label)
        
        self.add_widget(layout)
