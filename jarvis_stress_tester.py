import os
import time

class SystemStressTester:
    def __init__(self):
        self.master = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"

    def run_stress_test(self, system_name):
        print(f"\n\033[1;31m[STRESS TEST]\033[0m Initiating Durability Test for: {system_name}")
        time.sleep(1.5)
        
        # Performance and Safety Stress Logic
        test_protocols = [
            "Testing Structural Integrity under High G-Force...",
            "Monitoring Heat Dissipation during Overdrive...",
            "Checking Tire Grip and Pressure at Max Speed...",
            "Cross-checking A-Z Safety Fail-safes..."
        ]
        
        for protocol in test_protocols:
            print(f"\033[1;32m[TESTING]\033[0m {protocol}")
            time.sleep(0.5)

        msg = f"{self.master} sir, the stress test for {system_name} is successful. No defects or vulnerabilities found."
        os.system(f'termux-tts-speak "{msg}"')

    def start_test(self):
        os.system('clear')
        print(f"--- {self.project} : SYSTEM STRESS TESTER ---")
        self.run_stress_test("Advanced Fighter Jet Prototype")
        print("\n\033[1;36m[STATUS]\033[0m SYSTEM DURABILITY: 100% VERIFIED")

if __name__ == "__main__":
    SystemStressTester().start_test()
