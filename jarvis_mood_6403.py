import time, secrets, random

class JarvisMoodAI:
    def __init__(self):
        self.mood_id = f"NAM-{secrets.token_hex(2).upper()}"

    def analyze_deepak_mood(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-MOOD ONLINE (ID: {self.mood_id}) ---\033[0m")
        print("\033[1;36m[ANALYZING] Vocal Stress & Frequency Patterns...\033[0m")
        
        # Simulating Mood Detection logic
        moods = ["Focused", "Exhausted", "Energetic", "Calm"]
        detected = random.choice(moods)
        time.sleep(1.2)
        
        print(f"\033[1;32m[DETECTED] Current State: {detected}\033[0m")
        self.adjust_system(detected)

    def adjust_system(self, mood):
        if mood == "Exhausted":
            response = "Deepak, you sound tired. I've dimmed the screen and prepared a coding break timer."
        elif mood == "Focused":
            response = "System optimized for deep work. Silence mode activated."
        else:
            response = f"I've adjusted my core to match your {mood} state."
            
        print(f"\033[1;35m[VOICE] {response}\033[0m")

if __name__ == "__main__":
    nam = JarvisMoodAI()
    nam.analyze_deepak_mood()
