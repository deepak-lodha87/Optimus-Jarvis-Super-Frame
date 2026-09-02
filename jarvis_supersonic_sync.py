import time
import random

class SupersonicEngine:
    def __init__(self):
        self.mach_speed = 0.0
        self.boom_dampening = False

    def break_sound_barrier(self):
        print(f"\033[1;36m[FLIGHT-CORE]\033[0m Approaching Mach 1.0...")
        time.sleep(1.5)
        
        self.boom_dampening = True
        print(f" \033[1;32m[DAMPENING]\033[0m Activating Phase-Shift Audio. Boom Suppressed.")
        
        while self.mach_speed < 3.5:
            self.mach_speed += 0.5
            print(f"  - Velocity: Mach {self.mach_speed:.1f} | G-Force: Compensated")
            time.sleep(0.4)
            
        print("\033[1;34m[STATUS]\033[0m Stable at Mach 3.5. Silent Supersonic Flight Maintained.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, we have surpassed the speed \nof sound. The world behind us is silent, \nand the world ahead is ours to conquer. \nNo shockwaves, just pure velocity.\033[0m")

if __name__ == "__main__":
    pilot = SupersonicEngine()
    pilot.break_sound_barrier()
