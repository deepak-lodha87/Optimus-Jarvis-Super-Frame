# Optimus Jarvis Super-Frame: Phase 421-422
# Feature: Adaptive Learning & User Preference Profile

import json
import os

class JarvisAdaptive:
    def __init__(self):
        self.code_ver = "422.Adaptive"
        self.profile_file = "user_preferences.json"
        self.preferences = self.load_preferences()

    def load_preferences(self):
        if os.path.exists(self.profile_file):
            with open(self.profile_file, 'r') as f:
                return json.load(f)
        return {"user_style": "Tactical", "last_command": None}

    def code_421_learn_preference(self, command):
        print(f"\n[MODULE 421] Analyzing User Command Pattern: '{command}'")
        # Learning logic: Updating preference based on command
        self.preferences["last_command"] = command
        with open(self.profile_file, 'w') as f:
            json.dump(self.preferences, f)
        print("[SYSTEM] Preference pattern updated in Neural Profile.")

    def code_422_apply_adaptation(self):
        print("\n[MODULE 422] Applying System Adaptation...")
        style = self.preferences.get("user_style", "Standard")
        print(f"[STATUS] System Interface optimized for '{style}' mode.")
        print(f"[MEMORY] Recalling last interaction: {self.preferences['last_command']}")

if __name__ == "__main__":
    adaptive_engine = JarvisAdaptive()
    print(f"--- {adaptive_engine.code_ver}: Operational ---")
    
    # Simulating a learning session
    adaptive_engine.code_421_learn_preference("Initialize Stealth Recon")
    adaptive_engine.code_422_apply_adaptation()
    
    print("\n--- Phase 422 Complete. Jarvis is now Evolving. ---")
