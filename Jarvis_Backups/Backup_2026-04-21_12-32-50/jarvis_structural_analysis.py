import time

class StructuralIntegrity:
    def __init__(self):
        self.safety_threshold = 0.85  # 85% safety minimum
        self.materials = {
            "Steel": {"strength": 250, "durability": "High"},
            "Aluminum": {"strength": 70, "durability": "Medium"},
            "Carbon Fiber": {"strength": 600, "durability": "Extreme"},
            "Titanium": {"strength": 450, "durability": "High"}
        }

    def analyze_stress(self, material, load_kn):
        print(f"\033[1;34m[ANALYSIS] Material: {material} | Applied Load: {load_kn}kN\033[0m")
        time.sleep(1)
        
        if material in self.materials:
            strength = self.materials[material]["strength"]
            stress_ratio = load_kn / strength
            
            if stress_ratio > 1.0:
                return f"\033[1;31m[CRITICAL] Structure Failure! Load exceeds {material} limits.\033[0m"
            elif stress_ratio > self.safety_threshold:
                return f"\033[1;33m[WARNING] Stress high. Structural deformation possible.\033[0m"
            else:
                return f"\033[1;32m[SAFE] Structural Integrity Verified. Status: {self.materials[material]['durability']}\033[0m"
        return "[ERROR] Material data not found."

if __name__ == "__main__":
    sia = StructuralIntegrity()
    print("-" * 50)
    print("   JARVIS STRUCTURAL INTEGRITY ANALYZER")
    print("-" * 50)
    
    # Testing a Carbon Fiber frame with high load
    print(sia.analyze_stress("Carbon Fiber", 500))
    # Testing Aluminum with excessive load
    print(sia.analyze_stress("Aluminum", 100))
