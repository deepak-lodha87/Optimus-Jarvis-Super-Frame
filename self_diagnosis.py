import os

class JarvisSelfDiagnosis:
    def __init__(self):
        self.systems = ["Perception", "Navigation", "Power_Train", "Network"]

    def run_check(self):
        print("Starting System Self-Diagnosis...")
        for system in self.systems:
            # Simulating a safety check
            print(f"Checking {system} Status: [OK]")
        
        print("\nSafety Status: All protocols are within nominal limits.")
        return "System Healthy"

    def identify_defect(self, component):
        # Logic to find if the issue is electrical or offline
        status = "Electrical Defect Detected" if component == "Power" else "Connectivity Offline"
        print(f"Alert: {status} in {component} module.")
        print("Solution: Initiating secondary backup circuits.")

if __name__ == "__main__":
    diagnosis = JarvisSelfDiagnosis()
    diagnosis.run_check()
