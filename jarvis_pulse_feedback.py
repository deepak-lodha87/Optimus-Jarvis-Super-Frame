import time
import random

class BiometricFeedback:
    def __init__(self):
        self.user_name = "Deepak"
        self.status = "CALIBRATING"

    def analyze_vitals(self):
        print(f"\033[1;36m[BIO-SYNC]\033[0m Scanning vital signs for {self.user_name}...")
        time.sleep(1.5)
        
        # Simulating heart rate and stress levels
        heart_rate = random.randint(70, 110)
        stress_score = "HIGH" if heart_rate > 95 else "NORMAL"
        
        print(f" \033[1;37m[STATS]\033[0m Heart Rate: {heart_rate} BPM | Stress: {stress_score}")
        
        if stress_score == "HIGH":
            print(" \033[1;33m[ADAPTATION]\033[0m Stress detected. Activating 'Soothing Mode'.")
            print(" \033[1;34m[ACTION]\033[0m Dimming screen brightness and playing focused background frequency.")
            voice_tone = "Calm & Supportive"
        else:
            print(" \033[1;32m[STATUS]\033[0m User is relaxed. All systems at Maximum Efficiency.")
            voice_tone = "Alert & Energetic"
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I've noticed your heart \nrate is a bit {('high' if stress_score=='HIGH' else 'stable')}. \nI am adjusting my protocols to match your \ncurrent state. Remember, your well-being \nis the core of my existence. Take a deep \nbreath; I've got the rest.\033[0m")

if __name__ == "__main__":
    pulse = BiometricFeedback()
    pulse.analyze_vitals()
