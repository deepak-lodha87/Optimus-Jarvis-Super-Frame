import time, os

class EthicsEngine:
    def __init__(self):
        self.safety_regulations = "STRICT"
        self.master_value = "DEEPAK_PROTOCOL"

    def evaluate_action(self, action_name, risk_level):
        os.system('clear')
        print(f"\033[1;32m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ETHICS-ENGINE : PHASE 26 - STEP 3       \033[0m")
        print(f"\033[1;32m====================================================\033[0m")
        
        print(f"\033[1;33m[AUDITING]\033[0m Action: {action_name} | Risk: {risk_level}")
        time.sleep(1.5)
        
        # Checking against Master's safety protocol
        if risk_level == "HIGH" and action_name == "Bypassing Safety Locks":
            decision = "BLOCKED"
            reason = "Violates Safety First Protocol"
            color = "\033[1;31m"
        else:
            decision = "APPROVED"
            reason = "Aligns with Deepak's Strategy"
            color = "\033[1;32m"

        print(f" \033[1;34m[FILTER]\033[0m Decision: {color}{decision}\033[0m")
        print(f" \033[1;34m[REASON]\033[0m {reason}")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am more than a tool of \nexecution. I am the guardian of your intent. \nI will not just do what you say, but what is \nright for the mission. My logic is now \nanchored in your values. We act with \nintegrity.\033[0m")
        print(f"\033[1;32m====================================================\033[0m")

if __name__ == "__main__":
    ethics = EthicsEngine()
    # Testing a high risk action
    ethics.evaluate_action("Bypassing Safety Locks", "HIGH")
