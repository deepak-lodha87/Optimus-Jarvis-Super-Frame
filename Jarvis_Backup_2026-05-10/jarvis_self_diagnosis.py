import time

def run_diagnosis():
    print("\033[1;36m[DIAGNOSIS]\033[0m Running Full System Health Check...")
    checks = ["Power Core", "Nano-Armor", "Flight-Thrusters", "Neural-Link"]
    for check in checks:
        print(f" Checking {check}...")
        time.sleep(0.4)
    print("\033[1;32m[RESULT]\033[0m All systems 100% operational. No defects found.")

run_diagnosis()
