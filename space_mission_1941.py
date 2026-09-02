import time
import random

class DeepSpaceOperations:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_separation = 1940
        self.phase_landing = 1941
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Mission Protocols: {self.phase_separation} & {self.phase_landing}")

    # Phase 1940: Multi-Rocket Stage Separation (रॉकेट स्टेज पृथक्करण)
    def execute_stage_separation(self, current_altitude):
        print(f"\n[Code 01: Stage Separation - Phase {self.phase_separation}]")
        print(f"Current Altitude: {current_altitude} km. Monitoring fuel exhaustion...")
        time.sleep(1.5)
        
        if current_altitude > 100:
            print("Action: Initiating explosive bolts. Detaching Booster Stage...")
            time.sleep(1.0)
            print("Status: Separation successful. Vacuum-rated engine ignited.")
            return "Staging: STAGE_02_ACTIVE"
        else:
            print("Status: Main boosters still firing. Maintaining trajectory.")
            return "Staging: STAGE_01_POWERING"

    # Phase 1941: Lunar Landing Stabilization (चंद्रमा पर लैंडिंग)
    def stabilize_lunar_landing(self):
        print(f"\n[Code 02: Lunar Landing - Phase {self.phase_landing}]")
        print("Engaging Doppler Radar for surface altitude check...")
        time.sleep(1.2)
        
        # चंद्रमा के गुरुत्वाकर्षण और लैंडिंग का सिमुलेशन
        tilt_angle = random.uniform(0.0, 5.0)
        print(f"Current Tilt: {tilt_angle:.2f} degrees. Adjusting RCS Thrusters...")
        time.sleep(1.8)
        
        if tilt_angle < 1.0:
            print("Status: Vertical alignment confirmed. Landing legs deployed.")
            print("Result: Touchdown confirmed. Welcome to the Moon.")
            return "Landing: SUCCESSFUL"
        else:
            print("Action: Auto-correction in progress. Leveling descent...")
            return "Landing: IN_PROGRESS"

if __name__ == "__main__":
    space_mission = DeepSpaceOperations()
    
    # दोनों फेजेस का निष्पादन
    sep_report = space_mission.execute_stage_separation(120)
    land_report = space_mission.stabilize_lunar_landing()
    
    print(f"\n--- Mission Milestone Summary ---")
    print(f"Final Report: {sep_report} | {land_report}")
