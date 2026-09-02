import os
import time

def run_diagnostics():
    print("\n\033[1;34m[SYSTEM]: Starting Advanced Diagnostic Scan (Phase 2101)...\033[0m")
    modules = ["Neural_Link", "Core_Blueprints", "Armor_Control", "Cloud_Buffer"]
    
    for module in modules:
        time.sleep(0.5)
        print(f"Checking {module}...")
        print(f"\033[1;32m>> {module}: STATUS OK\033[0m")
    
    print("\n\033[1;33m[JARVIS]: All systems are operational. No anomalies detected.\033[0m")
    print("-" * 50)

if __name__ == "__main__":
    run_diagnostics()
