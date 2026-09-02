# Optimus Jarvis Super-Frame: Phase 11 (Combat Intelligence)
# Logic: Threat Assessment & Counter-Measure Deployment

class CombatModule:
    def __init__(self):
        self.module_name = "Tactical Combat Intelligence"
        self.threats = {"Alpha": 85, "Bravo": 40, "Charlie": 15}

    def assess_threats(self):
        print(f"\n[{self.module_name}] Scanning for immediate threats...")
        # Sorting threats by priority
        sorted_threats = sorted(self.threats.items(), key=lambda x: x[1], reverse=True)
        
        for threat, level in sorted_threats:
            status = "CRITICAL" if level > 70 else "MODERATE"
            print(f"[THREAT] {threat}: Level {level}% - Status: {status}")

    def deploy_counter_measures(self):
        print("\n[SYSTEM] Deploying Counter-Measures...")
        print("[ACTION] Alpha threat neutralized via Cyber-Shield.")
        print("[ACTION] Scenario stable. Awaiting next phase.")

if __name__ == "__main__":
    print("--- Optimus Jarvis: Combat Mode Initiated ---")
    combat = CombatModule()
    combat.assess_threats()
    combat.deploy_counter_measures()
