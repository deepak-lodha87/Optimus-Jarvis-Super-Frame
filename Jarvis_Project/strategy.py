import time

class JarvisStrategy:
    def __init__(self):
        self.module = "Neural Strategic Planner"
        self.threat_levels = ["Safe", "Low", "Medium", "High", "Extraterrestrial"]

    def analyze_situation(self, situation_desc):
        print(f"\n[+] Analyzing Situation: {situation_desc}")
        time.sleep(1.5)
        # Strategic Logic: If 'alien' or 'enemy' is in description
        if "alien" in situation_desc.lower() or "ufo" in situation_desc.lower():
            risk = "Extraterrestrial"
        elif "attack" in situation_desc.lower():
            risk = "High"
        else:
            risk = "Medium"
        
        print(f"[!] Threat Level Detected: {risk}")
        return risk

    def formulate_plan(self, risk):
        print("\n[+] Formulating Counter-Strategy...")
        time.sleep(1)
        if risk == "Extraterrestrial":
            print("[STRATEGY] Deploying: Phase 313 Anti-Gravity Core & Phase 316 Exotic Alloys.")
            print("[ACTION] Recommendation: Initiate First Contact Protocol or Evasive Maneuvers.")
        elif risk == "High":
            print("[STRATEGY] Deploying: Defensive Shields & Resource Reallocation.")
        else:
            print("[STRATEGY] Status: Surveillance Mode Active. No immediate threat.")
        
        print("[SUCCESS] Strategic Plan Ready for Execution.")

if __name__ == "__main__":
    planner = JarvisStrategy()
    print("--- Jarvis Strategic Command ---")
    sit = input("Identify the threat/situation: ")
    risk_level = planner.analyze_situation(sit)
    planner.formulate_plan(risk_level)
