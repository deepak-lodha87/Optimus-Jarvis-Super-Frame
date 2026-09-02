import time
import math

class SubmarineEngineering:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_hull = 1908
        self.phase_decoy = 1909
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Undersea Modules: {self.phase_hull} & {self.phase_decoy}")

    # Phase 1908: Pressure Hull Design (दबाव झेलने वाला ढांचा)
    def calculate_hull_integrity(self, depth_meters):
        print(f"\n[Code 01: Pressure Hull - Phase {self.phase_hull}]")
        # P = density * gravity * depth
        pressure_kpa = 1025 * 9.81 * depth_meters / 1000
        print(f"Current Depth: {depth_meters}m | Calculated Pressure: {pressure_kpa:.2f} kPa")
        time.sleep(1.5)
        
        if depth_meters > 800:
            print("Status: Titan-Steel alloy reinforcement engaged. Hull Integrity: 99.8%")
        else:
            print("Status: Normal operating depth. Structural stress: LOW.")
        return f"Hull: SECURE at {depth_meters}m"

    # Phase 1909: Anti-Torpedo Decoys (दुश्मन को गुमराह करना)
    def deploy_decoys(self):
        print(f"\n[Code 02: Anti-Torpedo Decoy - Phase {self.phase_decoy}]")
        print("Incoming Torpedo Signature Detected!")
        time.sleep(1.0)
        
        decoys = ["Acoustic_Noisemaker", "Bubble_Cloud", "Counter_Torpedo"]
        print(f"Action: Releasing {decoys[0]} to mask engine noise...")
        time.sleep(1.2)
        print("Result: Enemy projectile diverted. Submarine position: MASKED.")
        return "Defenses: DEPLOYED"

if __name__ == "__main__":
    sub_tech = SubmarineEngineering()
    
    # दोनों फेजेस का निष्पादन
    hull_report = sub_tech.calculate_hull_integrity(1200)
    decoy_report = sub_tech.deploy_decoys()
    
    print(f"\n--- Submarine Operations Summary ---")
    print(f"Final Status: {hull_report} | {decoy_report}")
