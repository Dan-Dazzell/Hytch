from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Welcome to the Home Screen"))
        self.add_widget(layout)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="This is the Second Screen"))
        self.add_widget(layout)

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()

        # Create the screens
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(SecondScreen(name="second"))

        # Create the navigation drawer
        root = BoxLayout(orientation="horizontal")

        # Create the drawer content
        nav_drawer = MDNavigationDrawer
        nav_drawer.add_widget(self.sm)

        # Add a button to open the drawer
        nav_button = Button(text="Open Navigation Drawer")
        nav_button.bind(on_release=nav_drawer.toggle)

        # Create the drawer menu
        menu = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu.add_widget(Button(text="Home", on_release=self.go_home))
        menu.add_widget(Button(text="Second Screen", on_release=self.go_second))

        nav_drawer.add_widget(menu)

        root.add_widget(nav_button)
        root.add_widget(nav_drawer)

        return root

    def go_home(self, instance):
        self.sm.current = "home"

    def go_second(self, instance):
        self.sm.current = "second"

if __name__ == "__main__":
    MyApp().run()
