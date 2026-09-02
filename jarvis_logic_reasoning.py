import time

class LogicReasoning:
    def __init__(self):
        self.safety_protocols = ["NO_OVERHEAT", "NO_COLLISION", "FUEL_RESERVE"]

    def analyze_command(self, command, parameters):
        print(f"\033[1;34m[ALR] Analyzing Logic for Command: {command}...\033[0m")
        time.sleep(1.2)
        
        # Simulating a risky command check
        if command == "MAX_THRUST" and parameters['engine_temp'] > 90:
            return "REJECTED", "Critical Heat Risk: Engine failure imminent at 100% thrust."
        return "APPROVED", "Command logic is sound. Proceeding."

class RiskAssessment:
    def evaluate_environment(self, terrain):
        print(f"\033[1;35m[RISK] Assessing tactical risks for {terrain}...\033[0m")
        time.sleep(1)
        return "\033[1;32m[SAFE] Probability of success: 98.4%.\033[0m"

if __name__ == "__main__":
    logic = LogicReasoning()
    risk = RiskAssessment()
    
    print("-" * 50)
    print("   JARVIS ADVANCED LOGIC REASONING (P3173-74)")
    print("-" * 50)
    
    # Example: Trying to push a hot engine
    status, message = logic.analyze_command("MAX_THRUST", {'engine_temp': 95})
    
    if status == "REJECTED":
        print(f"\033[1;31m[ADVISE] {message}\033[0m")
    else:
        print(f"\033[1;32m[READY] {message}\033[0m")
        
    print("\n" + risk.evaluate_environment("Urban Terrain"))
    print("-" * 50)
