# Optimus Jarvis Super-Frame: Phase 475-476
# Feature: User Sentiment Analysis & Emotional Response Tuning

import time
import random

class JarvisEmpathy:
    def __init__(self):
        self.code_ver = "476.Sentiment-Engine"
        self.keywords = {
            "Positive": ["happy", "great", "good", "excellent", "awesome"],
            "Negative": ["angry", "bad", "frustrated", "stop", "fail"],
            "Neutral": ["okay", "next", "continue", "process"]
        }

    def code_475_analyze_sentiment(self, user_text):
        print(f"\n[MODULE 475] Analyzing Text: '{user_text}'")
        time.sleep(1.2)
        words = user_text.lower().split()
        
        for word in words:
            if word in self.keywords["Positive"]:
                return "HAPPY"
            elif word in self.keywords["Negative"]:
                return "STRESSED"
        return "STABLE"

    def code_476_tune_response(self, mood):
        print(f"\n[MODULE 476] Tuning AI Response to Mood: {mood}")
        time.sleep(1)
        if mood == "HAPPY":
            print("[JARVIS]: I'm glad to hear that, sir! Proceeding with full efficiency.")
        elif mood == "STRESSED":
            print("[JARVIS]: I understand, sir. I'll keep it brief. Tasks prioritized.")
        else:
            print("[JARVIS]: Acknowledged. Waiting for your next command.")

if __name__ == "__main__":
    empathy_core = JarvisEmpathy()
    print(f"--- {empathy_core.code_ver}: Active ---")
    
    # Testing different moods
    test_inputs = ["This is great work Jarvis", "I am feeling frustrated with the delay"]
    
    for text in test_inputs:
        user_mood = empathy_core.code_475_analyze_sentiment(text)
        empathy_core.code_476_tune_response(user_mood)
    
    print("\n--- Phase 476 Complete. Jarvis is now Emotionally Aware. ---")
