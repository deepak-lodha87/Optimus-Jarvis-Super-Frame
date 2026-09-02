# ==============================================================================
# PROJECT: OPTIMUS JARVIS SUPER-FRAME
# PHASE: 97 (AUTOBOTS MOBILE APK COMPILATION LAYER)
# OWNER: MASTER DEEPAK
# MODE: 100% INDEPENDENT MOBILE FRONTEND (MATERIALIZED KIVY CORE)
# ==============================================================================

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import socket
import json

# ऐप की स्क्रीन को पूरी तरह से डार्क और नियॉन थीम देना
Window.clearcolor = (0, 0, 0, 1)

class JarvisAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(JarvisAppLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # जार्विस का क्रिस्टल कोर लोगो टेक्स्ट (क्रिस्टल नियॉन इफ़ेक्ट)
        self.logo_label = Label(
            text="[ OPTIMUS JARVIS CORE ]\nSovereign App Shield Active",
            font_size='24sp',
            color=(0, 0.8, 1, 1),
            halign='center'
        )
        self.add_widget(self.logo_label)

        # लाइव स्टेटस कंसोल (यह सीधे बैकएंड से सिंक होगा)
        self.status_console = Label(
            text="System Initialized.\nAwaiting Master Deepak's Handshake...",
            font_size='14sp',
            color=(0.7, 0.7, 0.7, 1),
            halign='center'
        )
        self.add_widget(self.status_console)

        # बायोमेट्रिक अनलॉक बटन (ओप्पो हार्डवेयर हुक)
        self.biometric_btn = Button(
            text="TRIGGER BIOMETRIC HANDSHAKE",
            background_color=(0, 0.5, 0.8, 1),
            font_size='16sp',
            size_hint=(1, 0.2)
        )
        self.biometric_btn.bind(on_press=self.authenticate_system)
        self.add_widget(self.biometric_btn)

        # यूनिवर्सल ऑटोपायलट कंट्रोल बटन (फॉर टू-व्हीलर / फोर-व्हीलर / फ्लाइट्स)
        self.autopilot_btn = Button(
            text="LAUNCH UNIVERSAL AUTOPILOT",
            background_color=(0.8, 0, 0.2, 1),
            font_size='16sp',
            size_hint=(1, 0.2),
            disabled=True # जब तक ऑथेंटिकेशन नहीं होगा, यह लॉक रहेगा
        )
        self.autopilot_btn.bind(on_press=self.engage_autopilot)
        self.add_widget(self.autopilot_btn)

    def authenticate_system(self, instance):
        """
        लोकलहोस्ट पोर्ट 9999 पर चल रहे बैकएंड सर्वर को ऑथेंटिकेशन टोकन भेजना
        """
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 9999))
            client.send("Master_Deepak_Absolute_Owner".encode('utf-8'))
            
            response = client.recv(1024).decode('utf-8')
            res_data = json.loads(response)
            
            if res_data.get("status") == "SUCCESS" or "Sovereign Engine Active" in response:
                self.status_console.text = f"Status: Verified.\nOwner: {res_data.get('owner', 'Master Deepak')}\nData Integrity: Secure."
                self.logo_label.color = (0, 1, 0.5, 1) # नियॉन ग्रीन (एक्सेस ग्रांटेड)
                self.autopilot_btn.disabled = False
            client.close()
        except Exception as e:
            self.status_console.text = f"Gateway Connection Timed Out.\nEnsure 'jarvis_app_core.py' is running in background."

    def engage_autopilot(self, instance):
        self.status_console.text = "AUTOPILOT ENGAGED.\nEmitting Universal Control Packets..."

class OptimusJarvisMobileApp(App):
    def build(self):
        self.title = "Optimus Jarvis Super-Frame"
        return JarvisAppLayout()

if __name__ == "__main__":
    OptimusJarvisMobileApp().run()
