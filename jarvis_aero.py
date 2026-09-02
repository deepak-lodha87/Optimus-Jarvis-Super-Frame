import time

class AeroControl:
    def __init__(self):
        self.wing_angle = 0  # degrees
        self.drag_coefficient = 0.35

    def adjust_wings(self, speed):
        print(f"\033[1;34m[AERO] Current Velocity: {speed} km/h. Analyzing Airflow...\033[0m")
        time.sleep(1)
        
        if speed > 150:
            self.wing_angle = 15
            self.drag_coefficient = 0.28
            print("\033[1;33m[ACTION] Deploying Active Downforce. Wing Angle: 15°\033[0m")
        else:
            self.wing_angle = 5
            print("\033[1;32m[ACTION] Low-Drag Mode Active. Wing Angle: 5°\033[0m")
        
        return f"Current Drag Coeff: {self.drag_coefficient}"

if __name__ == "__main__":
    aero = AeroControl()
    print("-" * 50)
    print("   JARVIS ACTIVE AERODYNAMICS (P3193)")
    print("-" * 50)
    # High speed test
    print(aero.adjust_wings(180))
    print("-" * 50)
