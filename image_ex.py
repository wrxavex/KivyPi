from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


class RootWidget(BoxLayout):
    pass


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):

        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainApp(App):

    def build(self):
        root = RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        c.add_widget(
            AsyncImage(
                source="https://lh3.googleusercontent.com/xToRFw-mqA18HtizgutV0K1IouakfR8iJ3PW75u-1n1oxbP7hVfBMlgHWIwuUYKKS_s=w300",
                size_hint=(1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}
            )
        )
        root.add_widget(
            AsyncImage(
                    source='https://lh3.googleusercontent.com/C4ObcUQ8eb9ZRVlqJCgODNig0Y0laWmqNFGfg6h1to5GwkmZdQX4M1Lk5dbO1FYBsVA=w300'
            )
        )
        c = CustomLayout()
        c.add_widget(
            AsyncImage(
                source="https://lh4.ggpht.com/wKrDLLmmxjfRG2-E-k5L5BUuHWpCOe4lWRF7oVs1Gzdn5e5yvr8fj-ORTlBF43U47yI=w300",
                size_hint=(1, .5),
                pos_hint={'center_x':.5, 'center_y':.5}
            )
        )
        root.add_widget(c)
        return root

if __name__ == '__main__':
    MainApp().run()