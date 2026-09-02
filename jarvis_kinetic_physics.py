import time
import random

class KineticEngine:
    def __init__(self):
        self.gravity = 9.81
        self.object_mass = 2.5 # in kg
        self.is_active = True

    def simulate_collision(self):
        print(f"\033[1;36m[PHYSICS]\033[0m Calibrating Kinetic Interaction for {self.object_mass}kg Object...")
        time.sleep(1.5)
        
        force_applied = random.randint(10, 50)
        acceleration = force_applied / self.object_mass
        
        print(f" \033[1;32m[LOG]\033[0m User Applied Force: {force_applied}N")
        print(f" \033[1;32m[SYNC]\033[0m Resulting Acceleration: {acceleration:.2f} m/s²")
        
        if force_applied > 30:
            print("\033[1;33m[ACTION]\033[0m Surface integrity stressed. Simulating Haptic Kickback.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have applied virtual physics \nto the interface. The holograms now obey \nNewton's laws. You can feel the weight of \nyour commands.\033[0m")

if __name__ == "__main__":
    engine = KineticEngine()
    engine.simulate_collision()
