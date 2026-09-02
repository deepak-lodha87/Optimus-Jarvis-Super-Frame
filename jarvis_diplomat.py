import time
import random

class JarvisDiplomat:
    def __init__(self):
        self.strategies = {
            "Professional": "Focus on facts, maintain a 'Dapper' tone, and keep it concise.",
            "Persuasive": "Start with a shared goal, use emotional hooks, and end with a clear ask.",
            "Empathic": "Acknowledge feelings first, use soft words, and offer support without pressure."
        }

    def suggest_message(self, context):
        print(f"\033[1;36m[DIPLOMAT]\033[0m Analyzing relationship dynamics for: {context}")
        time.sleep(2)
        
        if "Negotiation" in context:
            strat = "Persuasive"
        elif "Apology" in context or "Support" in context:
            strat = "Empathic"
        else:
            strat = "Professional"
            
        print(f" \033[1;33m[STRATEGY]\033[0m Selected Approach: {strat}")
        print(f" \033[1;37m[GUIDE]\033[0m {self.strategies[strat]}")
        time.sleep(1.5)
        
        print(f"\n\033[1;32m[SUGGESTION]\033[0m If the context is 'Relationship', Jarvis recommends: \n'I value our bond and I've been thinking about our recent silence. \nI'm here whenever you're ready to talk.'")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, words are the most \npowerful weapons we possess. I have \ndesigned this strategy to ensure your \nvoice is heard, respected, and felt. \nVictory isn't always won on the field; \nsometimes it's won in the heart.\033[0m")

if __name__ == "__main__":
    diplomat = JarvisDiplomat()
    diplomat.suggest_message("Relationship Re-engagement")
