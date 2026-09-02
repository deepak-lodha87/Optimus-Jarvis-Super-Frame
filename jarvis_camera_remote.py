import os
import time
import subprocess

class VisualIntel:
    def __init__(self):
        self.master = "Deepak"
        self.save_path = "surveillance_capture.jpg"

    def take_photo(self):
        print(f"\n\033[1;31m[ACTION]\033[0m Activating Camera Sensor for {self.master} sir...")
        
        # असली हार्डवेयर कमांड: यह फोन के पीछे वाले कैमरे से फोटो खींचेगा
        # '0' का मतलब है बैक कैमरा
        try:
            os.system(f"termux-camera-photo -c 0 {self.save_path}")
            
            if os.path.exists(self.save_path):
                print(f"\033[1;32m[SUCCESS]\033[0m Image captured and saved as {self.save_path}")
                msg = "Deepak sir, visual intel has been captured. The image is now stored in your local repository."
                os.system(f'termux-tts-speak "{msg}"')
                
                # फोटो को गैलरी में देखने के लिए (वैकल्पिक)
                # os.system(f"termux-open {self.save_path}")
            else:
                print("\033[1;31m[ERROR]\033[0m Camera access failed. Check permissions.")
                
        except Exception as e:
            print(f"Hardware Error: {e}")

if __name__ == "__main__":
    intel = VisualIntel()
    intel.take_photo()
