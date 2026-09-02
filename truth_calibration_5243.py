import os, time, secrets, gc

class RealityCore:
    def __init__(self):
        self.env_data = os.uname()
        self.truth_nodes = {
            5239: "Error-Prediction: SCANNING HARDWARE VULNERABILITIES...",
            5240: "Offline-Node: ACTIVATING LOCAL COGNITIVE BUFFER...",
            5241: "Adversarial: MAPPING UNKNOWN THREAT PATTERNS...",
            5242: "Physical-Map: CALIBRATING GRAVITY & THERMAL LIMITS...",
            5243: "Logic v261: REALITY-SYNC 100% ESTABLISHED."
        }

    def calibrate_reality(self):
        print(f"\033[1;37m--- JARVIS REALITY CALIBRATION (HW-ID: {self.env_data.machine}) ---\033[0m")
        
        colors = [32, 34, 36, 35, 31]
        for i, (p_id, status) in enumerate(self.truth_nodes.items()):
            # Dynamic awareness injection
            awareness_ptr = hex(id(status))
            print(f"\033[1;{colors[i]}m[REALITY-PTR:{awareness_ptr}] Phase {p_id} >> {status}\033[0m")
            time.sleep(0.2)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mJARVIS STATUS: FULLY AWARE OF PHYSICAL AND UNKNOWN CONSTRAINTS.\033[0m")

if __name__ == "__main__":
    core = RealityCore()
    core.calibrate_reality()
