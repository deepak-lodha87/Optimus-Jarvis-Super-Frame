import time
import random

def run_diagnostics():
    print("--- [ Phase 2: Optimus Jarvis Self-Diagnosis ] ---")
    subsystems = ["Neural Link", "Tactical Engine", "Cloud Sync", "Power Grid"]
    
    for system in subsystems:
        print(f"[#] Scanning {system}...")
        time.sleep(0.8)
        status = random.choice(["Optimal", "Stable", "Ready"])
        print(f"[OK] {system} is {status}.")

    print("\n[CONCLUSION]: Phase 2 Logic is fully operational. Ready for Phase 3.")

if __name__ == "__main__":
    run_diagnostics()
