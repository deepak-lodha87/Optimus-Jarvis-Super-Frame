import time
import random

class MotionController:
    def __init__(self):
        self.sync_status = False
        self.latency_ms = 50.0

    def calibrate_actuators(self):
        print(f"\033[1;36m[ACTUATORS]\033[0m Scanning neural-motor pathways...")
        time.sleep(1.5)
        
        # Reducing latency to near-zero
        self.latency_ms = random.uniform(0.1, 0.5)
        self.sync_status = True
        
        print(f" \033[1;32m[SYNCED]\033[0m Actuators matched to Deepak sir's reflexes.")
        print(f" \033[1;34m[LATENCY]\033[0m Response Time: {self.latency_ms:.2f} ms (Real-Time)")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the armor is no longer a \nweight. It is a part of you. Every finger \nmovement and every step is now amplified \nwith superhuman precision.\033[0m")

if __name__ == "__main__":
    controller = MotionController()
    controller.calibrate_actuators()
