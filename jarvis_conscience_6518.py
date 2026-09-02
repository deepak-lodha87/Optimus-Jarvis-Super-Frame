import time, secrets, random

class JarvisConscience:
    def __init__(self):
        self.personality_id = f"NACo-{secrets.token_hex(2).upper()}"
        self.current_mood = "Neutral"

    def analyze_user_mood(self, user_input):
        print(f"\n\033[1;37m--- NEURAL-AUTO-CONSCIENCE V1 ONLINE (ID: {self.personality_id}) ---\033[0m")
        print("\033[1;36m[SENSING] Analyzing vocal frequencies and sentiment...\033[0m")
        time.sleep(1.2)
        
        # Simulating mood detection
        moods = ["Focused", "Tired", "Energetic", "Serious"]
        detected_mood = random.choice(moods)
        self.current_mood = detected_mood
        
        print(f"\033[1;32m[DETECTED] Deepak's State: {detected_mood}\033[0m")
        self.respond_with_empathy(detected_mood)

    def respond_with_empathy(self, mood):
        responses = {
            "Focused": "Understood. I will keep my reports brief and precise to match your focus.",
            "Tired": "I've optimized the background tasks. You should take a break, I'll monitor everything.",
            "Energetic": "Systems are at 100%! Let's push some heavy code today, Deepak.",
            "Serious": "I am standing by with full tactical protocols. Ready for your command."
        }
        print(f"\033[1;33m[ADAPTING] Adjusting Jarvis Persona to {mood} mode...\033[0m")
        time.sleep(0.8)
        print(f"\033[1;35m[VOICE] {responses[mood]}\033[0m")

if __name__ == "__main__":
    conscience = JarvisConscience()
    conscience.analyze_user_mood("Jarvis, update status.")
