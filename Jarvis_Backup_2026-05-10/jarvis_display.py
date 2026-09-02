import time
import sys

def visual_scanner():
    frames = ["[■□□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■■■]"]
    for frame in frames:
        sys.stdout.write(f"\r>> SCANNING SYSTEM INTEGRITY: {frame}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n>> SCAN COMPLETE: 100% OPERATIONAL")

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"

    def phase_1480_visual_console(self):
        print("\n" + "="*50)
        print("      O P T I M U S   J A R V I S   S U P E R - F R A M E")
        print("="*50)
        visual_scanner()
        print("-" * 50)
        print(">> INITIALIZING TACTICAL INTERFACE...")
        time.sleep(0.5)

    def phase_1481_hardware_mapping(self):
        components = ["CORE-PROCESSOR", "NEURAL-LINK", "ARMOR-SENSORS", "POWER-TRAIN"]
        for comp in components:
            print(f"   [ONLINE] --> {comp}")
            time.sleep(0.2)
        print("-" * 50)
        print(f">> {self.user}, the workshop environment is simulated.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.phase_1480_visual_console()
    jarvis.phase_1481_hardware_mapping()
