from kivy.uix.screenmanager import ScreenManager, SlideTransition, NoTransition
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.size_hint = (1, 1)  # Ensure full-screen size
        sm = ScreenManager

        # Logo (Initially hidden)
        self.logo = Image(
            source='materials/Logo.png',
            opacity=0,
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.logo)
        
        # Start animation when the widget is ready
        Clock.schedule_once(self.fade_in_logo, 1)

    def fade_in_logo(self, dt):
        anim_logo = Animation(opacity=1, duration=1)  # Fade-in effect
        anim_logo.start(self.logo)

        # Schedule transition to IdentityScreen after animation
        Clock.schedule_once(self.switch_to_identity, 2)

    def switch_to_identity(self, dt):
        # Set transition to None for instant change
        self.manager.transition = NoTransition()
        self.manager.current = 'identity_screen'
        # Restore the default transition
        self.manager.transition = SlideTransition()
