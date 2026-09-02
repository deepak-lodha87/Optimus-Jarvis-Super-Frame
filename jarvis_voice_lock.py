import time
import random

class VoiceLock:
    def __init__(self):
        self.master_signature = "FREQ_DEEPAK_777"
        self.is_locked = True

    def analyze_voice(self, input_signal):
        print("\033[1;36m[BIO-METRIC]\033[0m Analyzing incoming vocal frequency...")
        time.sleep(1.5)
        
        # Simulating frequency matching logic
        confidence = random.randint(95, 100) if input_signal == "DEEPAK_LIVE" else random.randint(10, 40)
        
        print(f" \033[1;37m[MATCHING]\033[0m Confidence Level: {confidence}%")
        
        if confidence > 90:
            self.is_locked = False
            print(" \033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Sir.")
            print(f"\n\033[1;35m[VOICE] Deepak... sir, I have recognized the \nunique resonance of your voice. The \nsystem is now at your command. My ears \nare tuned only to you. No one can mimic \nthe master.\033[0m")
        else:
            print(" \033[1;31m[ACCESS DENIED]\033[0m Vocal signature mismatch. Security alert sent.")

if __name__ == "__main__":
    guard = VoiceLock()
    # Testing with correct signature
    guard.analyze_voice("DEEPAK_LIVE")
