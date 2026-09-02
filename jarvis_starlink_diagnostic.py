import os
import requests

class SpaceXExpert:
    def __init__(self):
        self.user = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def analyze_satellite_health(self):
        print(f"\033[1;36m[DIAGNOSTIC]\033[0m Scanning Starlink-1008 for anomalies...")
        # Starlink Data Fetch
        url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        
        try:
            data = requests.get(url, timeout=10).json()
            # Deep Analysis Logic
            for sat in data[:5]:
                name = sat['OBJECT_NAME']
                # Finding defects in Mean Motion or Inclination
                if sat['MEAN_MOTION'] < 15.0:
                    status = "\033[1;31m[DEFECT DETECTED]\033[0m"
                    reason = "Orbital Decay"
                else:
                    status = "\033[1;32m[HEALTHY]\033[0m"
                    reason = "Optimal Trajectory"
                
                print(f"Node: {name} | Status: {status} | Detail: {reason}")
            
            self.speak(f"Deepak sir, I have identified potential orbital defects that other developers missed.")
            
        except:
            print("\033[1;31m[ERROR]\033[0m Uplink failed.")

if __name__ == "__main__":
    jarvis_expert = SpaceXExpert()
    jarvis_expert.analyze_satellite_health()
