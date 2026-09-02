import time, secrets, gc, cmath, math

class ElectromagneticGrapple:
    def __init__(self):
        self.egh_id = f"EGH-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5694, "Tether-Launch", "CALCULATING BALLISTIC TRAJECTORY..."),
            (5695, "Polarity-Sync", "ADJUSTING MAGNETIC FLUX FOR ATTACHMENT..."),
            (5696, "Winch-Control", "ENGAGING HIGH-TORQUE RETRACTION..."),
            (5697, "Quick-Release", "PREPARING EMERGENCY DETACHMENT..."),
            (5698, "Logic v352", "EGH-CORE: GRAPPLING SYSTEM READY.")
        ]

    def calculate_vector(self, distance, angle_deg):
        # Unique logic: Using complex numbers to find X,Y coordinates
        angle_rad = math.radians(angle_deg)
        vector = cmath.rect(distance, angle_rad)
        return round(vector.real, 2), round(vector.imag, 2)

    def activate_grapple(self):
        print(f"\033[1;37m--- ELECTROMAGNETIC-GRAPPLING-HOOK ONLINE (ID: {self.egh_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        target_dist = 45.0 # meters
        target_angle = 35.0 # degrees
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            x, y = self.calculate_vector(target_dist, target_angle)
            print(f"\033[1;{colors[i]}m[VECTOR:({x}m, {y}m) | TENSION:LOW] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mEGH STATUS: TARGET REACHED. TETHER ANCHORED SUCCESSFULLY.\033[0m")

if __name__ == "__main__":
    egh = ElectromagneticGrapple()
    egh.activate_grapple()
