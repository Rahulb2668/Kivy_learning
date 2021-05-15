import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]  # [R,G,B, alpha]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class HboxlayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = "Button #%s"%(i+1),
                         background_color = random.choice(colors)
                         )
            layout.add_widget(btn)
            btn.bind(on_press=self.on_pressed_me)
        return layout


    def on_pressed_me(self, instance):
        print('Pressed me')



if __name__ == "__main__":
    app = HboxlayoutExample()
    app.run()