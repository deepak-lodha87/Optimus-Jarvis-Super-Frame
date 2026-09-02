import time
import random

class ResourceScanner:
    def __init__(self):
        self.scanning_depth = "5.0 KM"
        self.found_deposits = []

    def initiate_deep_scan(self):
        print(f"\033[1;36m[SCANNER]\033[0m Activating Magnetotelluric Array...")
        time.sleep(2)
        
        resources = ["Lithium Ore", "Geothermal Pocket", "Gold Vein", "Freshwater Aquifer"]
        discovery = random.choice(resources)
        confidence = random.uniform(88.5, 99.2)
        
        print(f" \033[1;32m[DISCOVERY]\033[0m Found: {discovery}")
        print(f" \033[1;32m[CONFIDENCE]\033[0m Analysis Match: {confidence:.2f}%")
        
        if "Lithium" in discovery or "Energy" in discovery:
            print(f"\033[1;34m[OPTIMUS-LINK]\033[0m Resource compatible with our Energy Phase. Marking Coordinates.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Earth is no longer hiding \nits secrets from us. I have identified a \n{discovery} deposit below. We now have the \nkey to unlimited resources.\033[0m")

if __name__ == "__main__":
    scanner = ResourceScanner()
    scanner.initiate_deep_scan()
