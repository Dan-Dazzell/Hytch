from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.size_hint = (1, 1)  # Make sure the screen takes full width and height

        # Logo (hidden initially)
        self.logo = Image(source='materials/Logo.png', opacity=0, size_hint=(None, None), size=(dp(200), dp(200)), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.logo)
        
        # Start animation when the widget is ready
        Clock.schedule_once(self.fade_in_logo, 1)
    
    def fade_in_logo(self, dt):
        anim_logo = Animation(opacity=1, duration=1)
        anim_logo.start(self.logo)

class SplashApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        return sm

if __name__ == '__main__':
    SplashApp().run()
