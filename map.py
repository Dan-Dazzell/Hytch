from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout

class CarButton(ButtonBehavior, Image):
    pass

class Sidebar(MDBoxLayout):
    """Sidebar that slides in/out and closes on swipe."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.4, 1)  # 40% of screen width
        self.pos_hint = {"right": 1}
        self.padding = 20
        self.spacing = 20
        self.md_bg_color = (1, 1, 1, 1)  # White background
        self.x = 1.0 * self.width  # Start off-screen

        # Sidebar contents
        self.add_widget(Label(text="Request a Driver", font_size=20, bold=True))
        request_button = MDRaisedButton(text="Confirm Request", on_release=self.request_driver)
        self.add_widget(request_button)

    def on_touch_move(self, touch):
        """Detect left swipe to close the sidebar."""
        if touch.dx < -20:  # Swiping left
            self.slide_out()
        return super().on_touch_move(touch)

    def slide_in(self):
        """Slide the sidebar in."""
        Animation(x=self.width * 0.6, d=0.3).start(self)

    def slide_out(self):
        """Slide the sidebar out."""
        Animation(x=self.width, d=0.3).start(self)

    def request_driver(self, instance):
        print("Driver request sent!")

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set teal background
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Layout
        layout = FloatLayout()

        # MapView widget
        self.mapview = MapView(zoom=12, lat=17.0608, lon=-61.7964)  # Centered on Antigua
        layout.add_widget(self.mapview)

        # Sidebar
        self.sidebar = Sidebar()
        self.add_widget(self.sidebar)

        # Car button (bottom right)
        img_button = CarButton(
            source="materials/driving_car_button.png",
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={"right": 0.98, "y": 0.1}  # Positioned slightly above the bottom
        )
        img_button.bind(on_press=self.toggle_sidebar)
        layout.add_widget(img_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def toggle_sidebar(self, instance):
        """Slide the sidebar in/out."""
        if self.sidebar.x >= self.width:  # If sidebar is hidden
            self.sidebar.slide_in()
        else:
            self.sidebar.slide_out()
