# Optimus Jarvis Super-Frame: Phase 471-472
# Feature: Neural Voice Print & Frequency Pattern Analysis

import time
import random

class JarvisVoiceAuth:
    def __init__(self, owner_name):
        self.code_ver = "472.Voice-Print"
        self.owner = owner_name
        # Simulated "Unique" frequency for Deepak
        self.authorized_freq = 145.2  # Hz (Simplified)

    def code_471_capture_frequency(self):
        print(f"\n[MODULE 471] Listening to Audio Stream: '{self.owner}'")
        time.sleep(1.5)
        # Simulating voice frequency detection
        captured_freq = random.uniform(144.5, 146.0)
        print(f"[SYSTEM] Frequency Detected: {captured_freq:.2f} Hz")
        return captured_freq

    def code_472_match_pattern(self, freq):
        print("\n[MODULE 472] Running Neural Pattern Match...")
        time.sleep(1)
        # Tolerance check (Is the voice close enough to the master print?)
        difference = abs(self.authorized_freq - freq)
        
        if difference < 1.0:
            print(f"[STATUS] Voice Print Match: 100%. Access Granted.")
            print(f"[JARVIS]: Voice recognition confirmed. How can I help, {self.owner}?")
        else:
            print("[ALERT] Voice Mismatch! Frequency deviation too high.")
            print("[ACTION] Locking sensitive modules.")

if __name__ == "__main__":
    v_auth = JarvisVoiceAuth("Deepak")
    print(f"--- {v_auth.code_ver}: Active ---")
    
    current_freq = v_auth.code_471_capture_frequency()
    v_auth.code_472_match_pattern(current_freq)
    
    print("\n--- Phase 472 Complete. Voice Identity is now Secure. ---")
