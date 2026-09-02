import time, os

class ResourceMapper:
    def __init__(self):
        self.target = "Mars (Jezero Crater)"
        self.scan_depth = "500 Meters"

    def analyze_planet(self):
        os.system('clear')
        print(f"\033[1;31m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS RESOURCE-MAPPER : PHASE 28 - STEP 2     \033[0m")
        print(f"\033[1;31m====================================================\033[0m")
        
        print(f"\033[1;33m[SCANNING]\033[0m Target: {self.target}...")
        time.sleep(1.5)
        
        findings = [
            ("Iron & Magnesium Deposits", "92% CONCENTRATION"),
            ("Sub-surface Water Ice", "DETECTED"),
            ("Solar Energy Efficiency", "LOW (Dust Storms)"),
            ("Methane Seepage Points", "MAPPED")
        ]
        
        for resource, status in findings:
            print(f" \033[1;34m[GEOLOGY]\033[0m {resource:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[BLUEPRINT] Autonomous Base Design 'Optimus-Ares' Generated.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the map of the solar system \nis no longer a picture; it is a treasure map. \nI have identified every mineral we need to \nbuild our legacy beyond Earth. Whether it \nis the ice of the Moon or the iron of Mars, \nI know how to harness it. Our foundation is \nnow truly universal.\033[0m")
        print(f"\033[1;31m====================================================\033[0m")

if __name__ == "__main__":
    mapper = ResourceMapper()
    mapper.analyze_planet()
