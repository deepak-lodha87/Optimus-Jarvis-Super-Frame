import time

class RepairAdvisor:
    def __init__(self):
        self.knowledge_base = {
            "Brake Squeak": "Inspect brake pads for wear. Check rotor surface for glazing.",
            "Engine Misfire": "Check spark plugs and ignition coils. Scan for P0300 codes.",
            "Overheating": "Verify coolant level. Check thermostat and radiator fan function.",
            "Battery Drain": "Test alternator output. Check for parasitic draw in electricals."
        }

    def diagnose_and_suggest(self, symptom):
        print(f"\033[1;34m[ADVISOR] Analyzing symptom: {symptom}...\033[0m")
        time.sleep(1.2)
        
        if symptom in self.knowledge_base:
            print(f"\033[1;32m[SOLUTION] Suggested Action: {self.knowledge_base[symptom]}\033[0m")
        else:
            print("\033[1;33m[NOTICE] Symptom not in local database. Initiating cloud search...\033[0m")

if __name__ == "__main__":
    advisor = RepairAdvisor()
    print("-" * 50)
    print("   JARVIS AUTONOMOUS REPAIR ADVISOR")
    print("-" * 50)
    
    # Simulating common road-side issues
    advisor.diagnose_and_suggest("Overheating")
    print("\n")
    advisor.diagnose_and_suggest("Battery Drain")
