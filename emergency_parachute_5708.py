import time, secrets, gc, math

class EmergencyParachuteDeployment:
    def __init__(self):
        self.epd_id = f"EPD-{secrets.token_hex(4).upper()}"
        self.gravity = 9.81
        self.nodes = [
            (5704, "Free-Fall-Detect", "MONITORING ACCELEROMETER FOR ZERO-G..."),
            (5705, "Altitude-Threshold", "CHECKING MINIMUM DEPLOYMENT HEIGHT..."),
            (5706, "Canopy-Ejection", "FIRING BALLISTIC GAS CARTRIDGE..."),
            (5707, "Descent-Stabilizer", "CONTROLLING AERODYNAMIC DRAG..."),
            (5708, "Logic v354", "EPD-CORE: EMERGENCY DEPLOYMENT ACTIVE.")
        ]

    def calculate_velocity(self, fall_height):
        # Velocity = sqrt(2 * g * h)
        return round(math.sqrt(2 * self.gravity * fall_height), 2)

    def activate_emergency_protocol(self):
        print(f"\033[1;37m--- EMERGENCY-PARACHUTE-DEPLOYMENT ONLINE (ID: {self.epd_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        fall_dist = 500 # meters
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            current_v = self.calculate_velocity(fall_dist)
            print(f"\033[1;{colors[i]}m[VELOCITY:{current_v}m/s | STATUS:FALLING] Phase {p_id}: {title} >> {status}\033[0m")
            
            # Simulate parachute slowing down the fall
            fall_dist -= 100 
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mEPD STATUS: DEPLOYMENT SUCCESSFUL. DESCENT RATE STABILIZED.\033[0m")

if __name__ == "__main__":
    epd = EmergencyParachuteDeployment()
    epd.activate_emergency_protocol()
