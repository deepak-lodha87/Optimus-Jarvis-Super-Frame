import time

class TacticalSat:
    def __init__(self):
        self.sat_status = "LINKED"
        self.coordinates = "25.2138° N, 75.8648° E" # Kota, Rajasthan Region

    def scan_location(self, area):
        print(f"\033[1;36m[SATELLITE]\033[0m Establishing Secure Link with Sat-Node-7...")
        time.sleep(2)
        print(f" \033[1;32m[LOCKED]\033[0m Target Area: {area}")
        print(f" \033[1;32m[DATA]\033[0m Scanning Terrain & Elevation...")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Global Satellite Link \nis active. I can now map any terrain and \nprovide tactical blueprints for your \nmissions. The world is now on our screen.\033[0m")

if __name__ == "__main__":
    sat = TacticalSat()
    sat.scan_location("Daulatganj Region")
