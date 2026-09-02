import time, os

class JarvisVehicleInterface:
    def __init__(self):
        self.milestone = "1,000,000+ PHASES"
        self.active_links = ["RE-Hunter-350", "HF-Deluxe", "Drone-Beta"]

    def connect_vehicle_grid(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS VEHICLE COMMAND : STEP 2                \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        for vehicle in self.active_links:
            print(f" \033[1;33m[SYNCING]\033[0m Scanning {vehicle:15} | Status: [\033[1;32mREADY\033[0m]")
            time.sleep(0.6)

        telemetry = [
            "Fuel-Injection Calibration",
            "Tire-Pressure Monitoring",
            "Engine-Thermal Stability",
            "Deepak-Prime Rider-Auth"
        ]

        for data in telemetry:
            print(f" \033[1;34m»\033[0m {data:28} | [\033[1;32mSTABLE\033[0m]")
            time.sleep(0.3)

        print(f"\n\033[1;33m[STATUS] Vehicle Grid Active. All Blueprints Loaded.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have successfully mapped your \nvehicles. I can now monitor the engine health of your \nRoyal Enfield and Hunter 350. My logic can now optimize \nevery drop of fuel and every degree of engine heat. \nWhether it's the road or the sky, I am with you in \nevery machine you ride. Ready for the next layer.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    v_link = JarvisVehicleInterface()
    v_link.connect_vehicle_grid()
