# Optimus Jarvis Super-Frame: Phase 457-458
# Feature: Dynamic Response Generation & Cognitive Context

import random
import time

class JarvisCognitive:
    def __init__(self):
        self.code_ver = "458.Cognitive-Engine"
        self.responses = {
            "GREETING": ["Welcome back, sir.", "Always a pleasure to see you, Deepak.", "Optimus is fully operational and waiting."],
            "SUCCESS": ["Task executed successfully.", "Mission accomplished, sir.", "Process completed without any errors."],
            "ALERT": ["Sir, I've detected a slight anomaly.", "We have a situation that needs your attention.", "Security bypass attempt blocked."]
        }

    def code_457_generate_response(self, category):
        print(f"\n[MODULE 457] Picking Dynamic Response for Category: {category}")
        if category in self.responses:
            # Randomly picking one response
            choice = random.choice(self.responses[category])
            return choice
        return "I'm not sure how to respond to that, sir."

    def code_458_contextual_delivery(self, message):
        print("\n[MODULE 458] Processing Contextual Tone...")
        time.sleep(1)
        # Adding a prefix to show Jarvis's personality
        final_output = f"[JARVIS]: {message}"
        print(final_output)

if __name__ == "__main__":
    brain = JarvisCognitive()
    print(f"--- {brain.code_ver}: Active ---")
    
    # Testing different categories
    greet = brain.code_457_generate_response("GREETING")
    brain.code_458_contextual_delivery(greet)
    
    alert = brain.code_457_generate_response("ALERT")
    brain.code_458_contextual_delivery(alert)
    
    print("\n--- Phase 458 Complete. Jarvis is now more Conversational. ---")
