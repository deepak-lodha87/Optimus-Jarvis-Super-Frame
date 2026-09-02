import time
import math

class CaptainStrategy:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित है
        self.phase = 1851
        print(f"--- Optimus Jarvis Super-Frame | Phase: {self.phase} ---")
        print("Integrating Strategic Capabilities: Captain America Protocol.")

    # कोड 1: Tactical Battlefield Analysis (रणनीतिक विश्लेषण)
    def analyze_battlefield(self):
        print(f"\n[Code 01: Tactical Analysis - Phase {self.phase}]")
        threats = {"Infantry": 15, "Armored_Vehicle": 2, "Air_Support": 1}
        print(f"Scanning field... Threats detected: {threats}")
        time.sleep(1.2)
        print("Strategy: 'High Ground' advantage prioritized. Flanking route identified.")
        return "Tactical Plan: GENERATED"

    # कोड 2: Shield Trajectory Logic (शिल्ड प्रक्षेपवक्र गणना)
    def calculate_shield_throw(self, distance, angle):
        print(f"\n[Code 02: Shield Trajectory - Phase {self.phase}]")
        # Simple Physics logic for ricochet (Vibranium physics simulation)
        force = distance * math.cos(math.radians(angle))
        print(f"Calculating return path for {distance} meters at {angle} degrees...")
        time.sleep(1.0)
        print(f"Trajectory Optimized. Calculated Impact Force: {force:.2f} Newtons.")
        return "Shield Path: LOCKED"

if __name__ == "__main__":
    strategy = CaptainStrategy()
    
    # दोनों रणनीतिक कोड्स का निष्पादन
    plan = strategy.analyze_battlefield()
    path = strategy.calculate_shield_throw(50, 45)
    
    print(f"\n--- Phase {strategy.phase} Strategy Report ---")
    print(f"Status: {plan} | {path}")
