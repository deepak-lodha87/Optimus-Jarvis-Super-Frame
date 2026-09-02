import time

class JarvisRescueSystem:
    def __init__(self):
        self.project = "Optimus Jarvis Super-Frame"
        self.phase = "1023-1024"
        self.system_health = 100
        self.emergency_mode = False

    def activate_emergency_protocol(self):
        """
        Phase 1023: Detecting critical system failures and isolating them.
        """
        print(f"\n[JARVIS] Monitoring Core Stability...")
        # Simulating a sudden drop in health
        self.system_health = 45 
        
        if self.system_health < 50:
            print(f"!!! CRITICAL WARNING: System Health at {self.system_health}% !!!")
            self.emergency_mode = True
            print("[JARVIS] Initiating Emergency Lockdown & Power-Save Mode.")

    def auto_rescue_logic(self):
        """
        Phase 1024: Auto-repairing and rerouting power to keep Jarvis alive.
        """
        if not self.emergency_mode:
            print("\n[JARVIS] System is stable. No rescue needed.")
            return

        print(f"\n[JARVIS] Running Auto-Rescue Sequence...")
        time.sleep(1.5)
        
        # Rerouting logical pathways
        print("Action: Rerouting Neural-Link to Backup Cloud Core...")
        self.system_health = 100
        self.emergency_mode = False
        print(f"RESULT: System Restored to {self.system_health}%. Zero-Failure Maintained.")

if __name__ == "__main__":
    rescue = JarvisRescueSystem()
    print(f"--- {rescue.project} | Phase {rescue.phase} ---")
    
    # 1. Check for emergency (Phase 1023)
    rescue.activate_emergency_protocol()
    
    # 2. Rescue and Repair (Phase 1024)
    rescue.auto_rescue_logic()

    print("\n[SYSTEM] Emergency & Auto-Rescue modules are now permanent, Deepak.")
