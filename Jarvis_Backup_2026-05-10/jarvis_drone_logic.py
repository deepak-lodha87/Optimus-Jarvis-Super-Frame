import time

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.drone_unit = "Spectre-7"
        self.mapping_data = "Scanning..."

    def phase_1462_drone_surveillance(self):
        print("\n--- [ PHASE 1462: DRONE SURVEILLANCE ] ---")
        print(f">> Deploying Drone Unit: {self.drone_unit}")
        time.sleep(0.5)
        protocols = ["Thermal Imaging", "Motion Detection", "Signal Jamming"]
        for p in protocols:
            print(f"   [ACTIVE]: {p}")
        print(">> Status: Perimeter secured by aerial units.")

    def phase_1463_aerial_mapping(self):
        print("\n--- [ PHASE 1463: AERIAL BLUEPRINT MAPPING ] ---")
        print(">> Initializing 360-degree Topographic Scan...")
        time.sleep(0.6)
        self.mapping_data = "Topographic Mesh Generated"
        print(f">> Data: {self.mapping_data}")
        print(">> Accuracy: 99.9% (Verified against GPS coordinates)")

    def run_reconnaissance(self):
        print(f"--- [ OPTIMUS JARVIS: RECON PROTOCOLS ] ---")
        self.phase_1462_drone_surveillance()
        self.phase_1463_aerial_mapping()
        print("-" * 45)
        print(f">> {self.user}, global mapping and aerial oversight are operational.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.run_reconnaissance()
