import time
import random

class NeuralFeedback:
    def analyze_input_patterns(self):
        print("\033[1;34m[FEEDBACK] Monitoring typing cadence and error rate...\033[0m")
        time.sleep(1.2)
        # Simulating metrics
        wpm = random.randint(30, 80)
        error_rate = random.uniform(0.1, 5.0)
        
        print(f"  • Speed: {wpm} WPM")
        print(f"  • Accuracy: {100 - error_rate:.2f}%")
        
        if error_rate > 3.0:
            return "High Stress Detected"
        return "Optimal Focus Detected"

class AdaptiveInterface:
    def adjust_vibe(self, state):
        print(f"\033[1;35m[ADAPT] System State: {state}. Adjusting UI...\033[0m")
        time.sleep(1)
        if state == "High Stress Detected":
            return "\033[1;36m[MODE] Soft-Blue 'Calm' UI Activated. Minimizing alerts.\033[0m"
        return "\033[1;32m[MODE] Standard 'Efficiency' UI Active. Full power authorized.\033[0m"

if __name__ == "__main__":
    nf = NeuralFeedback()
    ai = AdaptiveInterface()
    
    print("-" * 50)
    print("   JARVIS BEHAVIORAL FEEDBACK LOOP (P3091-92)")
    print("-" * 50)
    
    current_state = nf.analyze_input_patterns()
    print(f"Analysis: {current_state}")
    print("\n" + ai.adjust_vibe(current_state))
    print("-" * 50)
