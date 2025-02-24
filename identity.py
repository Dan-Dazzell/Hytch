from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, Rectangle

class IdentityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set a teal background color
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Main layout
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)

        # Welcome Text
        welcome_label = MDLabel(
            text="Welcome to Heytch", halign="center", theme_text_color="Custom", 
            text_color=(1, 1, 1, 1), font_style="H4"
        )
        layout.add_widget(welcome_label)

        # Login Button
        login_button = MDRaisedButton(
            text="Login", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5},
            md_bg_color=(1, 1, 1, 1), text_color=(0, 150/255, 136/255, 1)
        )
        login_button.bind(on_press=self.navigate_to_login)  # Bind to login navigation method
        layout.add_widget(login_button)

        # Sign Up Button
        signup_button = MDRaisedButton(
            text="Sign Up", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5},
            md_bg_color=(1, 1, 1, 1), text_color=(0, 150/255, 136/255, 1)
        )
        signup_button.bind(on_press=self.navigate_to_signup)  # Bind to signup navigation method
        layout.add_widget(signup_button)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def navigate_to_login(self, instance):
        # Navigate to the login screen
        self.manager.current = 'login_screen'

    def navigate_to_signup(self, instance):
        # Navigate to the signup screen
        self.manager.current = 'signup_screen'
