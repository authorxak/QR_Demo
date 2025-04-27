# -Zero-
import os
import qrcode
import random
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window

Window.clearcolor = (0.2, 0.2, 0.2, 1)

KV = """
Manager:
    StartPage:
    FirstPage:
    SecondPage:

<StartPage>:
    name: "start"
    MDFloatLayout:
        md_bg_color: app.theme_cls.bg_normal

        MDCard:
            size_hint: 0.85, 0.7
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: [30, 40, 30, 20]
            spacing: 25
            orientation: "vertical"
            radius: [25,]
            MDLabel:
                text: "QR Code Solutions"
                font_style: "Subtitle1"
                halign: "center"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            MDIconButton:
                icon: "qrcode-scan"
                icon_size: "64sp"
                pos_hint: {"center_x": 0.5}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            BoxLayout:
                orientation: "vertical"
                spacing: 20
                size_hint_y: 0.6

                MDRaisedButton:
                    text: "Text to QR"
                    icon: "text-box-outline"
                    size_hint: 0.8, None
                    height: "50dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: app.theme_cls.primary_color
                    on_release: 
                        app.root.current = "Text"
                        app.root.transition.direction = "left"

                MDRaisedButton:
                    text: "Image to QR"
                    icon: "image-outline"
                    size_hint: 0.8, None
                    height: "50dp"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: app.theme_cls.primary_color
                    on_release: 
                        app.root.current = "Image"
                        app.root.transition.direction = "left"

            MDLabel:
                text: "© 2025 CyberQurt Team"
                font_style: "Caption"
                halign: "center"
                theme_text_color: "Hint"
                size_hint_y: None
                height: self.texture_size[1]
<FirstPage>:
    name: "Text"
    MDRelativeLayout:
        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            Image:
                id: qr_image
                size_hint: None, None
                size: 200, 200
                pos_hint: {'center_x': 0.5}
                source: ""
                opacity: 0  # Изначально скрыто

            MDTextField:
                id: text_input
                size_hint_x: 1
                size_hint_y: None
                height: "48dp"
                hint_text: "Enter text for QR code"
                multiline: False

            MDRaisedButton:
                text: "Generate QR Code"
                size_hint_x: 0.6
                size_hint_y: None
                height: "48dp"
                pos_hint: {'center_x': 0.5}
                on_release: root.generate_qr_code(text_input.text)


<SecondPage>:
    name: "Image"
    MDFloatLayout:
        md_bg_color: app.theme_cls.bg_normal

        MDCard:
            size_hint: 0.8, 0.6
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 10
            padding: 40
            spacing: 30
            orientation: "vertical"
            radius: [25,]

            MDLabel:
                text: "Image to QR"
                font_style: "H4"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]

            MDIcon:
                icon: "image-outline"
                font_size: "64sp"
                halign: "center"
                theme_text_color: "Secondary"

            MDRaisedButton:
                text: "Coming Soon"
                size_hint: 0.6, None
                height: "48dp"
                pos_hint: {"center_x": 0.5}
                md_bg_color: app.theme_cls.primary_color
                disabled: True

            MDLabel:
                text: "This feature will be available in the next update"
                font_style: "Body2"
                halign: "center"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
"""


class StartPage(Screen):
    pass


class FirstPage(Screen):
    def generate_qr_code(self, text):
        if text:
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=5,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            filename = f"temp_qr_{random.randint(0, 999)}.png"
            img.save(filename)
            qr_image = self.ids.qr_image
            qr_image.source = filename
            qr_image.opacity = 1
            qr_image.size = (200, 200)
            os.remove(filename)
            self.ids.text_input.text = ""


class SecondPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=4,
        )


class Manager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.title = "QR Code Demo"
        self.root = Builder.load_string(KV)


if __name__ == '__main__':
    MyApp().run()

