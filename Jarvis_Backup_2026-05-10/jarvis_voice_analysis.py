import time
import random

class VoiceEngine:
    def __init__(self):
        self.sampling_rate = "44.1kHz"
        self.status = "Monitoring Frequency"

    def analyze_tone(self, frequency_hz):
        print(f"\033[1;35m[AUDIO] Analyzing Input Frequency: {frequency_hz} Hz...\033[0m")
        time.sleep(1.2)
        
        # Frequency ranges for mood detection logic
        if frequency_hz > 300:
            mood = "EXCITED / URGENT"
            action = "Increasing system response speed."
        elif 150 <= frequency_hz <= 300:
            mood = "CALM / STEADY"
            action = "Maintaining standard operational protocols."
        else:
            mood = "TIRED / LOW ENERGY"
            action = "Switching to supportive/empathetic tone."
            
        print(f"\033[1;32m[RESULT] Mood Detected: {mood}\033[0m")
        print(f"• Jarvis Action: {action}")

if __name__ == "__main__":
    voice = VoiceEngine()
    print("-" * 50)
    print("   JARVIS VOICE FREQUENCY ANALYZER")
    print("-" * 50)
    
    # Simulating different voice frequencies
    test_frequencies = [210, 450, 120]
    for freq in test_frequencies:
        voice.analyze_tone(freq)
        print("-" * 30)
