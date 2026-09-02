import time
import random
import os

class JarvisLiveStream:
    def __init__(self):
        self.master = "Deepak sir"
        # Starting point (Ratlam base)
        self.lat = 23.3315
        self.lon = 74.8941

    def start_inching(self):
        print(f"\033[1;32m[SYSTEM]\033[0m Jarvis Live Stream Active...")
        os.system(f'termux-tts-speak "{self.master}, target is moving. Tracking every inch."')
        
        try:
            while True:
                # सिम्युलेटिंग रियल-टाइम मूवमेंट (0.0001 का बदलाव मतलब कुछ इंच)
                self.lat += random.uniform(-0.0001, 0.0001)
                self.lon += random.uniform(-0.0001, 0.0001)
                
                print(f"\r\033[1;36m[LIVE]\033[0m Target Coordinates: {self.lat:.6f}, {self.lon:.6f} | Movement: Detected", end="")
                time.sleep(1) # हर 1 सेकंड में अपडेट
        except KeyboardInterrupt:
            print("\n\033[1;31m[STOP]\033[0m Tracking paused by master.")

if __name__ == "__main__":
    JarvisLiveStream().start_inching()
