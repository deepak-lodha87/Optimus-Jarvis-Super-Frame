import time

class SubTerraScanner:
    def __init__(self):
        self.mode = "ACTIVE_GPR"
        self.depth_limit = "15 Meters"

    def start_scan(self):
        print(f"\033[1;33m[SCANNING]\033[0m Initiating Sub-Surface Radar Pulse...")
        time.sleep(1.8)
        
        layers = ["Electrical-Grid", "Water-Optics", "Structural-Foundation"]
        for layer in layers:
            print(f" \033[1;32m[DETECTED]\033[0m {layer} mapped successfully.")
            time.sleep(0.7)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the underground scan is \ncomplete. I can now see the hidden veins of \nthe city beneath your feet. Nothing stays \nhidden from our new tactical eye.\033[0m")

if __name__ == "__main__":
    scanner = SubTerraScanner()
    scanner.start_scan()
