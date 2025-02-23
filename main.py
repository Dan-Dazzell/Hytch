from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDLabel:
        text: "Hello, KivyMD!"
        halign: "center"
        theme_text_color: "Primary"

    MDRaisedButton:
        text: "Click Me"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_press: app.on_button_click()
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_button_click(self):
        print("Button clicked!")

MyApp().run()
