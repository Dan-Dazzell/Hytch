from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, Rectangle

class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set a teal background color
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Main layout
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)

        # Title
        title = MDLabel(text="Sign Up", halign="center", theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style="H4")
        layout.add_widget(title)

        # Username Field
        self.username = MDTextField(
            hint_text="Username", size_hint=(None, None), size=(300, 50), 
            pos_hint={'center_x': 0.5}, mode="rectangle", multiline=False
        )
        layout.add_widget(self.username)

        # Password Field
        self.password = MDTextField(
            hint_text="Password", size_hint=(None, None), size=(300, 50), 
            pos_hint={'center_x': 0.5}, mode="rectangle", multiline=False, password=True
        )
        layout.add_widget(self.password)

        # Confirm Password Field
        self.confirm_password = MDTextField(
            hint_text="Confirm Password", size_hint=(None, None), size=(300, 50), 
            pos_hint={'center_x': 0.5}, mode="rectangle", multiline=False, password=True
        )
        layout.add_widget(self.confirm_password)

        # Sign Up Button (Navigates to map.py)
        signup_button = MDRaisedButton(
            text="Sign Up", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5},
            md_bg_color=(1, 1, 1, 1), text_color=(0, 150/255, 136/255, 1)
        )
        signup_button.bind(on_press=self.navigate_to_map)  # Bind button to navigation method
        layout.add_widget(signup_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def navigate_to_map(self, instance):
        # Regardless of the entered info, navigate to the Map screen
        self.manager.current = 'map_screen'
