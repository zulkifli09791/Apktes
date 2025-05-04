from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

pages = [
    {"image": "images/foto1.jpg", "caption": "Keluarga di taman"},
    {"image": "images/foto2.jpg", "caption": "Liburan ke pantai"},
    {"image": "images/foto3.jpg", "caption": "Ulang tahun ibu"},
]

class PageScreen(Screen):
    def __init__(self, page_data, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Image(source=page_data["image"], allow_stretch=True))
        layout.add_widget(Label(text=page_data["caption"], size_hint_y=0.1))
        self.add_widget(layout)

class BookApp(App):
    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())
        for i, page in enumerate(pages):
            screen = PageScreen(name=f"page{i}", page_data=page)
            self.sm.add_widget(screen)
        self.sm.current = "page0"

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.sm)

        nav = BoxLayout(size_hint_y=0.1)
        nav.add_widget(Button(text="Sebelumnya", on_press=self.prev_page))
        nav.add_widget(Button(text="Berikutnya", on_press=self.next_page))
        root.add_widget(nav)

        return root

    def next_page(self, instance):
        index = int(self.sm.current.replace("page", ""))
        if index < len(pages) - 1:
            self.sm.current = f"page{index + 1}"

    def prev_page(self, instance):
        index = int(self.sm.current.replace("page", ""))
        if index > 0:
            self.sm.current = f"page{index - 1}"

BookApp().run()