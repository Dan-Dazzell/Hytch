from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

# Import LoginScreen from the separate file
from login_screen import LoginScreen

class IdentityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            Color(0, 150/255, 136/255, 1)  # Teal background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        # Main layout
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)
        
        # Logo
        self.logo = Image(source='materials/Logo.png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5})
        layout.add_widget(self.logo)
        
        # Welcome text
        welcome_label = MDLabel(text="Welcome to Heytch", halign="center", theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style="H5")
        layout.add_widget(welcome_label)
        
        # Buttons
        login_button = MDRaisedButton(text="Login", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5}, md_bg_color=(1, 1, 1, 1), text_color=(0, 150/255, 136/255, 1))
        signup_button = MDRaisedButton(text="Sign Up", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5}, md_bg_color=(1, 1, 1, 1), text_color=(0, 150/255, 136/255, 1))
        
        # Bind button actions
        login_button.bind(on_release=self.go_to_login)
        
        layout.add_widget(login_button)
        layout.add_widget(signup_button)
        
        self.add_widget(layout)
    
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def go_to_login(self, instance):
        # Navigate to the LoginScreen when the button is pressed
        self.manager.current = 'login_screen'

class IdentityApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light" 
        
        # Create ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(IdentityScreen(name='identity_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))  # Added LoginScreen from login_screen.py
        
        return sm
    

if __name__ == "__main__":
    IdentityApp().run()
