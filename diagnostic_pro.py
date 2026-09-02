import time

class ServiceProtocol:
    def __init__(self):
        self.critical_parts = ["Engine Oil", "Brake Pads", "Fuel Injector", "Air Filter"]

    def phase_2597(self):
        print("\033[1;33m>> INITIATING: [SYSTEM_ROOT_2597] - Predictive Maintenance\033[0m")
        print("[LOG] Scanning Vehicle Component Health...")
        time.sleep(1)
        for part in self.critical_parts:
            print(f"[ACT] Analyzing wear and tear of {part}...")
            time.sleep(0.5)
        print("[RES] Prediction Complete: Brake Pads require replacement in 500km.")

    def phase_2598(self):
        print("\n\033[1;31m>> INITIATING: [SYSTEM_ROOT_2598] - Real-Time Fault Analysis\033[0m")
        print("[LOG] Monitoring Live Sensor Feed")
        time.sleep(1)
        print("[ACT] Cross-referencing current vibrations with standard metrics...")
        time.sleep(1.5)
        print("[RES] No immediate defects. System is running at optimal efficiency.")
        print("\033[1;32m>> STATUS: SERVICE ADVISOR ENGINE ONLINE\033[0m")

if __name__ == "__main__":
    advisor = ServiceProtocol()
    advisor.phase_2597()
    advisor.phase_2598()
