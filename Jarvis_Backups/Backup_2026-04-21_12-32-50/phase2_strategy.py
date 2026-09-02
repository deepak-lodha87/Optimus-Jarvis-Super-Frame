import time

class OptimusJarvis:
    def __init__(self):
        self.identity = "Optimus Jarvis Super-Frame"
        self.strategy_level = "Captain America Protocol"

    def tactical_analysis(self, situation):
        print(f"\n[!] Analyzing Situation: {situation}")
        time.sleep(1)
        
        # Strategic Decision Logic
        strategies = {
            "low_threat": "Monitor and report. No immediate action required.",
            "medium_threat": "Initiate defensive maneuvers and alert user.",
            "high_threat": "Execute counter-measures and activate full shield protocols."
        }
        
        # Simulating a strategic scan
        print(f"[+] Applying {self.strategy_level}...")
        time.sleep(1)
        
        if "danger" in situation.lower():
            return strategies["high_threat"]
        elif "warning" in situation.lower():
            return strategies["medium_threat"]
        else:
            return strategies["low_threat"]

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    # Example Scenario
    result = jarvis.tactical_analysis("Detected a high-level danger in the network.")
    print(f"\n[STRATEGIC ADVICE]: {result}")
