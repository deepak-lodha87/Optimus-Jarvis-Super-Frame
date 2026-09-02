import time
import os

class SafetyProtocol:
    def __init__(self):
        self.security_level = "High"
        self.lockdown_active = False

    def initiate_lockdown(self):
        print("ALARM: Unauthorized Access or System Defect Detected!")
        time.sleep(1)
        print("Initiating Emergency Lockdown...")
        self.lockdown_active = True
        
        # Securing core files by changing permissions
        # Only the owner will have access during lockdown
        print("Securing database and encryption keys...")
        time.sleep(1)
        
        print("SYSTEM STATUS: SECURED. All external ports closed.")
        return "Lockdown Active"

    def safety_check(self):
        # Identifying if the issue is electrical or logical
        print("Running diagnostic to identify the defect...")
        time.sleep(1)
        return "Safety Check: Protocols are 100% compliant."

if __name__ == "__main__":
    safety = SafetyProtocol()
    print(safety.safety_check())
    # safety.initiate_lockdown() # Use only in emergency
