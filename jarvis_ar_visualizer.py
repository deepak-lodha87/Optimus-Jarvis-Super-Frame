import time
import random

class ARVisualizer:
    def __init__(self):
        self.rendering_engine = "Optimus-AR Core"
        self.overlay_active = False

    def activate_camera_overlay(self):
        print("\033[1;36m[AR] Initializing Augmented Reality Layer...\033[0m")
        time.sleep(1.2)
        print("  • Calibrating Reno 12 Pro Camera Sensors... [OK]")
        print("  • Mapping Spatial Environment... [STABLE]")
        self.overlay_active = True
        return "\033[1;32m[SUCCESS] Hybrid AR Visualizer is now LIVE.\033[0m"

class HUD_Overlay:
    def stream_telemetry(self, machine_name):
        print(f"\033[1;35m[HUD] Projecting Telemetry for {machine_name}...\033[0m")
        # Simulating live data projection on screen
        for i in range(5):
            val = random.randint(60, 95)
            print(f"  • HUD_LAYER >> {machine_name}_POWER: {val}% | TEMP: 34°C")
            time.sleep(0.4)
        return "\033[1;34m[INFO] HUD Overlay synchronized with Machine Sensors.\033[0m"

if __name__ == "__main__":
    ar = ARVisualizer()
    hud = HUD_Overlay()
    
    print("-" * 50)
    print("   JARVIS HYBRID AR & HUD INTERFACE (P3161-62)")
    print("-" * 50)
    
    print(ar.activate_camera_overlay())
    print("\n" + hud.stream_telemetry("UNIT-V8-ENGINE"))
    print("-" * 50)
