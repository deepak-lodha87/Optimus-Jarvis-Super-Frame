import time
import random

class HeuristicEngine:
    def __init__(self):
        self.experience_db = {"Overheat": "Reduce CPU Load", "Low_Memory": "Clear Cache"}

    def solve_problem(self, issue):
        print(f"\033[1;34m[HEURISTIC] Analyzing issue: {issue}...\033[0m")
        time.sleep(1)
        if issue in self.experience_db:
            solution = self.experience_db[issue]
            return f"\033[1;32m[SOLVED] Applied past experience: {solution}\033[0m"
        else:
            print("[LEARNING] New issue detected. Generating heuristic trial...")
            time.sleep(1.5)
            return "\033[1;33m[NEW STRATEGY] Logic updated for future occurrences.\033[0m"

class DecisionEngine:
    def execute_priority(self):
        tasks = ["Backup", "Security Scan", "Code Optimization"]
        chosen = random.choice(tasks)
        print(f"\033[1;35m[DECISION] Jarvis has independently prioritized: {chosen}\033[0m")
        time.sleep(1)
        return f"[STATUS] {chosen} is now running in background."

if __name__ == "__main__":
    h_brain = HeuristicEngine()
    d_engine = DecisionEngine()
    
    print("-" * 50)
    print("   JARVIS HEURISTIC & AUTONOMOUS ENGINE")
    print("-" * 50)
    
    # Testing experience-based solving
    print(h_brain.solve_problem("Overheat"))
    print("\n")
    # Testing independent decision making
    print(d_engine.execute_priority())
    print("-" * 50)
