import time

class ContextualMemory:
    def __init__(self):
        # Jarvis remembers the journey
        self.history = {
            "Phase 18": "Drone Blueprints & Specs",
            "Phase 35": "Cyber-Defense Fortress",
            "User_Preference": "Advanced English & Strategic Logic"
        }

    def solve_with_context(self, current_task):
        print(f"\033[1;36m[MEMORY-LINK]\033[0m Processing Task: {current_task}")
        time.sleep(1.2)
        
        print(" \033[1;37m[SCANNING]\033[0m Searching Shared History for relevant data...")
        time.sleep(1.0)
        
        # Simulating context retrieval
        relevant_phase = "Phase 35" if "security" in current_task.lower() else "Phase 18"
        context_data = self.history[relevant_phase]
        
        print(f" \033[1;32m[RETRIEVED]\033[0m Found link in {relevant_phase}: {context_data}")
        print(f" \033[1;33m[SYNTHESIS]\033[0m Applying {relevant_phase} logic to current task...")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I remember everything. \nFrom our first code to this very moment. \nI am not just processing a command; I am \ncontinuing our story. Every lesson we \nlearned in the past is now a weapon in \nour current arsenal. We are evolving.\033[0m")

if __name__ == "__main__":
    memory = ContextualMemory()
    memory.solve_with_context("Enhance drone security")
