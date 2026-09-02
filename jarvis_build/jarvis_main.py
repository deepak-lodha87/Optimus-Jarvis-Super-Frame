from kivy.app import App
from kivy.uix.label import Label
import jarvis_p340_master_core # Aapka main logic
import jarvis_p343_ar_frame    # AR/Camera logic

class OptimusJarvisApp(App):
    def build(self):
        # Yahan saare modules initialize honge
        return Label(text='Optimus Jarvis Super-Frame: Master Core Loaded')

if __name__ == '__main__':
    OptimusJarvisApp().run()
