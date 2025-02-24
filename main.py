from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.app import MDApp
from splashscreen import SplashScreen
from identity import IdentityScreen
from login_screen import LoginScreen
from map import Map

class IdentityApp(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(SplashScreen(name='splash_screen'))
        sm.add_widget(IdentityScreen(name='identity_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(Map(name='map_screen'))

        sm.current = 'splash_screen'  # Start with the splash screen
        return sm

if __name__ == "__main__":
    IdentityApp().run()
