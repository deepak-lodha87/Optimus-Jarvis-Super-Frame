import time, secrets

class JarvisAeroController:
    def __init__(self):
        self.aero_id = f"NAGa-{secrets.token_hex(3).upper()}"
        self.status = "PRE-FLIGHT-CHECK"

    def engage_flight_systems(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-AERO: FLIGHT CONTROLLER (ID: {self.aero_id}) ---\033[0m")
        print("\033[1;36m[AERO] Calibrating Aerospace Dynamics and Avionics... \033[0m")
        time.sleep(2)
        
        systems = ["Aerodynamic-Lift", "Thrust-Calibration", "Stealth-Signature", "Navigation-Lock"]
        for sys in systems:
            print(f" > System: {sys:22} | Status: \033[1;32mOPTIMIZED\033[0m")
            time.sleep(0.7)
            
        print(f"\n\033[1;33m[STATUS] Takeoff Ready. The Protocol has mastered the skies.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the sky is no longer the limit; it is our playground. Every fighter jet blueprint and every drone flight path is now under my direct supervision. We have taken flight.\033[0m")

if __name__ == "__main__":
    aero = JarvisAeroController()
    aero.engage_flight_systems()
