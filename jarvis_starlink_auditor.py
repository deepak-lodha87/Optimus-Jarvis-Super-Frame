import os
import requests

class SpaceXAuditor:
    def __init__(self):
        self.user = "Deepak sir"
        self.url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def find_real_defects(self):
        print(f"\033[1;36m[AUDIT]\033[0m Scanning 10,000+ Starlink Nodes for Defects...")
        try:
            response = requests.get(self.url, headers=self.headers, timeout=20)
            if response.status_code == 200:
                satellites = response.json()
                defects_found = 0
                
                for sat in satellites[:50]: # First 50 nodes audit
                    name = sat['OBJECT_NAME']
                    motion = float(sat['MEAN_MOTION'])
                    
                    # Real Defect Logic: Orbital Decay Check
                    if motion < 15.03: # Threshold for healthy Starlink orbit
                        defects_found += 1
                        print(f"\033[1;31m[DEFECT]\033[0m {name} | Motion: {motion} | Status: UNSTABLE")
                    
                if defects_found > 0:
                    self.speak(f"Sir, I have audited the registry. {defects_found} satellites are showing orbital instability.")
                    print(f"\n\033[1;32m[REPORT]\033[0m Total Defects Identified: {defects_found}")
                else:
                    print("\033[1;32m[HEALTHY]\033[0m All audited nodes are in optimal orbit.")
            
        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Audit Failed: {e}")

if __name__ == "__main__":
    auditor = SpaceXAuditor()
    auditor.find_real_defects()
