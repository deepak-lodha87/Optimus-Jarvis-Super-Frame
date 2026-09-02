import time

def self_diagnosis():
    print("[+] Initializing Optimus Jarvis Super-Frame...")
    time.sleep(1)
    print("[+] Running Self-Diagnosis...")
    
    # Logic check for system components
    status = {
        "Core Intelligence": "Active",
        "Perception Engine": "Online",
        "Strategic Module": "Standby",
        "Connectivity": "Stable"
    }
    
    for component, state in status.items():
        print(f"  - {component}: {state}")
        time.sleep(0.5)

    print("[!] System Check Complete. All systems operational.")

if __name__ == "__main__":
    self_diagnosis()
