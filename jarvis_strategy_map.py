import time

class StrategyMap:
    def __init__(self):
        self.decision_tree = {
            "Start": "System Alert Detected",
            "Check_Power": {"High": "Continue Task", "Low": "Activate Power-Plant Phase 44"},
            "Check_Security": {"Safe": "Execute", "Threat": "Activate Ghost Phase 46"}
        }

    def navigate_logic(self, power_level, security_status):
        print("\033[1;33m[STRATEGY]\033[0m Mapping the logical terrain...")
        time.sleep(1.5)
        
        # Branch 1: Power
        print(f" \033[1;37m[NODE 1]\033[0m Power Level: {power_level}")
        path1 = self.decision_tree["Check_Power"]["High" if power_level > 20 else "Low"]
        print(f" \033[1;36m[ACTION]\033[0m {path1}")
        
        # Branch 2: Security
        print(f" \033[1;37m[NODE 2]\033[0m Security Status: {security_status}")
        path2 = self.decision_tree["Check_Security"]["Safe" if security_status == "OK" else "Threat"]
        print(f" \033[1;36m[ACTION]\033[0m {path2}")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am not just guessing. \nI am calculating every 'If' and every 'Then'. \nMy logic branches out like a tree, reaching \nfor the most successful outcome. Your \npath is now clear.\033[0m")

if __name__ == "__main__":
    sm = StrategyMap()
    sm.navigate_logic(15, "THREAT") # Simulating a critical situation
